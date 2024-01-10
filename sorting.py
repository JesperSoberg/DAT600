from random import shuffle
import matplotlib.pyplot as plt
import matplotlib as mpl

def createArray(arrayLength : int) -> list[int]:
	unSortedList = list()
	for i in range(arrayLength):
		unSortedList.append(i)
	shuffle(unSortedList)
	return unSortedList


unSortedList = createArray(4)
#print(unSortedList)

def insertionSort(array : list) -> list[int]:
	for _ in range(len(array)):
		j = _
		while j > 0 and array[j-1] > array[j]:
			array[j-1], array[j] = array[j], array[j-1]
			j -= 1
	print(f"Sorted:  {array}")
	return array

#unSortedList = createArray(8)
#sortedList = insertionSort(unSortedList)


def mergeSort(array : list) -> list[int] and int:
	steps = 0
	if len(array) > 1:
		middlePoint = int(len(array) / 2)

		nArray1 = array[0:middlePoint]
		nArray2 = array[middlePoint:]
		nArray1, steps = mergeSort(nArray1)
		nArray2, steps = mergeSort(nArray2)

		output = merge(nArray1, nArray2)
		steps += 6 + steps
		return (output, steps)
	return (array, steps)

def merge(leftArray : list[int], rightArray : list[int]) -> list[int] and int:
	steps = 0
	output = list()
	i = j = 0
	steps += 2
	while i < len(leftArray) and j < len(rightArray):

		if leftArray[i] < rightArray[j]:
			output.append(leftArray[i])
			i += 1
			steps += 2
		else:
			output.append(rightArray[j])
			j += 1
			steps += 2
	
	for _ in range(i, len(leftArray)):
		output.append(leftArray[_])
		steps += 1
	
	for _ in range(j, len(rightArray)):
		output.append(rightArray[_])
		steps += 1
	#print(f"merged into {output}")
	return output#, steps
	
#unSortedList = createArray(8)
#print(unSortedList)
#sortedList = mergeSort(unSortedList)
#print(sortedList[0], sortedList[1])