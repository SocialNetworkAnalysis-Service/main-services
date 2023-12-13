import json

import requests

from src.config_reader import config

headers = {
    "Content-Type": 'application/json; charset="utf-8"',
}


async def send_call_verify(phone_number: str):
    data = {
        "login": config.sms_agent_login,
        "pass": config.sms_agent_password,
        "type": "flashcall",
        "payload": [{"phone": phone_number}],
    }
    response = requests.post(
        config.sms_agent_api_url, headers=headers, data=json.dumps(data)
    )
    response_data = response.json()[0]
    if "error" in response_data.keys():
        return False
    return response_data["code"]