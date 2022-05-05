import math
import numpy
import sys
import time
import matplotlib.pyplot as plt


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.insert(i, A[p + i])
    for j in range(0, n2):
        R.insert(j, A[q + j + 1])
    i = 0
    j = 0
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


nValues = 10
values_array = []
for i in range(1, 9):
    values_array.append(numpy.random.randint(0, sys.maxsize, nValues))
    nValues *= 10

insertionSortRandomTimes = []
insertionSortBestTimes = []
insertionSortWorstTimes = []
mergeSortRandomTimes = []
# mergeSortBestTimes = []
# mergeSortWorstTimes = []

nRuns = 4
nValues = 10
maxTime = 120
run = 0
executionTime = 0
for i in range(0, nRuns):
    values = []
    if executionTime < maxTime:
        print("Insertion Random Run", i + 1, "nValues: ", nValues)
        # values = numpy.random.randint(1, 100000, nValues)
        values = values_array[run]
        # print(values)
        startTime = time.time()
        insertion_sort(values)
        endTime = time.time()
        executionTime = endTime - startTime
        insertionSortRandomTimes.append(executionTime)
        nValues *= 10
        run += 1

print("INSERTION RANDOM TIMES:", insertionSortRandomTimes)
print("---------------------------------------------------------------------------------------")

nValues = 10
executionTime = 0
for i in range(0, nRuns):
    values = []
    if nValues > 1000000000:
        break
    if executionTime < maxTime:
        print("Insertion Best Run", i + 1, "nValues: ", nValues)
        for j in range(0, nValues):
            values.append(j)
        print(values)
        startTime = time.time()
        insertion_sort(values)
        endTime = time.time()
        executionTime = endTime - startTime
        insertionSortBestTimes.append(executionTime)
        nValues *= 10
print("INSERTION BEST TIMES:", insertionSortBestTimes)
print("---------------------------------------------------------------------------------------")

nValues = 10
executionTime = 0
for i in range(0, nRuns):
    values = []
    if executionTime < maxTime:
        print("Insertion Worst Run", i + 1, "nValues: ", nValues)
        for j in range(0, nValues):
            values.append(nValues - j)
        # print(values)
        startTime = time.time()
        insertion_sort(values)
        endTime = time.time()
        executionTime = endTime - startTime
        insertionSortWorstTimes.append(executionTime)
        nValues *= 10
print("INSERTION WORST TIMES:", insertionSortWorstTimes)
print("---------------------------------------------------------------------------------------")

nValues = 10
executionTime = 0
run = 0
for i in range(0, nRuns):
    if executionTime < maxTime:
        print("Merge Random Run", i + 1, "nValues: ", nValues)
        # values = numpy.random.randint(1, 100000, nValues)
        values = values_array[run]
        # print(values)
        startTime = time.time()
        merge_sort(values, 0, len(values) - 1)
        endTime = time.time()
        executionTime = endTime - startTime
        mergeSortRandomTimes.append(executionTime)
        nValues *= 10
        run += 1

print("MERGE RANDOM TIMES:", mergeSortRandomTimes)
print("---------------------------------------------------------------------------------------")

"""
nValues = 10
executionTime = 0
run = 0
for i in range(0, nRuns):
    values = []
    if nValues > 1000000000:
        break
    if executionTime < maxTime:
        print("Merge Best Run", i + 1, "nValues: ", nValues)
        for j in range(0, nValues):
            values.append(j)
        # print(values)
        startTime = time.time()
        merge_sort(values, 0, len(values) - 1)
        endTime = time.time()
        executionTime = endTime - startTime
        mergeSortBestTimes.append(executionTime)
        nValues *= 10
        run += 1

print("MERGE BEST TIMES:", mergeSortBestTimes)
print("---------------------------------------------------------------------------------------")

nValues = 10
executionTime = 0
run = 0
for i in range(0, nRuns):
    values = []
    if executionTime < maxTime:
        print("Merge Worst Run", i + 1, "nValues: ", nValues)
        for j in range(0, nValues):
            values.append(nValues - j)
        # print(values)
        startTime = time.time()
        merge_sort(values, 0, len(values) - 1)
        endTime = time.time()
        executionTime = endTime - startTime
        mergeSortWorstTimes.append(executionTime)
        nValues *= 10
        run += 1

print("MERGE WORST TIMES:", mergeSortWorstTimes)
print("---------------------------------------------------------------------------------------")
"""

