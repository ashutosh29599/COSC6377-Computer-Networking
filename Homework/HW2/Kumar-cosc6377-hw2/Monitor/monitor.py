import csv
import json
import requests
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt


def monitor():
    with open("config.json") as file:
        data = json.load(file)

        website = data['data'][0]['website']
        poll_interval = data['data'][0]['poll-interval']    # in seconds
        email = data['data'][0]['alert']

        poll_time = 0

        with open("log.csv", "a", newline="") as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(["timestamp", "website", "status_code", "latency", "poll_time"])

        while True:
            start_time = time.time()
            response = requests.get(website)
            end_time = time.time()

            if response.status_code != 200:
                try:
                    # https://stackoverflow.com/questions/67951635/how-to-send-email-alert-through-python-if-a-string-is-found-in-a-csv-file
                    # https://support.google.com/accounts/answer/185833?visit_id=637972587783521250-175398277&p=InvalidSecondFactor&rd=1
                    message = MIMEText(f"Hello!\n\nThe website {website} is down. Status code: {response.status_code}.")
                    message['Subject'] = f"Website {website} down!"
                    message["From"] = "akumar29cs@gmail.com"
                    message["To"] = email

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login("akumar29cs@gmail.com", "rvcp zwpc awun kriu")
                    server.send_message(message)
                    server.quit()

                except Exception as e:
                    print(f"Error = {e}")

            if response.status_code == 200:
                print(f"Website {website} UP.")
            else:
                print(f"Website {website} DOWN.")

            latency = round((end_time - start_time) * 1000, 3)

            print(f"Status code: {response.status_code}")
            print(f"Latency = {latency}ms")
            print("____________________")

            with open("log.csv", "a", newline="") as output_file:
                csv_writer = csv.writer(output_file)
                csv_writer.writerow([datetime.now(), website, response.status_code, latency, poll_time])

            poll_time += poll_interval
            time.sleep(poll_interval)


def create_graph(log_filename):
    time_intervals = []
    data = []

    with open(f"{log_filename}.csv", "r") as file:
        csv_reader = csv.reader(file)
        poll_interval = 0

        for row in csv_reader:
            if row[0] != "timestamp":
                time_intervals.append(poll_interval)
                data.append(float(row[-2]))

                poll_interval += int(row[-1])

    plt.plot(time_intervals, data)

    # plt.xlim(0, 500)
    # plt.xticks(range(0, 501, 50))
    # plt.ylim(0, 600)
    # plt.yticks(range(0, 601, 100))

    plt.title("Latency")
    plt.xlabel("Time (in seconds)")
    plt.ylabel("Latency (in ms)")

    plt.savefig(f"{log_filename}.png")
    plt.show()


if __name__ == "__main__":
    monitor()

    # create_graph("log")
