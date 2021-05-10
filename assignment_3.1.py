hrs = input("Enter Hours:")
rate = float(input("Enter your Rate"))
h = float(hrs)

if h>40:
    sum = h-40
    print((sum*rate*1.5) + (40*rate))
    
else:
    print(h*rate)