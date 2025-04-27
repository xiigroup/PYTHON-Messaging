# PYTHON-Messaging
Send and Receive Whatsapp and SMS messages from any PYTHON enabled system.

## Sample PYTHON Usage
This sample PYTHON code send an sms message and returns the response in json. to send a whatsapp message replace sms with **whatsapp**.
Replace **DOMAIN** , **API_USERNAME** & **API_KEY** with your API user Information.

```
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

For all api payloads definitions [Check wiki](https://github.com/xiigroup/PHP-Messaging/wiki), to request your credentials [Contact sales](https://xiigroup.co.za/#contact)
