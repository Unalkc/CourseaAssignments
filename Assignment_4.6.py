def computepay(h,r):
    if h>40:
        p = ((h-40)*1.5 *r)+(40*r)
    else:
        p = r * h
    return p

hrs = float(input("Enter Hours:"))
rate =  float(input("Enter a Rate "))
p = computepay(hrs,rate)
print("Pay",p)