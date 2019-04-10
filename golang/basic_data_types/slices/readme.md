

Use slices instead of arrays in Go for most cases.

Only if you sure you do not want to change a fixed data set of items - use arrays.

Slices are being passed by reference to functions (means the memory address is passed).
If we have a big data set and we want to pass it to a function, using a slices will be much faster because you just pass a reference (the memory address of the slice variable) and not the all data set.


Creating a slice literal - Just like an array , BUT we do not specify the size


//Re-slicing
1. Writing someSlice[3:14] will start taking items from the third item until the 13 item (the right value - 14 - is NOT included)
2. When creating a sub slice from an existing slice it the items are referring to the original addresses in memory!
   So when manipulating the sub slice values - it will be reflected in the original slice.
   Take it into consideration in your code - if you'll take a big big file and dump into a slice an create a sub slice out of it - the big slice will exist in memory



TODO:
1. Add section on 'copy'.
2. Add section on 'Multidimensional slices'.
3. Add section on 'sort slice'.
4. Add section on 'byte slices'?