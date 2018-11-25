package main

import "fmt"

func main() {

	emptyMap := make(map[string]int)
	fmt.Println(emptyMap) //Prints: map[]

	emptyMap["some_index"] = 500
	fmt.Println(emptyMap) //Prints: map[some_index:500]

	anotherMap := map[int]string{
		1: "200",
		2: "300",
	}
	fmt.Println(anotherMap) //Prints: map[1:200 2:300]]

	delete(anotherMap, 1)
	fmt.Println(anotherMap) //Prints: map[2:300]]
}
