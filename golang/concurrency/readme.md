Go offers its own unique and innovative way of achieving concurrency, which comes in theform of goroutines and channels.

Goroutines are the smallest Go entities that can be executed on their own in a Go program, while channels can get data from goroutines in a concurrent and efficient way and thus allow goroutines to have a point of reference and
communicate with each other.

Everything in Go is executed using goroutines; this makes perfect sense since Go is a concurrent programming language by design.
Therefore, when a Go program starts its execution, its single goroutine calls the main() function, which starts the actual program execution.