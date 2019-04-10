package main

import (
	"fmt"
)

func main() {
	fmt.Println(namedParamsFunc1(3, 5)) //Prints 3 5
	fmt.Println(namedParamsFunc2(3, 5)) //Prints 3 5
}

//Not mentioned explicitly in the return - will be returned in the order they were passed as params
func namedParamsFunc1(num1, num2 int) (min, max int) {
	if num1 > num2 {
		min = num2
		max = num1
	} else {
		min = num1
		max = num2
	}
	return
}

//Mentioned explicitly in the return
func namedParamsFunc2(num1, num2 int) (min, max int) {
	if num1 > num2 {
		min = num2
		max = num1
	} else {
		min = num1
		max = num2
	}
	return min, max
}
