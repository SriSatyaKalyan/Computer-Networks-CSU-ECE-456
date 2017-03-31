import sys

Keys = open(sys.argv[1], "r")       #Taking the 'keys.txt' file as argument 1 to read the keys
key = Keys.read()
lenofkey = len(key)                 #Length of Key

encdata = open(sys.argv[2],"r")     #Taking the 'encdata.txt' file as argument 2 to read the encrypted data
decdata = encdata.read()            #Reading the encrypted data
lenofddata = len(decdata)           #Calculating the length of encrypted data

                
diter = 0                           #Initializing iteration to zero
dencdata = ''                       #Creating a null string
while (diter<lenofddata):           #Starting the loop for encrypting the data
    modata = decdata[diter:diter+2]
    g =len(modata)
    fchar = modata[:int(g/2)]
    schar = modata[int(g/2):]
    keyiter = lenofkey-1
    binga = fchar+schar
    while (keyiter>=0):             #Considering keys and decrypting the data
        dinga = fchar+schar
        mokey = key[keyiter] 
        schar = chr(ord(schar)^ord(mokey))
        repchar = fchar
        fchar = schar
        schar = repchar
        binga = fchar+schar
        keyiter -= 1
    dencdata += binga               #Appending the dencrypted data to a variable, two bits at a time
    diter += 2
    
if (dencdata[len(dencdata)-1] == '\x00'):     #Checking if the length of data is even 
    dencdata = dencdata[:len(dencdata)-1]     #Removing Null Character to data
                         
f = open('dencdata.txt', 'w')       #Open a file named 'dencdata.txt' and writing decrypted data
f.write(dencdata)                   
f.close()

print('The key is:           ',key)
print('The encrypted data is:',decdata)
print('The decrypted data is:',dencdata)
