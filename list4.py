# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10]
print(sum(list1))
total=0
smile=[]
basket=[]
for i in list1:
    total=total+i
    print(total)
    if i <=5:
        k=i*20 
        smile.append(k)
        print(smile)
    else:
        p=i+100
        basket.append(p)
        print(basket)    