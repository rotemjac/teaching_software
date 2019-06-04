#!/bin/bash


var1="Hello"
var2="World"
name="Foo bar"

#Assign the build in command 'whoami' to a variable
user=$(whoami)

#You refer variables with $
echo "The string is: $name $var1  $var2"

#$otherVar is not defined - but there won't be any error, just an ignore
echo "The string is: $name $otherVar  $var2"


echo "Are you $name of $user?"

#Using a internal variable (is defined as part of your shell).
echo "Current bash version is: $BASH_VERSION"