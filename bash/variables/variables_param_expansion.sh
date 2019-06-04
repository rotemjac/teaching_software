#!/bin/bash

fileNameToCreate="someTextFile.txt"

#In this example we'll use the variable as param expansion passed to a variable


#Attempt 1: This will fail because this user doesn't have permissions on /home
fileLocation1=/home/${fileNameToCreate}
echo "Some text" > $fileLocation


#Attempt 2: Lets try working on the current user's path
userName=$(whoami) # Use the command whoami
fileLocation2=/home/${userName}/${fileNameToCreate}
echo "Some text" > fileLocation2



#Notice 1: Try to remove the $ from the last line - see what will happen (the file will be created in THIS path)


#Notice 2: Don't forget to delete the created text file