package main

import "fmt"

//This function intSeq returns another function, which we define anonymously in the body of intSeq. The returned function closes over the variable i to form a closure.
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// ----------------------------------- Example without closure ----------------------------------- //
	//Simple assignment of anonymous / inline function to a variable
	inlineFunc := func() string {
		return "Hello!"
	}

	fmt.Println(inlineFunc()) //Prints 1

	// ----------------------------------- Example with closure ----------------------------------- //

	//Assigning a function to nextInt - #1
	//This function value captures its own i value, which will be updated each time we call nextInt.
	nextInt := intSeq()

	fmt.Println(nextInt()) //Prints 1
	fmt.Println(nextInt()) //Prints 2
	fmt.Println(nextInt()) //Prints 3

	//Assigning a function to nextInt - #2
	//The variable of newInts will contain a new function that ha a new closure to the variable i , so the counting will be from the start
	newInts := intSeq()
	fmt.Println(newInts()) //Prints 1
	fmt.Println(newInts()) //Prints 2
}
