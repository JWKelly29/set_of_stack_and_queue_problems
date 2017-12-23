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


class ThreeStacks:
	def __init__(self, size):
		self.items = [None] * size
		self.stack_size = size / 3

		self.bottom_first = 0
		self.end_first = stack_size - 1
		self.start_middle = stack_size
		self.end_middle = (stack_size * 2) - 1
		self.start_last = stack_size * 2
		self.end_last = size - 1

		self.stack1_idx = 0
		self.stack2_idx = self.stack1_idx + stack_size
		self.stack3_idx = self.stack2_idx + stack_size

		
		

	def push(self, item):

		

	def pop(self):
		

	def size(self):
		






s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print "created Stack"

### Questions

#### Describe how you could use a single array to implement three stacks

ts = ThreeStacks()
ts.push(1)
ts.push(2)
ts.push(3)
ts.push(4)
ts.push(5)
ts.push(6)
ts.push(7)
ts.push(8)
ts.push(9)

print("size of three stack", ts.size)
print("last item added to three stack", ts.peek_last)



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



