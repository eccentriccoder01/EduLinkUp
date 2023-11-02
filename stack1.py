#Program to illustrate STACK using List
stk=[]
top=None
def isEmpty(stk):
    if stk==[]:
        return True
    return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top],"<--Top")
        for m in range(top-1,-1,-1):
            print(stk[m])

#__main__
while True:
    print("STACK OPERATIONS")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")
    ch=int(input("Enter your choice(1-5) : "))
    if ch==1:
        item=int(input("Enter item : "))
        Push(stk,item)
    elif ch==2:
        item=Pop(stk)
        if item=='Underflow':
            print("Underflow!! Stack is Empty")
        else:
            print("Popped item is : ",item)
    elif ch==3:
        item=Peek(stk)
        if item=='Underflow':
            print("Underflow!! Stack is Empty")
        else:
            print("Topmost item is : ",item)
    elif ch==4:
        Display(stk)
    elif ch==5:
        break
    else:
        print("Wrong choice. Please choose the correct option.")
print("******Program Ends********")
