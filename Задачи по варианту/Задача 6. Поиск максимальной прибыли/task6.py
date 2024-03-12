import time, tracemalloc

def find_max_crossing_subarray(a, low, mid, high):
	leftsum = float('-inf')
	s = 0
	maxleft = 0
	for i in range(mid, low - 1, -1):
		s += a[i]
		if s > leftsum:
			leftsum = s
			maxleft = i
	rightsum = float('-inf')
	s = 0
	maxright = 0
	for i in range(mid + 1, high + 1):
		s += a[i]
		if s > rightsum:
			rightsum = s
			maxright = i
	return maxleft, maxright, leftsum + rightsum

def find_maximum_subarray(a, low, high):
	if high == low:
		return low, high, a[low]
	else:
		mid = (low + high) // 2
		left_low, left_high, left_sum = find_maximum_subarray(a, low, mid)
		right_low, right_high, right_sum = find_maximum_subarray(a, mid + 1, high)
		cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
		if left_sum >= right_sum and left_sum >= cross_sum:
			return left_low, left_high, left_sum
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = f1.readline()
dates = []
prices = []
diffs = [0]
while n != "\n":
	date, price = n.split()
	dates.append(date)
	prices.append(float(price))
	n = f1.readline()
for i in range(1, len(prices)):
	diffs.append(prices[i] - prices[i-1])
zakupaem, prodaem, profit = find_maximum_subarray(diffs, 0, len(diffs) - 1)
s = "SBERBANK: " + str(dates[0]) +  "-" +  str(dates[-1]) + " buy: " +  str(dates[zakupaem - 1]) + " sell: " + str(dates[prodaem]) + " profit: " + str(profit)
f2.write(s)
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
