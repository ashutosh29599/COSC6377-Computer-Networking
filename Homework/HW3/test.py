import requests
import time
import csv

# 1. Setting parameters for the POST request
url = 'http://35.224.82.70:5555/delayme'
headers = {'Content-type': 'application/json'}
data = {"truncid": 71}

# csv field names
fields = ['Website', 'Time', 'Latency', 'Comment', 'Status Code']

# name of csv file (log file)
filename = "website_logs_h3.csv"

start_time = time.time()
# Time = time.time()
response = requests.post(url, data=data)
latency = (time.time() - start_time) * 1000
# print(f"Latency: {latency} ms")

print(response.json())

# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
#     # writing the fields
#     csvwriter.writerow(fields)
#     for i in range(10):
#         # 2. Sending the POST request
#         start_time = time.time()
#         # Time = time.time()
#         response = requests.post(url, headers=headers, data=data)
#         latency = (time.time() - start_time) * 1000
#         # print(f"Latency: {latency} ms")
#
#         print(response.json())

        # 3. Handling the response from the server
        # if response.status_code == requests.codes.ok:
        #     print('Request was successful')
        #     print(response.json())
        #     print(f"Latency: {latency} ms")
        #     csvwriter.writerows([[url, Time, latency, "Website is up", response]])
        # else:
        #     latency = (time.time() - start_time) * 1000
        #     print('Request failed with status code:', response.status_code)
        #     print(f"Latency: {latency} ms")
        #     csvwriter.writerows([[url, Time, latency, "Website is down", response]])

time.sleep(5)
