import statistics
import time
import requests
import matplotlib.pyplot as plt


def monitor(truncid):
    payload = {"truncid": truncid}

    latencies_with_delay = []
    latencies_without_delay = []

    for i in range(100):
        print(f"{i}->")

        # without delay
        start_time = time.time()
        response = requests.post("http://35.224.82.70:5555/donotdelayme", data=payload)
        end_time = time.time()
        latency_1 = (end_time - start_time) * 1000

        print(f"Response for donotdelayme: {response.json()}")
        print(f"Latency without delay = {latency_1}ms")

        time.sleep(1)

        # with delay
        start_time = time.time()
        response = requests.post("http://35.224.82.70:5555/delayme", data=payload)
        end_time = time.time()
        latency_2 = (end_time - start_time) * 1000

        print(f"Response for delayme: {response.json()}")
        print(f"Latency with delay = {latency_2}ms")

        if (latency_1 > 200) or (latency_2 > 200):
            continue
        latencies_without_delay.append(latency_1)
        latencies_with_delay.append(latency_2)

        print("---------------------------")
        time.sleep(1)

    print(f"Latencies without delay: {latencies_without_delay}")
    print(f"Latencies with delay: {latencies_with_delay}")
    print()
    print(f"Avg latency without delay: {statistics.mean(latencies_without_delay)}")
    print(f"Avg latency with delay: {statistics.mean(latencies_with_delay)}")

    plt.figure(truncid)
    plt.plot(latencies_with_delay, label="With delay")
    plt.plot(latencies_without_delay, label="Without delay")

    # plt.yticks(range(0, 200, 20))

    plt.legend()
    plt.title(f"Latencies for truncid {truncid}")
    plt.ylabel("Latencies in ms")
    plt.savefig(f"Graphs/{truncid}_latencies3.png")
    # print()


if __name__ == "__main__":
    monitor(93)
