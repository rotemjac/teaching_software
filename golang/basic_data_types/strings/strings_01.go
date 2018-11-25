package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "SOME STRING"

	lower := strings.ToLower(str)

	fmt.Println(lower)

	//Split a string
	sentence := "Sometimes I lay under the moon and thanks god i'm breathing"

	words := strings.Split(sentence, " ")

	fmt.Printf("%v \n", words)

	//Better form (the docs said)
	fields := strings.Fields(sentence)
	fmt.Printf("%v \n", fields)
}
