import random
list1=[0,1,2,3,4,5,6,7,8,9]
list2=[]
for i in range(0,5):
    a=random.randint(0,list1[i])
    list2.append(a)
print(list2)
choice=int(input("enter number: "))
j=0
while j<len(list2):
    if choice in list2:
        print(choice,"present in list2")
    else:
        print("not present in list")
    j=j+1
    break
