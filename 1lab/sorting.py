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


def insertionSort(array : list) -> list[int]:
	for _ in range(len(array)):
		j = _
		while j > 0 and array[j-1] > array[j]:
			array[j-1], array[j] = array[j], array[j-1]
			j -= 1
	return array


def mergeSort(array : list) -> list[int] and int:
	if len(array) > 1:
		middlePoint = int(len(array) / 2)

		nArray1 = array[0:middlePoint]
		nArray2 = array[middlePoint:]
		nArray1 = mergeSort(nArray1)
		nArray2 = mergeSort(nArray2)

		output = merge(nArray1, nArray2)
		return output
	return array

def merge(leftArray : list[int], rightArray : list[int]) -> list[int]:
	output = list()
	i = j = 0
	while i < len(leftArray) and j < len(rightArray):

		if leftArray[i] < rightArray[j]:
			output.append(leftArray[i])
			i += 1

		else:
			output.append(rightArray[j])
			j += 1
	
	for _ in range(i, len(leftArray)):
		output.append(leftArray[_])
	
	for _ in range(j, len(rightArray)):
		output.append(rightArray[_])

	return output
	



if __name__ == "__main__":
	unSortedList = createArray(100000)

	start = time.time()
	sortedList = insertionSort(unSortedList)
	#print(f'Insertionsort: {unSortedList}, %s seconds' % (time.time() - start))
	print(f'Insertionsort: %s seconds' % (time.time() - start))
		
	start = time.time()
	sortedList = mergeSort(unSortedList)
	#print(f'Mergesort: {sortedList}, %s seconds' % (time.time() - start))
	print(f'Mergesort: %s seconds' % (time.time() - start))
	#print(f'Counter is {counter}')


	print("###### python end #####")