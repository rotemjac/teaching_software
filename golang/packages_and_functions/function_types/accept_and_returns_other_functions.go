package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	//Functions that accept other functions as parameters
	res1 := funcThatAcceptFuncAsParam(someFunc1, "Some string")
	res2 := funcThatAcceptFuncAsParam(someFunc2, "Some string")

	fmt.Println(res1) //Prints 111
	fmt.Println(res2) //Prints 211

	//Functions that return other functions
	//See closures example
}

func someFunc1(num int) int {
	return num + 100
}
func someFunc2(num int) int {
	return num + 200
}

func funcThatAcceptFuncAsParam(funAsParam func(int) int, str string) int {
	//Get string length
	numberOfChars := utf8.RuneCountInString(str)

	//
	numberFromOuterFunc := funAsParam(numberOfChars)
	return numberFromOuterFunc
}
