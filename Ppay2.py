hrs = input('Enter Hours:')
try:
    hval = float(hrs)
except:
    hval = -1

if hval > 0:
    rate = input('Enter Rate Per Hour:')
else:
    hval = -1

try:
    rval = float(rate)
except:
    rval = -2

nval = 1.5*(hval-40.0)*rval
gross = (hval*rval) + nval
gross2 = (hval*rval)

if hval > 40.0:
    print(gross)
else:
    print(gross2)
