#pay with bonus over $40

print('This code will compute your total pay. If you work over 40 hours, your rate will be multiplied by 1.5, thus earning you more money.')

hrs = input('Enter Hours:')
try:
    hval = float(hrs)
except:
    hval = -1

if hval > 0:
    rate = input('Enter Rate Per Hour:')
else:
    hrs = input('Enter a number:')
    rate = input('Enter Rate Per Hour:')

try:
    hval = float(hrs)
except:
    hval = -1

try:
    rval = float(rate)
except:
    rval = -2

if rval > 0:
    print('one moment...')
else:
    rate = input('Enter a number:')

try:
    rval = float(rate)
except:
    rval = -2

if hval > 40.0:
    rval= rval * 1.5
else:
    rval = rval * 1.0

gross = hval * rval
print('Pay:' , gross)
