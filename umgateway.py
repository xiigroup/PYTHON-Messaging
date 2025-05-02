import logging
import json
import requests
from requests.auth import HTTPBasicAuth
logger = logging.getLogger(__name__)

def send_message(username, password, data):
  try:
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    auth = HTTPBasicAuth(username, password)
    response = requests.post("https://api.xiigroup.co.za/", data=data, headers=headers, auth=auth)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    logger.exception(f"E: {response}")
    return response.json()  # Parse the JSON response
  except requests.exceptions.RequestException as e:
    logger.exception(f"Error sending message: {e}")
    return None
  except json.JSONDecodeError as e:
    logger.exception(f"Error decoding JSON response: {e}")
    return None
