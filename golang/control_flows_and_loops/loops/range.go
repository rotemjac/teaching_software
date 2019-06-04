package main

import "fmt"

func main() {

	//An example of range loop
	arr := [10]int{0, 10, 21, 32, 34, 54, 67, 89}

	for i, value := range arr {
		//Look that we allocated 10 spaces and init only 8 items, so the other 2 will have the value of 0
		fmt.Println("Value of index: ", i, " is: ", value)
	}

}
