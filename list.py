a=[1,2,3,4,5]
print(a)

colors=["red", "yellow", "blue"]
print(colors)
print(colors[2])
print(colors[1:3])


colors= colors + ["white", "orange", "brown"]
print(colors)


list=["high","low","more"]
if "low" in list:
    print("yes, it is")


housemade=[]
housemade.append("Jhon")
print(housemade)
housemade.append("Joseph")
print(housemade)


housemade.insert(0,"Luies")
print(housemade)

housemade.remove("Jhon")
print(housemade)

housemade.reverse()
print(housemade)

num=[2,5,1,8,16,9]
print(num)
num.sort()
print(num)


#dictionaries

sample={'key1':25,'key2':35,'key3':45,'key4':55,}
print(sample)
print(sample["key3"])