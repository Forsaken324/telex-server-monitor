import psutil
import requests
import socket

SERVER_URL = "https://yourserver.com/report"  # Your FastAPI endpoint
USER_ID = "user-unique-id"  # This should be generated when a user installs the script

def get_server_health():
    return {
        "user_id": USER_ID,
        "hostname": socket.gethostname(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
    }

def send_data():
    data = get_server_health()
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print("Failed to send data:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)

if __name__ == "__main__":
    send_data()
