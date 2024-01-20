from random import shuffle
import matplotlib.pyplot as plt
import matplotlib as mpl
import time

def createArray(arrayLength : int) -> list[int]:
	unSortedList = list()
	for i in range(arrayLength):
		unSortedList.append(i)
	shuffle(unSortedList)
	return unSortedList


unSortedList = createArray(4)
print(unSortedList)

def insertionSort(array : list) -> list[int]:
	for _ in range(len(array)):
		j = _
		while j > 0 and array[j-1] > array[j]:
			array[j-1], array[j] = array[j], array[j-1]
			j -= 1
	return array

start = time.time()
unSortedList = createArray(8)
sortedList = insertionSort(unSortedList)
print(f'Insertionsort: {unSortedList}, %s seconds' % (time.time() - start))


counter = 0

def mergeSort(array : list) -> list[int] and int:
	global counter
	if len(array) > 1:
		middlePoint = int(len(array) / 2)

		nArray1 = array[0:middlePoint]
		nArray2 = array[middlePoint:]
		nArray1 = mergeSort(nArray1)
		nArray2 = mergeSort(nArray2)

		output = merge(nArray1, nArray2)
		counter += 6
		return output
	return array

def merge(leftArray : list[int], rightArray : list[int]) -> list[int]:
	global counter
	output = list()
	i = j = 0
	counter += 2
	while i < len(leftArray) and j < len(rightArray):

		if leftArray[i] < rightArray[j]:
			output.append(leftArray[i])
			i += 1
			counter += 2
		else:
			output.append(rightArray[j])
			j += 1
			counter += 2
	
	for _ in range(i, len(leftArray)):
		output.append(leftArray[_])
		counter += 1
	
	for _ in range(j, len(rightArray)):
		output.append(rightArray[_])
		counter += 1
	#print(f"merged into {output}")
	return output
	
	
unSortedList = createArray(8)
print(unSortedList)
start = time.time()
sortedList = mergeSort(unSortedList)
print(f'Mergesort: {unSortedList}, %s seconds' % (time.time() - start))
print(f'Counter is {counter}')


print(" ###### python end ####")