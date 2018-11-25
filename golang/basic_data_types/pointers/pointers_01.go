package main

import "fmt"

func main() {

	a := 10
	b := 12
	fmt.Println(a)
	fmt.Println(b)

	address_a := &a
	address_b := &b
	fmt.Println(address_a)
	fmt.Println(address_b)

	getDoublePointer(address_a)
	fmt.Println(*address_a) //We add * (dereferencing the pointer) in order to take the value

	value := *(returnDoublePointer(b))
	fmt.Println(value) //A pointer is returned - we dereference the pointer
}

func getDoublePointer(a *int) {
	*a = *a * *a //a is already a pointer, in order to manipulate its value we add the * (dereferencing the pointer)
}
func returnDoublePointer(a int) *int {
	value := a * a
	return &value
}
