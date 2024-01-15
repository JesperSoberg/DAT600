package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	//unsortedList := []int{2, 0, 1, 3}

	unsortedList := createArray(8)

	fmt.Println(unsortedList)

	defer timer("main")()
	fmt.Println("Insertion sort: ", insertionSort(unsortedList))
	time.Sleep(time.Second * 2)
	//fmt.Println("Final", mergeSort(unsortedList))

}

// https://stackoverflow.com/questions/45766572/is-there-an-efficient-way-to-calculate-execution-time-in-golang
func timer(name string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s too %v\n", name, time.Since(start))
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
	fmt.Println(array)
	return array
}

func mergeSort(array []int) []int {
	if len(array) > 1 {

		middlePoint := len(array) / 2

		nArray1 := array[0:middlePoint]
		nArray2 := array[middlePoint:]
		fmt.Println(nArray1)
		fmt.Println(nArray2)
		nArray1 = mergeSort(nArray1)
		nArray2 = mergeSort(nArray2)
		//merge(nArray1, nArray2)
		output := []int{}
		output = merge(nArray1, nArray2)
		return output
	}

	return array
}

func merge(leftArray []int, rightArray []int) []int {
	output := []int{}
	fmt.Println("merge")
	fmt.Println(leftArray)
	fmt.Println(rightArray)
	i := 0
	j := 0
	for i < len(leftArray) && j < len(rightArray) {
		fmt.Println("Comparing", leftArray[i], "and", rightArray[j])
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
	fmt.Println("Merged into", output)
	return output
	//fmt.Println("Final", output)
}
