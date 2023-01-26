#success!

def computepay(h,r):
    if h <= 40.0:
        return h*r
    if h > 40.0:
        return ((h-40.0)*1.5*r)+(40.0*r)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
