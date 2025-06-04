mylist=input("enter a list of numbers seperated by space:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    sum=sum+num
    print("the sum of the numbers is",sum)
