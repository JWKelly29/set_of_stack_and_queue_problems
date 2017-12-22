class Stack:
     def __init__(self):
         self.items = []


     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print "created Stack"

### Questions

#### Describe how you could use a single array to implement three stacks

#### Describe a stack in which in addition to push and pop function also has a minimum function.
#### The push, pop and minimum functions should all operate in O(1) time.


#### Implement a class which automatically creates a new stack when a certain limit is exceeded
#### This class should has a method to pop from any stack


#### Implement a myqueue class which implements a queue using two stacks

#### Write a write a program to sort a stack such that the smallest items are on top.
#### You can use an additional temporary stack but no other data structure. 
#### The stack supports push, pop, peek and isEmpty.

#### write a program for an animal shelter where customers who wish to adopt
#### an animal must choose the oldest animal (in terms of time at the shelter)
#### or they may choose a cat or a dog in which they will then recieve the oldest
#### cat or dog.
#### This queue will have four functions enqueue, dequeueAny, dequeueDog, dequeueCat



