queue = [None for i in range(10)]
front_pointer = 0
rear_pointer = -1
queue_full = 10
queue_len = 0
item = None

#ENQUEUE
def enqueue(new_i):
    global queue_len, rear_pointer
    if queue_len < queue_full:
        if rear_pointer < len(queue) - 1:
            rear_pointer += 1
            print(f"Enqueue: {new_i}")
        else:
            rear_pointer = 0
        queue[rear_pointer] = new_i
        queue_len += 1
        
    else:
        print("Queue is full & cannot enqueue further")

#DEQUEUE
def dequeue():
    global queue_len, front_pointer, item
    if queue_len == 0:
        print("Queue is empty, cannot dequeue further")
    else:
        item = queue[front_pointer]
        queue[front_pointer] = None
        if front_pointer == len(queue) - 1:
            front_pointer = 0
        else:
            front_pointer += 1
        queue_len -= 1
        print(f"Dequeued: {item}")



#test
enqueue(10)
enqueue(15)
# dequeue()
# dequeue()

enqueue(89)
enqueue(190)
enqueue(34)
enqueue(32)
enqueue(54)
enqueue(87)
enqueue(19)
enqueue(121)
enqueue(122)
