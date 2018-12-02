package samplePackage

import "fmt"

//Lower case - private
func somePrivateFunc() string {
	return "Try to reach me from outside!"
}

//Upper case - public
func SampleFunc() string {
	fmt.Println("Hi")
	return "Some String"
}
