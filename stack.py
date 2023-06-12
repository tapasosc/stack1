stack=[]

def push():
    element=int(input("enter the elemnt?:"))
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is empty!!")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)

while True:
    operation=int(input("enter the option: 1.push_element 2.pop_elemnt 3.quit :"))
    if operation==1:
        push()
    elif operation==2:
        pop()
    elif operation==3:

        break
    else:
        print("enter correct option!")
