package main

import "fmt"

func main() {

	//Creating a new slice literal - notice that in slices we do not specify the size
	originalSlice := make([]int, 5)
	newSlice := originalSlice[1:3]
	fmt.Println(originalSlice)
	fmt.Println(newSlice)

	//This will affect the items from originalSlice
	newSlice[0] = -200
	newSlice[1] = -300
	fmt.Println(originalSlice)
	fmt.Println(newSlice)

	//Creating a new slice which points to the other slice address
	anotherNewSlice := newSlice[:]
	anotherNewSlice[0] = -400    //Of course this will also affect the original slices
	fmt.Println(originalSlice)   //You will see the change also in here
	fmt.Println(newSlice)        //And also in here
	fmt.Println(anotherNewSlice) //In here - of course
}
