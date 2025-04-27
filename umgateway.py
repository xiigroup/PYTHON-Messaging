import logging
import json
import requests
from requests.auth import HTTPBasicAuth
logger = logging.getLogger(__name__)

def send_whatsapp_message(endpoint, number_id, username, message):
  """
  Sends a message to a simple messaging server.

  Args:
    username: The username of the sender.
    message: The message to send.

  Returns:
    The server's response (as a dictionary), or None if an error occurred.
  """
  try:
    data = {
        "endpoint": endpoint,
        "action": "send",
        "nid": number_id,
        "to": username[1:],
        "body": message,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    auth = HTTPBasicAuth("3", "857358244")
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

def send_whatsapp_button(endpoint, number_id, username, message):
  """
  Sends a message to a simple messaging server.

  Args:
    username: The username of the sender.
    message: The message to send.

  Returns:
    The server's response (as a dictionary), or None if an error occurred.
  """
  try:
    data = {
        "endpoint": endpoint,
        "action": "send",
        "type": "button",
        "button[1]": "Mark as complete",
        "nid": number_id,
        "to": username[1:],
        "body": message,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    auth = HTTPBasicAuth("3", "857358244")
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
