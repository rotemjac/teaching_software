package main

import (
	"fmt"
)

//Part 1 - Function that accept pointer
func funcThatAcceptPointer(num *int) int {
	return *num + 100
}

//Part 2 - Function that return pointers
//It is considered a good practice to create new structure
// variables using a separate function and return a pointer to them from that function.
// So, the scenario of functions returning pointers is very common.
// Generally speaking, such a function simplifies the structure of a program and allows the developer to concentrate on
// more important things instead of copying the same Go code all the time.
func funcThatReturnsPointer(num int) *int {
	otherNum := num + 100
	return &otherNum
}

func main() {
	someNum := 10

	//Part 1
	result := funcThatAcceptPointer(&someNum) //You need to pass the ADDRESS of the variable

	//Will cause a compilation error - Cannot use '10' (type untyped int) as type *int
	//result2 := funcThatAcceptPointer(10)

	fmt.Println(result)

	//Part 2
	resultAddress := funcThatReturnsPointer(someNum)
	fmt.Println(*resultAddress) //We need to take the address
}
