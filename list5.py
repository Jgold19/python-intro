list1=[1,2,4,6,7,9,10]
#print all the list less than 39
print("All the list less or equal to 29")
y=0        
hold=10
collate=[]        
for p in list1:
    y=y+p
    if y>=hold:
        collate.append(y)
        print(collate)