x,y,a=map(float,input().split())
s=x+a%3*int(x+y)%2//4
print("{:.2f}".format(s))
