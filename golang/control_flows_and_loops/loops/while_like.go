package main

import "fmt"

func main() {

	//Emulating a while loop like - with break
	counter2 := 0
	j := 0
	for {
		if j > 99 {
			break
		}
		j++
		counter2++
	}

	fmt.Println(counter2) //Print 100

	//Emulating a do..while loop
	j = 0
	counter2 = 0

	anExpression := true
	for ok := true; ok; ok = anExpression {
		if j > 99 {
			anExpression = false
		}
		j++
		counter2++
	}

	//Here it will print 101 - because unlike the 'while' loop that had the break terminating the loop
	//immediately, in the do..while it will finish the current run and will be terminate in the start of next run becuase that the
	//the value of 'anExpression' is false
	fmt.Println(counter2)

}
