#Password generator
#for loop
 import random
 passlen=int(input("Enter the length of password: "))
 s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
 m=""
 for i in range(passlen):
    m=m+random.choice(s)
 print(m)