plt.xscale("log")
plt.yscale("log")
plt.ylim(0.0000001, 1000)
x = []
for i in range(1, len(insertionSortRandomTimes)+1):
    x.append(10**i)
plt.plot(x, insertionSortRandomTimes, 'o-')
x = []
for i in range(1, len(insertionSortBestTimes)+1):
    x.append(10**i)
plt.plot(x, insertionSortBestTimes, 'o-')
x = []
for i in range(1, len(insertionSortWorstTimes)+1):
    x.append(10**i)
plt.plot(x, insertionSortWorstTimes, 'o-')
plt.title("Ordinamento per Insertion Sort")
plt.xlabel("Numero elementi")
plt.ylabel("Tempo (s)")
plt.legend(["Caso medio (random)", "Caso migliore", "Caso Peggiore"])
plt.show()

plt.xscale("log")
plt.yscale("log")
plt.ylim(0.0000001, 1000)
x = []
for i in range(1, len(mergeSortRandomTimes)+1):
    x.append(10**i)
plt.plot(x, mergeSortRandomTimes, 'o-')
"""
x = []
for i in range(1, len(mergeSortBestTimes)+1):
    x.append(10**i)
plt.plot(x, mergeSortBestTimes, 'o-')
x = []
for i in range(1, len(mergeSortWorstTimes)+1):
    x.append(10**i)
plt.plot(x, mergeSortWorstTimes, 'o-')
"""
plt.title("Ordinamento per Merge Sort")
plt.xlabel("Numero elementi")
plt.ylabel("Tempo (s)")
# plt.legend(["Caso medio (random)", "Caso migliore", "Caso Peggiore"])
plt.legend(["Caso medio (random)"])
plt.show()

# CONFRONTI

plt.xscale("log")
plt.yscale("log")
plt.ylim(0.0000001, 1000)
x = []
for i in range(1, len(insertionSortRandomTimes)+1):
    x.append(10**i)
plt.plot(x, insertionSortRandomTimes, 'o-')
x = []
for i in range(1, len(mergeSortRandomTimes)+1):
    x.append(10**i)
plt.plot(x, mergeSortRandomTimes, 'o-')
plt.title("Confronto caso medio tra InsertionSort e MergeSort")
plt.xlabel("Numero elementi")
plt.ylabel("Tempo (s)")
plt.legend(["InsertionSort", "MergeSort"])
plt.show()

plt.xscale("log")
plt.yscale("log")
plt.ylim(0.0000001, 1000)
x = []
for i in range(1, len(insertionSortBestTimes)+1):
    x.append(10**i)
plt.plot(x, insertionSortBestTimes, 'o-')
x = []
for i in range(1, len(mergeSortRandomTimes)+1):
    x.append(10**i)
plt.plot(x, mergeSortRandomTimes, 'o-')
plt.title("Confronto caso migliore tra InsertionSort e MergeSort")
plt.xlabel("Numero elementi")
plt.ylabel("Tempo (s)")
plt.legend(["InsertionSort", "MergeSort"])
plt.show()

plt.xscale("log")
plt.yscale("log")
plt.ylim(0.0000001, 1000)
x = []
for i in range(1, len(insertionSortWorstTimes)+1):
    x.append(10**i)
plt.plot(x, insertionSortWorstTimes, 'o-')
x = []
for i in range(1, len(mergeSortRandomTimes)+1):
    x.append(10**i)
plt.plot(x, mergeSortRandomTimes, 'o-')
plt.title("Confronto caso peggiore tra InsertionSort e MergeSort")
plt.xlabel("Numero elementi")
plt.ylabel("Tempo (s)")
plt.legend(["InsertionSort", "MergeSort"])
plt.show()
