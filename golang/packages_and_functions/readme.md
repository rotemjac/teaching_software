
Packages and functions


Everything in Go comes in packages.

A package in Go is a .go file (a source file) that contains the work "package" in the beginning and the the package name.
Some packages have only one source file and some have multiple subdirectories.

The source code of a Go package, which can contain multiple files and multiple directories, can be found within a single directory that is named after the package name with the exception the main package.

We use Packages in order group functions, variables, and constants that share some common context
so that they could be used easily in Go programs.

Beside the main package, Go packages are not "stand alone" programs - you can't compile them into executable files.
This means that they need to be called directly or indirectly from a main package in order to be used.

The main function is used in every independent Go program.



Encapsulation

In Go, using capital letter for any package object (type, variable or function) will make it exported automatically.
Go does not have any other notation to control package member access like Java has for classes with public/private/protected. It’s all down to the case of the first letter in Go.



Functions

We have many types of functions in GO:

1. Functions that return multiple values (see in tuples topic). Those values can also be named.
2. Anonymous (Inline) functions
3. Functions with pointer parameters , Functions that return pointers
4. Functions that accept other functions , Functions that return other functions