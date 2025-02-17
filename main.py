import os
import psutil
import logging
import requests
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: str


@app.get("/integration.json")
def get_integration_jsonfile(request: Request):
    base_url = str(request.base_url).rstrip("/")
    integration_json = {
        "data": {
            "date": {"created_at": "2025-02-09", "updated_at": "2025-02-09"},
            "descriptions": {
                "app_name": "Ubuntu Server Monitoring",
                "app_description": "Monitors CPU, Memory, Disk Usage, and Uptime on an Ubuntu Server",
                "app_logo": "https://i.imgur.com/lZqvffp.png",
                "app_url": base_url,
                "background_color": "#000000"
            },
            "is_active": False,
            "integration_type": "interval",
            "category": "Monitoring",
            "author": "David Nduonofit",
            "website": base_url,
            "key_features": [
                "Monitor your server's CPU usage",
                "Monitor Memory Usage",
                "Monitor Disk Usage",
                "Monitor Uptime"
            ],
            "permissions": {
                "monitoring_user": {
                    "always_online": True,
                    "display_name": "Server Monitor"
                }
            },
            "settings": [
                {"label": "Server Details", "type": "text", "required": True, "default": ""},
                {"label": "Web Hook", "type": "text", "required": True, "default": ""},
                {"label": "Interval", "type": "text", "required": True, "default": "* * * * *"},
                {"label": "Max Data Upload Size (in KB)", "type": "number", "required": True, "default": 5}
            ],
            "target_url": "",
            "tick_url": f"{base_url}/health"
        }
    }
    return integration_json


@app.route('/')
async def home():
    return {"staus" : "success", "details" : {
        'description' : 'This is an integration, that runs on your server, sharing necessary resource information, to our centralized server, which updates your telex channel at proposed intervals',
        "installation_process" : "Run this command to get the monitoring agent installed on your server, 'curl -sSL https://your-server.com/install.sh | bash', after this, add the integration to your telex channel"


    }}

server_health_data = {}

@app.post('/health')
async def health_check(data: dict):
    """
    Receives health data from a user's server.
    """
    try:
        hostname = data.get("hostname", "Unknown")
        server_health_data[hostname] = data  # Store in memory (Use a DB in production)
        return {"status": "success", "message": f"Data received from {hostname}"}
    except Exception as e:
        logging.error(f"Error processing health data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


def run_server():
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    run_server()


# when a user visits a page, the user should sign up and then a key will be sent to them, that key is what will be requested, anytime a message is sent to the channel