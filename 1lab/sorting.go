package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	//unsortedList := []int{2, 0, 1, 3}

	unsortedList := createArray(100000)
	//fmt.Println(unsortedList)
	defer timer("Insertionsort")()
	insertionSort(unsortedList)
	//fmt.Println("Insertion sort: ", insertionSort(unsortedList))

	defer timer("Mergesort")()
	mergeSort(unsortedList)
	//fmt.Println("Merge sort: ", mergeSort(unsortedList))
	fmt.Println("##### Go end #####")
}

// https://stackoverflow.com/questions/45766572/is-there-an-efficient-way-to-calculate-execution-time-in-golang
func timer(name string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", name, time.Since(start))
	}
}

func createArray(arrayLength int) []int {
	var unsortedList []int
	for i := 0; i < arrayLength; i++ {
		unsortedList = append(unsortedList, i)
	}

	//https://yourbasic.org/golang/shuffle-slice-array/
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(unsortedList), func(i, j int) { unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i] })
	return unsortedList
}

func insertionSort(array []int) []int {
	for i := 1; i < len(array); i++ {
		j := i
		for j > 0 && array[j-1] > array[j] {
			array[j-1], array[j] = array[j], array[j-1]
			j--
		}
	}
	return array
}

func mergeSort(array []int) []int {
	if len(array) > 1 {

		middlePoint := len(array) / 2

		nArray1 := array[0:middlePoint]
		nArray2 := array[middlePoint:]

		nArray1 = mergeSort(nArray1)
		nArray2 = mergeSort(nArray2)

		output := []int{}
		output = merge(nArray1, nArray2)
		return output
	}

	return array
}

func merge(leftArray []int, rightArray []int) []int {
	output := []int{}
	i := 0
	j := 0
	for i < len(leftArray) && j < len(rightArray) {
		if leftArray[i] < rightArray[j] {
			output = append(output, leftArray[i])
			i++
		} else {
			output = append(output, rightArray[j])
			j++
		}
	}

	for ; i < len(leftArray); i++ {
		output = append(output, leftArray[i])
	}

	for ; j < len(rightArray); j++ {
		output = append(output, rightArray[j])
	}
	return output
}
