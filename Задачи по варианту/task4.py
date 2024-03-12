import random

def qSortgood(a):
	if len(a) <= 1:
		return a
	pivot = a[random.randint(0, len(a) - 1)]
	l = [x for x in a if x < pivot]
	r = [x for x in a if x > pivot]
	mid = [x for x in a if x == pivot]
	return qSortgood(l) + mid + qSortgood(r)

def binSearch(a, x):
    low, high = 0, len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))

a = qSortgood(a)
for x in b:
	print(binSearch(a, x), end = " ")
	
