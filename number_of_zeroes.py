def zero():
    num=int(input())
    sum = 0
    for i in range(1,10):
        sum=sum+int(num/pow(5,i))
    return sum;    
def run_time():
    y=int(input())
    for i in range(y):
        no_of_zeroes=zero()
        print(no_of_zeroes)

run_time()
