package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	//In order to avoid : Go rand.Intn return the same value on each run : https://stackoverflow.com/questions/39529364/go-rand-intn-same-number-value
	rand.Seed(time.Now().UnixNano())

	//Give me a random number between 0 and 100
	number := rand.Intn(100)
	fmt.Println(number)

	//Switch example - Basic
	switch {
	case number < 50:
		fmt.Println("Less than 50!")
	case number > 0:
		fmt.Println("Bigger than 50!")
	default:
		fmt.Println("50!")
	}

	//Switch example - differentiate between types
	var someType error = nil
	switch someType.(type) {
	case nil:
		fmt.Println("It is nil interface!")

	default:
		fmt.Println("Not nil interface!")
	}
}
