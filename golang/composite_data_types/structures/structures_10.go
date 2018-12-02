package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	//Example with json.Marshal
	type fruit2 struct {
		Weight int
		Price  int
		color  string
		color2 string
		num    int
	}

	//json.Marshal function returns two ([]byte and error)
	byt, err := json.Marshal(fruit2{1390, 101, "Blue",
		"Yellow", 999})

	//TODO: Explain the output here
	//TODO: Or take more examples like in here and move to a json section
	fmt.Println(byt)
	fmt.Println(err)
}
