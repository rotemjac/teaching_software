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

	//If example
	if number < 50 {
		fmt.Println("Small")
	} else {
		fmt.Println("Big")
	}

}
