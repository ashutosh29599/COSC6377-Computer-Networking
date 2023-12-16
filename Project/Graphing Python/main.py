import matplotlib.pyplot as plt


# t2.xlarge Single
# N = [500, 1000, 2000, 4000, 8000, 10000, 12000, 15000, 18000, 20000, 24000, 32000, 36000, 40000, 45000]
# Gflops = [9.421, 19.160, 25.745, 29.994, 33.000, 33.863, 34.399, 34.814, 35.140, 35.327, 35.536, 35.294, 36.029, 36.171, 36.265]
# plt.plot(N, Gflops, label="Single", marker="s")
# plt.title("Single t2.xlarge instance")
# plt.xlim(0, 50000)
# plt.xticks(range(0, 50001, 5000))
# plt.ylim(0, 40)
# plt.yticks(range(0, 41, 5))

# t2.xlarge two in the same region
# N = [500, 1000, 2000, 4000, 8000, 10000, 12000, 15000, 18000, 20000, 24000, 32000, 36000, 40000, 45000]
# Gflops = [10.3595, 18.4545, 25.824, 29.857, 33.072, 33.666, 34.274, 34.7195, 35.394, 35.253, 35.604, 35.4465, 36.1545, 36.0705, 36.102]
# plt.plot(N, Gflops, label="Two instances (within the same region)", marker="*")
# plt.title("Two t2.xlarge Instances in the same region (US East (Ohio))")
# plt.xlim(0, 50000)
# plt.xticks(range(0, 50001, 5000))
# plt.ylim(0, 40)
# plt.yticks(range(0, 41, 5))


# t2.xlarge four in two regions
# N = [500, 1000, 2000, 4000, 8000, 10000, 12000, 15000, 18000, 20000, 24000, 32000, 36000, 40000, 45000]
# Gflops = [10.49325, 18.833, 26.0895, 30.08225, 32.82575, 32.72375, 34.10875, 34.56425, 34.8475, 35.0155, 35.28875, 35.868, 36.25575, 36.0325, 36.48675]
# plt.plot(N, Gflops, label="Four instances (across two regions)", marker="D")
# plt.title("Four t2.xlarge instances across two regions")
# plt.xlim(0, 50000)
# plt.xticks(range(0, 50001, 5000))
# plt.ylim(0, 40)
# plt.yticks(range(0, 41, 5))

###############

# t2.micro Single
N = [500, 1000, 2000, 4000, 8000, 9000, 9500]
Gflops = [10.796, 18.967, 26.373, 30.493, 33.541, 34.043, 34.112]
plt.plot(N, Gflops, label="Single", marker="s")
# plt.title("Single t2.micro instance")
# plt.xlim(0, 10000)
# plt.xticks(range(0, 10001, 1000))
# plt.ylim(0, 35)
# plt.yticks(range(0, 36, 5))


# t2.micro two in the same region
N = [500, 1000, 2000, 4000, 8000, 9000, 9500]
Gflops = [10.963, 19.4545, 26.03, 30.78, 33.4475, 33.932, 33.864]
plt.plot(N, Gflops, label="Two instances (within the same region)", marker="*")
# plt.title("Two t2.micro Instances in the same region (US East (Ohio))")
# plt.xlim(0, 1000)
# plt.xticks(range(0, 10001, 1000))
# plt.ylim(0, 35)
# plt.yticks(range(0, 36, 5))


# t2.micro four in two regions
N = [500, 1000, 2000, 4000, 8000, 9000]
Gflops = [9.790275, 19.6045, 25.626, 30.61825, 33.52525, 34.05225]
plt.plot(N, Gflops, label="Four instances (across two regions)", marker="D")
# plt.title("Four t2.micro instances across two regions")
# plt.xlim(0, 10000)
# plt.xticks(range(0, 10001, 1000))
# plt.ylim(0, 35)
# plt.yticks(range(0, 36, 5))


# plt.title("t2.xlarge Gflops Output")
# plt.xlim(0, 50000)
# plt.xticks(range(0, 50001, 5000))
# plt.ylim(0, 40)
# plt.yticks(range(0, 41, 5))

plt.title("t2.micro Gflops Output")
plt.xlim(0, 10000)
plt.xticks(range(0, 10001, 1000))
plt.ylim(0, 35)
plt.yticks(range(0, 36, 5))


plt.legend()

# plt.plot(N, Gflops, marker='o')
plt.xlabel("Problem size (N)")
plt.ylabel("Gflops")
# plt.savefig("graph_combined_t2xlarge.png")
plt.savefig("graph_combined_t2micro.png")
# plt.savefig("graph_t2xlarge_single.png")
# plt.savefig("graph_t2xlarge_two_same_region.png")
# plt.savefig("graph_t2xlarge_four_across_two_regions.png")
# plt.savefig("t2micro_single.png")
# plt.savefig("t2micro_two_same_region.png")
# plt.savefig("t2micro_four_across_two_regions.png")
plt.show()
