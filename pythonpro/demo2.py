list1=[2,3,4,5,6,7,8,9,2,2,2,23,3,3]
list2=[]
list2.append(list1[0])
i=0
j=0
for i in list2:
    for j in list1:
        if list2[i] != list1[j]:
            j=j+1
    list2.append(list1[j])
    i=i+1
print(list2)
