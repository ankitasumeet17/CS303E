largest = None
smallest = None
while True:
    user = input('Enter a number: ')
    if user == 'done':
        break

    try:
        iuser = int(user)
    except:
        print('invalid input')
        continue

    if largest is None or largest < iuser:
        largest = iuser

    if smallest is None or smallest > iuser:
        smallest = iuser

print('Maximum is ' , largest)
print('Minimum is ' , smallest)
