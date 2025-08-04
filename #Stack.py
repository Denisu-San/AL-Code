#Stack
Stack = [None for i in range(0,10)]
TopPointer = 0
BasePointer = 1
StackFul = 10
Item = None

def push(new_item):
    global TopPointer
    if TopPointer < StackFul:
        TopPointer = TopPointer + 1
        Stack[TopPointer] = new_item
        print(f"pushed item: {new_item}")
    else:
        print("Stack is full") 
        
        
def pop():
    global TopPointer, Item
    if TopPointer == BasePointer - 1:
        print("Stack is empty")
    else:
        item = Stack[TopPointer]
        Stack[TopPointer] = None
        TopPointer = TopPointer - 1
        print(f"Item has been popped: {item}")

push(91)
push(81)
push(12)
pop()
pop()
pop()
pop()