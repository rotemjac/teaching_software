package main

import (
	"fmt"
	"samplePackage"
)

func main() {

	//Basic syntax
	counter := 0
	for i := 0; i < 100; i++ {
		counter++
	}

	fmt.Println(counter) //Print 100
	samplePackage.SampleFunc()
}
