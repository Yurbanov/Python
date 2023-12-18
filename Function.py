



def price(qty=1):
    print("Price : ", qty*40,"$")
price()


def Add(a,b):
    print(a+b)

#fuction call process

Add(5,6)


def Add(a,b,c):
    print(a+b+c)

#fuction call process

Add(5,6,7)



def name():
    print("Cooking for everyone!")

name()
name()
name()
name()
name()



def Order(item):
    if (item == "lash"):
        return 1

itemname = input("Enter the item: ")
result = Order(itemname)
print("Result is", result)
if result == 1:
    print("Price: $5")


