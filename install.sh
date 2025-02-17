#!/bin/bash

echo "Installing Server Monitoring Agent..."
sudo apt update
sudo apt install -y python3 python3-pip

# Download the agent script
curl -o /usr/local/bin/server_monitor.py https://yourserver.com/server_monitor.py
chmod +x /usr/local/bin/server_monitor.py

# Set up a systemd service to run the script periodically
cat <<EOF | sudo tee /etc/systemd/system/server_monitor.service
[Unit]
Description=Server Monitoring Agent
After=network.target

[Service]
ExecStart=/usr/bin/python3 /usr/local/bin/server_monitor.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the service
sudo systemctl enable server_monitor
sudo systemctl start server_monitor

echo "Installation complete!"
