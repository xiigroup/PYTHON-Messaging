# Unified Messaging - Python
Send and Receive Whatsapp and SMS messages from any PYTHON server.

## Sample PYTHON Usage
This sample PYTHON code send an sms message and returns the response in json. to send a whatsapp message replace sms with **whatsapp**.
Replace sms with whatsapp. Replace **DOMAIN** , **API_USERNAME** & **API_KEY** with your API user Information.

```
umgateway import send_message

payload = {
  "endpoint": "sms",
  "action": "send",
  "type": "text",
  "nid": "24",
  "to": "2701234567",
  "name": "Sipho Selabe",
  "body": "Dear client..",
}

send_message("DOMAIN", "API_USERNAME", "API_KEY", payload)
```

## Sample json response
The following response you receive after send a message using the above sample, please save the **id** and **transaction_id** for later quering important is the message cannot be sent instant.

```json
{
  "status": "success",
  "results_count": 8,
  "results": {
    "id": "20994c0b-abce-4949-0104-04200000a61d",
    "status_code": 1,
    "status_msg": "Received",
    "parts": 1,
    "tid": "78Pe7RuIGXElgLE.5154",
    "cost": 0.28
  }
}
```

For all api payloads definitions [Check wiki](https://github.com/xiigroup/PYTHON-Messaging/wiki), to request your credentials [Contact sales](https://xiigroup.co.za/#contact)
