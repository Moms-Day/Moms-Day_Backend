import os
import socket

from flask import Flask, Response


app = Flask(__name__)


@app.route('/hook', methods=['POST'])
def hook():
    os.system('./hook.sh')

    return Response('hook!', 200)


if __name__ == '__main__':
    app.run(port=9090, debug=True, host=socket.gethostbyname(socket.gethostname()))
