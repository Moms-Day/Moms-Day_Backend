git pull
sudo kill $(ps a | grep python | grep -v "grep" | grep -v "python3 hook_app.py" |  awk '{print $1}')
cd Server
sudo -E python3 server.py