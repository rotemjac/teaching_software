package main

import "fmt"

func main() {

	//We'll se 2 examples of A tuple assignment (in go terminology)
	//Notice: we use "_" to ignore an item

	//1. From a function that returns a tuple
	num1, num2, num3, _, str := getFourItems(10)
	fmt.Println(num1, num2, num3, str)

	//2.From an inline values
	val1, val2, val3 := num1+2, num1+200, num1+2000
	fmt.Println(val1, val2, val3)
}

//Here we return a tuple of 5 items from the different types
func getFourItems(num int) (int, int, float64, string, string) {
	return num + 1, num + 2, 0.2, "This string wil be ignored outside", "Some string"
}
