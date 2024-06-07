from random import *
# import os

i_pwd = input("Enter your password: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3',
       '4', '5', '6', '7', '8', '9', '0', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
pw = ""
while pw != i_pwd:
    pw = ""
    for i in range(len(i_pwd)):
        guess_pwd = pwd[randint(0, 35)]
        pw += guess_pwd
    print(pw)
print("Password is: ", pw)
