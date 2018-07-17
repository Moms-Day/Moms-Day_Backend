git pull
sudo kill $(ps a | grep python | grep -v "grep" | grep -v "python3 hook_app.py" |  awk '{print $1}')
sudo -E python3 ./Server/server.py