def add_rev():
    num=input()
    for i in range(int(num)):
        (x,y)=input().split(" ")
        x=str(x)
        x=x[::-1]
        y=str(y)
        y=y[::-1]
        res=int(x)+int(y)
        print(res); 
add_rev()
