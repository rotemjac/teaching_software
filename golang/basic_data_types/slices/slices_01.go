package main

import "fmt"

func main() {

	//Creating a new slice literal - notice that in slices we do not specify the size
	someSlice := []int{1, 2, 4, 6, 9, 12}
	fmt.Println(someSlice)

	//Adding an item to the slice
	someSlice = append(someSlice, 100000)
	fmt.Println(someSlice)

	//Printing first and last values
	fmt.Println(someSlice[0])
	fmt.Println(someSlice[len(someSlice)-1])

	//Creating empty slice using 'make'
	newSlice := make([]int, 20)

	//Print the values of 3-13 items (yes it doesn't include the last value)
	//Notice that the make functions initialize all items with 0
	fmt.Println(newSlice[3:14])

	//Make a slice empty
	newSlice = nil
	//Will cause an error: "panic: runtime error: slice bounds out of range"
	//fmt.Println(newSlice[3:14])//
}
