# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10]
print(sum(list1))
total=0
basket=[]
smile=[]
for i in list1:
    total=total+i
    print(total)
    if i >=5:
        
        basket.append(i)
        print(basket)
        if i <=5:
            smile.append(i)
            print(smile)
        
    
    