import math


def cal_D(a, b):
    return a*math.log(a/b) + (1 - a)*math.log((1 - a)/(1 - b))


def cal_term():
    pass


f = open("input.txt", "r")
n, m, p = f.read().split(" ")
N = int(n)
M = int(m)
P = float(p)

# N = 50
# M = 1000
# P = 0.95

N_total = M*N  # the total needed number of people

calculated_sum = 0.0
calculated_prob = 0.0
if M == 1:
    N_total = N
else:
    while calculated_prob <= P:
        N_total += 1  # I should increase N_total by binary search
        calculated_sum = sum([math.comb(N_total, i) * ((1 / M) ** i) * (1 - (1 / M)) ** (N_total - i) for i in range(N+1)])
        upper_bound = math.exp(-N_total * cal_D(N/N_total, (1/M)))
        lower_bound = (1/math.sqrt(8*N_total*(N/N_total)*(1-N/N_total)))*math.exp(-N_total * cal_D(N/N_total, (1/M)))
        # calculated_prob = 1 - (lower_bound + upper_bound)/2
        calculated_prob = 1 - calculated_sum
        calculated_prob = round(calculated_prob, 2)


print(N_total)
print(1/365435132134565454654)