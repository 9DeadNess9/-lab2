import time, tracemalloc

def merge(a, left, mid, right):
	n1 = mid - left + 1
	n2 = right - mid
	L = [0] * n1
	R = [0] * n2
	for i in range(n1):
		L[i] = a[left + i]
	for j in range(n2):
		R[j] = a[mid + 1 + j]
	i = 0
	j = 0
	k = left
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			a[k] = L[i]
			i += 1
		else:
			a[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		a[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		a[k] = R[j]
		j += 1
		k += 1

def mergeSort(a, left, right):
	if left < right:
		mid = (left + right) // 2
		mergeSort(a, left, mid)
		mergeSort(a, mid + 1, right)
		f2.write(str(left + 1) + " " + str(right + 1) + " " + str(a[left]) + " " + str(a[right]) + "\n")
		merge(a, left, mid, right)
		return a

def checkSorted(a):
	for i in range(1, len(a)):
		if a[i] < a[i - 1]:
			return False
	return True

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = list(map(int, f1.readline().split()))
for x in mergeSort(a, 0, len(a) - 1):
	f2.write(str(x) + " ")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
print(checkSorted(a))
