import time, tracemalloc

def is_majority_element(a, x, left, right):
	k = 0
	for y in a:
		if x == y:
			k += 1
	if k > len(a) // 2:
		return True
	else:
		return False


def find_majority_element(a):
	if len(a) == 0:
		return 0
	x = a[0]
	k = 1
	for i in range(1, len(a)):
		if a[i] == x:
			k += 1
		else:
			k -= 1
			if k == 0:
				x = a[i]
				k = 1
	if is_majority_element(a, x, 0, len(a) - 1):
		return 1
	else:
		return 0

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = list(map(int, f1.readline().split()))
f2.write(str(find_majority_element(a)))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
