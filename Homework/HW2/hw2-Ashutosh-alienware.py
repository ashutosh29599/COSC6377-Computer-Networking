import json
import requests
import time
import smtplib
from email.mime.text import MIMEText


with open("config.json") as file:
    data = json.load(file)
    # print(data['data'][0])

    website = data['data'][0]['website']
    poll_interval = data['data'][0]['poll-interval']    # in seconds

    while True:
        start_time = time.time()
        response = requests.get(website)
        end_time = time.time()

        if response.status_code != 200:
            try:
                # https://stackoverflow.com/questions/67951635/how-to-send-email-alert-through-python-if-a-string-is-found-in-a-csv-file
                # https://support.google.com/accounts/answer/185833?visit_id=637972587783521250-175398277&p=InvalidSecondFactor&rd=1
                message = MIMEText("Body of the email!")
                message["From"] = "akumar29cs@gmail.com"
                message["To"] = "akumar29cs@gmail.com"

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("akumar29cs@gmail.com", "rvcp zwpc awun kriu")
                server.send_message(message)
                server.quit()

            except Exception as e:
                print(f"Error = {e}")

        print(response.status_code)
        print(f"Latency = {(end_time - start_time) * 1000}ms")
        print("_______________________________________________")

        time.sleep(poll_interval)
        