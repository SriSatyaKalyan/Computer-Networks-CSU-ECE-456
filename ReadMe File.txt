The zip file folder contains:
SimpleEncrypt.py 
SimpleDecrypt.py
ReadMe File.txt
keys.txt
data.txt
encdata.txt
dencdata.txt

All these files should be saved in one folder and this folder address should be the directory of the Command Prompt. 

To encrypt the data, the following code should be run:
C:\---\---\Python WorkSpace> python SimpleEncrypt.py keys.txt data.txt

To decrypt the data, the following code should be run:
C:\---\---\Python WorkSpace> python SimpleDecrypt.py keys.txt encdata.txt

The 'SimpleEncrypt.py' and 'SimpleDecrypt.py' files are python files. The 'SimpleEncrypt.py' file takes the 'keys.txt' and 'data.txt' files as argument 1 and argument2 respectively
and encrypts the data . This encrypted data is stored in 'encdata.txt' file. The 'SimpleDecrypt.py' file takes 'keys.txt' file and 'encdata.txt'as arguments 1 
and 2 respectively. It then prints out the decrypted data which should be the input data in the 'data.txt' file. The decrypted output is also stored in 'dencdata.txt' file.

There is a problem with Python 3.5 which sometimes does not decrypt the characters in correct manner.
However, this problem can be avoided by using Python 2.7.