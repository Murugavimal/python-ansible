
userAge=input('Enter your age ')
age=int(userAge)

if age <0:
    print('Enter Valid Age')
elif age<18:
    print('Not allowed to Vote')
elif age>=18 and age<79:
    print('Allowed to Vote')
else:
    print('senior citizen')