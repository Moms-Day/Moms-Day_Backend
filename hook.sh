git pull
sudo kill $(ps a | grep python | grep -v "grep" |  awk '{print $1}')
sudo -E python3 server.py