
# declare the empty array

use_numbers=[]

# ask the user to add the value

data=int(input(' How many numbers you wana add...! '))
print(f"loop will continue until : {data}")

for i in range(data):
    num= int(input(f" Enter Number {i+1} to insert "))
    use_numbers.append(num)
    print(use_numbers)
total=0
for num in use_numbers:
   
    
    if(num%2 ==0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    total +=num
print(f"addition is {total}")
    
    



#-------


