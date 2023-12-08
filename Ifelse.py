x = int(input('Enter a number: '))

"""if x % 2 == 0:
    print('even number')
elif x % 2 !=0:
    print('odd number')
else:
    print('try again')"""

if x > 0:
    for i in range(2, x):
        if x % 2 == 0:
            print('not a prime number')
            break
        else:
            print('prime number')
            break
else:
    print('give a positive number')



# While LOOPING

i = 1
j = 1
while i <= 5:
    print('Programmer' ,i)
    while j <= 6:
        print('Data analysis' ,end='')
        j = j+1
    i = i+1
    

for i in[3,6, 'Programmer']:
    print(i)

for i in range(12):
    print(i)

for i in range(1,12):
    print(i)

print('* * * *')


for i in range(4):
    for j in range(i+1):
        print('* ', end="")

    print()

for i in range(4):
    for j in range(4-i):
        print('* ', end="")

    print()
