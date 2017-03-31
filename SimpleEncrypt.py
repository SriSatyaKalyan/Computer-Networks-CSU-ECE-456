#!/usr/bin/env python

import sys

Keys = open(sys.argv[1], "r")    #Taking the 'keys.txt' file as argument 1 to read the keys
key = Keys.read()
lenofkey = len(key)             #Length of Key

Data = open(sys.argv[2],"r")    #Taking the 'data.txt' file as argument 2 to read the data
data = Data.read()              #Read data from file
lenofdata = len(data)           #Length of data

if ((lenofdata)%2 == 1):        #Checking if the length of data is even 
    data = data +'\0'           #Appending a Null Character to data
    
iter = 0                        #Initializing iteration to zero
encdata = ''                    #Creating a null string
while (iter<lenofdata):         #Starting the loop for encrypting the data
    modata = data[iter:(iter+2)]
    g =len(modata)
    fchar = modata[:int(g/2)]
    schar = modata[int(g/2):]
    keyiter = 0
    binga = fchar+schar
    while (keyiter < lenofkey): #Considering keys and encrypting the data
        repchar = fchar
        fchar = schar
        schar = repchar
        mokey = key[keyiter]
        schar = chr(ord(schar)^ord(mokey))
        linga = fchar+schar
        keyiter += 1
    encdata += linga           #Appending the encrypted data to a variable, two bits at a time
    iter += 2
    
print('The key is:           ',key)
print('The input data is:    ',data)
print('The encrypted data is:')
print(str(encdata))
print('and it is stored in encdata.txt')

f = open('encdata.txt', 'w')   #Writing the encrypted data in a file named 'encdata.txt'
f.write(encdata) 
f.close()











