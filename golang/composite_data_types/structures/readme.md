

Structures

1. In Gos world we use mostly structs for encapsulation of typed fields - like classes in java.

2. Structures (and sometimes types) in Go are usually defined
   outside the main() function.
   This is in order to have a global scope and be available to the entire Go package, unless you want to clarify that a type is
   only useful within the current scope and is not expected to be used
   elsewhere.

3. The fields of a structure usually begin with an uppercase letter.
