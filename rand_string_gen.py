import random #random library
import string #string library for letters
letter = string.ascii_letters #can also use ascii_lowercase or ascii_uppercase if thats what u need

while 1: #infinite loop
    val = random.choice(letter) + random.choice(letter)+ random.choice(letter)+ random.choice(letter)+ random.choice(letter)
    print(val)
    with open('string_values.txt','a') as file: #give access to the file and append the data
        file.write(val+"\n")
    file.close()  

