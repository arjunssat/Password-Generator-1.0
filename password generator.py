#Password generator
import random
passlen=int(input("Enter the length of password: "))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
p="".join(random.sample(s, passlen))
print(p)

#for loop
# import random
# passlen=int(input("Enter the length of password: "))
# s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
# m=""
# for i in range(passlen):
#    m=m+random.choice(s)
# print(m)