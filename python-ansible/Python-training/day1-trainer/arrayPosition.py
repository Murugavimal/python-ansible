
userData=[12,13,14,15,16,17]
print("even indexs with values")
for i in range(0,len(userData),2):

    print(f"Index {i} -> {userData[i]}")
print("odd indexs with values")
for i in range(1,len(userData),2):

    print(f"Index {i} -> {userData[i]}")