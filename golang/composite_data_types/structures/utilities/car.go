package utilities

import "fmt"

type Car struct {
	id             int
	ProductionYear int
	DoorNum        int
	Color          string
}

func (c Car) PrintInfo() {
	fmt.Printf("This car was created in %d with %d doors and with color of: %s ", c.ProductionYear, c.DoorNum, c.Color)
}
