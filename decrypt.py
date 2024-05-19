import os
from cryptography.fernet import Fernet
file_list=[]
for file in os.listdir():
    if file == "ransom.py" or file == "Ransom_key.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)
        
with open("Ransom_key.txt","rb") as generatekey:
    key_open=generatekey.read()
    
for file in file_list:
    with open(file,"rb") as openfile:
        content=openfile.read()
    decryptd=Fernet(key_open).decrypt(content)
    with open(file,"wb") as writefile:
        writefile.write(decryptd)
