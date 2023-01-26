#x=3
#while x>0:
#    print(x)
#    x = x-1
#print('Happy New Years!')


#for i in [5, 4, 3, 2, 1]:
#    print(i)
#print('Happy New Years!')

#print('I like the following colors: ')
#colors = ['blue', 'red', 'yellow']
#for i in colors:
#    print(i)

count = 0
sum = 0
print('Enter a series of numbers and type "done" when finished: ')
while True:
    user = input('> ')
    if user == 'done':
        break

    try:
        fuser = float(user)
    except:
        print('invalid input')
        continue

    count = count + 1
    sum = sum + fuser

print('Count:' , count)
print('Sum:' , sum)
print('Average:' , sum/count)
