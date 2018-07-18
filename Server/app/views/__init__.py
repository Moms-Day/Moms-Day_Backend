from functools import wraps
import gzip
import time

import ujson

from flask import Response, abort, after_this_request, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response


def gzipped(fn):
    """
    View decorator for gzip compress the response body
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        @after_this_request
        def zipper(response):
            if 'gzip' not in request.headers.get('Accept-Encoding', '')\
                    or not 200 <= response.status_code < 300\
                    or 'Content-Encoding' in response.headers:
                # 1. Accept-Encoding에 gzip이 포함되어 있지 않거나
                # 2. 200번대의 status code로 response하지 않거나
                # 3. response header에 이미 Content-Encoding이 명시되어 있는 경우
                return response

            response.data = gzip.compress(response.data)
            response.headers.update({
                'Content-Encoding': 'gzip',
                'Vary': 'Accept-Encoding',
                'Content-Length': len(response.data)
            })

            return response
        return fn(*args, **kwargs)
    return wrapper


def auth_required(model):
    def decorator(fn):
        """
        View decorator for access control
        """
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            raise NotImplementedError()

            # return fn(*args, **kwargs)
        return wrapper
    return decorator


def json_required(required_keys):
    def decorator(fn):
        if fn.__name__ == 'get':
            print('[WARNING] JSON with GET method? on "{}()"'.format(fn.__qualname__))

        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)

            for key, typ in required_keys.items():
                if key not in request.json or not type(request.json[key]) is typ:
                    abort(400)
                # if typ is str and not request.json[key]:
                #     abort(400)
                # if typ is list and not request.json[key]:
                #     abort(400)
                # if typ is dict and not request.json[key]:
                #     abort(400)
                # if typ is tuple and not request.json[key]:
                #     if (typ[0] is not list) or (typ[1] is not dict):
                #         abort(400)

            return fn(*args, **kwargs)
        return wrapper
    return decorator


class BaseResource(Resource):
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200, **kwargs) -> Response:
        """
        Helper function which processes json response with unicode using ujson

        Args:
            data (dict and list): Data for dump to JSON
            status_code (int): Status code for response
        """
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8',
            **kwargs
        )

    class ValidationError(Exception):
        def __init__(self, description='', *args):
            self.description = description

            super(BaseResource.ValidationError, self).__init__(*args)


class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.after_request(after_request)

        from app.views import sample
        app.register_blueprint(sample.api.blueprint)

        from app.views import hook
        app.register_blueprint(hook.api.blueprint)

        from app.views.careworker import signup, auth
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(auth.api.blueprint)

        from app.views.daughter import signup, auth, ranking, evaluate, info
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(ranking.api.blueprint)
        app.register_blueprint(evaluate.api.blueprint)
        app.register_blueprint(info.api.blueprint)
