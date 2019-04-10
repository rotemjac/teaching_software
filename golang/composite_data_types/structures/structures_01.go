package main

import (
	"fmt"
)

func main() {

	//Basic example
	type fruit struct {
		weight int
		price  int
		color  string
	}

	a := fruit{1200, 99, "Green"}
	fmt.Println(a)
}
