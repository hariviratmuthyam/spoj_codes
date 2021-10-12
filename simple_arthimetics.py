def get_op():
    x=input()
    for i in ['+','-','*','/']:
        if i in x:
            global y
            y=x.split(i)
            op=i
            result=calc(op)
            print(' '+y[0])
            print(i+y[1])
            print((len(get_max([str(y[0]),str(y[1]),str(result)]))+1)*'-')
            print(' '+str(result)) 

def calc(operator):
    ch=operator
    if (ch=='+'):res=int(y[0])+int(y[1]);
    elif(ch=='-'):res=int(y[0])-int(y[1]);
    elif(ch=='*'):res=int(y[0])*int(y[1]);
    elif(ch=='/'):res=int(y[0])/int(y[1]);
    return res; 
    
def get_max(list):
    return max(list, key=len)
       
  
get_op()
