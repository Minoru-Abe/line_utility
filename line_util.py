import requests
LINECODE = "\n"

class SendNotification:
    def send_message(message, access_token):
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + access_token}
        payload = {"message": message}
        r = requests.post(url, headers=headers, params=payload,)
