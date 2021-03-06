

class ThreeStacks:
	def __init__(self, size):
		self.items = [None] * size
		self.stack_size = size / 3

		self.bottom_first = 0
		self.end_first = self.stack_size - 1
		self.start_middle = self.stack_size
		self.end_middle = (self.stack_size * 2) - 1
		self.start_last = self.stack_size * 2
		self.end_last = size - 1

		self.stack1_idx = 0
		self.stack2_idx = self.stack1_idx + self.stack_size
		self.stack3_idx = self.stack2_idx + self.stack_size

		

	
		

	def stack1_size(self):
		return self.stack1_idx 
	
	def stack2_size(self):
		return self.stack2_idx - self.end_first - 1

	def stack3_size(self):
		return self.stack3_idx - self.end_middle - 1

	def size(self):
		return (self.stack1_size() + self.stack2_size() + self.stack3_size())

	def push_stack1(self, item):
		if self.stack1_idx > self.end_first:
			print "Stack full"
			return False
		else:
			print "Added to Stack 1"
			self.items[self.stack1_idx] = item
			self.stack1_idx += 1
			return True


	def push_stack2(self, item):
		if self.stack2_idx > self.end_middle:
			print "Stack full"
			return False
		else:
			print "Added to Stack 2"
			self.items[self.stack2_idx] = item
			self.stack2_idx += 1
			return True

	def push_stack3(self, item):
		if self.stack3_idx > self.end_last + 1:
			print "Stack full"
			return False
		else:
			print "Added to Stack 3"
			self.items[self.stack3_idx] = item
			self.stack3_idx += 1
			return True

	def push_to_smallest_stack(self, item):

		if self.stack1_size() <= self.stack2_size() and self.stack1_size() <= self.stack3_size():
			self.push_stack1(item)
		elif self.stack2_size() <= self.stack1_size() and self.stack2_size() <= self.stack3_size():
			self.push_stack2(item)
		elif self.stack3_size() <= self.stack1_size() and self.stack3_size() <= self.stack2_size():
			self.push_stack3(item)
		else:
			self.push_stack1(item)

	def pop_stack1(self):
		if self.stack1_idx == self.bottom_first:
			print "Stack empty"
			return False
		else:
			print "Popped from Stack 1"
			self.stack1_idx -= 1
			self.items[self.stack1_idx] = None
			return True


	def pop_stack2(self):
		if self.stack2_idx == self.start_middle:
			print "Stack empty"
			return False
		else:
			print "Popped from Stack 2"
			self.stack2_idx -= 1
			self.items[self.stack2_idx] = None
			return True

	def pop_stack3(self):
		if self.stack3_idx == self.start_last:
			print "Stack empty"
			return False
		else:
			print "Popped from Stack 3"
			self.stack3_idx -= 1
			self.items[self.stack3_idx] = None
			return True

	def pop_from_largest(self):
		if self.stack1_size() > self.stack2_size() and self.stack1_size() > self.stack3_size():
			self.pop_stack1()
		elif self.stack2_size() > self.stack1_size() and self.stack2_size() > self.stack3_size():
			self.pop_stack2()
		elif self.stack3_size() > self.stack1_size() and self.stack3_size() > self.stack2_size():
			self.pop_stack3()
		else:
			self.pop_stack1()

	def peek_from_stack(self, stack):
		if stack == 1:
			print self.items[self.stack1_idx - 1]
			return self.items[self.stack1_idx - 1]
		elif stack == 2:
			print self.items[self.stack2_idx - 1]
			return self.items[self.stack2_idx - 1]
		else:
			print self.items[self.stack3_idx - 1]
			return self.items[self.stack3_idx - 1]
		




class StackWithMinumum:
	def __init__(self):
		self.items = []
		self.minimum = []


	def isEmpty(self):
		return self.items == []

	def push(self, item):
		if len(self.minimum) == 0:
			self.minimum.append(item)
		if item < self.minimum[-1]:
			self.minimum.append(item)
		self.items.append(item)

	def pop(self):
		if self.items[-1] == self.minimum[-1]:
			self.minimum.pop()
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def minimumValue(self):
		print self.minimum[-1]
		return self.minimum[-1]

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


class AutomaticStackGenerator:
	def __init__(self, limit):
		self.stacks = [Stack()]
		self.limit = limit

	def size(self):
		return len(self.stacks)

	def stack_sizes(self):
		arr = []
		index = 0
		while index < len(self.stacks):
			arr.append(self.stacks[index].size())
			index += 1
		return arr

	def isEmpty(self):
		return self.stacks == []

	def push(self, item):

		if len(self.stacks[-1].items) == self.limit:
			self.stacks.append(Stack())
			self.stacks[-1].items.append(item)
		else:
			self.stacks[-1].items.append(item)

	def pop_from_stack(self,stack_idx):
		if stack_idx > len(self.stacks) - 1 or stack_idx < 0:
			print "stack doesn't exist. Please enter a number between 0 and the number of stacks - 1"
			return False

		if len(self.stacks[stack_idx].items) == 1:
			self.stacks.pop(stack_idx)
		else:
			self.stacks[stack_idx].items.pop()





class MyQueue:
	def __init__(self):
		self.queue_items = Stack()
		self.dequeue_items = Stack()

	def queue(self, item):
		self.queue_items.push(item)

	def dequeue(self):
		index = 0
		length = len(self.queue_items.items)
		while index < length:
			item = self.queue_items.pop()
			if index == length - 1:
				pass
			else:
				self.dequeue_items.push(item)

			index += 1

		index = 0
		length = len(self.dequeue_items.items)
		while index < length:
			item = self.dequeue_items.pop()
			self.queue_items.push(item)
			index += 1

	def show_items(self):
		print("Queued items", self.queue_items.items)
		print("Dequeued items", self.dequeue_items.items)
		return self.queue_items.items, self.dequeue_items.items

class StackSorter:
	def __init__(self):
		self.stack = Stack()
		

	def sort_stack(self):
		if self.stack.isEmpty() == False:
			popped = self.stack.pop()
			self.sort_stack()
			self.insertToStack(self.stack, popped)
		print self.stack.items
		

	def insertToStack(self, stack, popped):
		if stack.isEmpty() == True or popped > stack.peek():
			
			stack.push(popped)
			
		else:
			temp_pop = stack.pop()
			self.insertToStack(stack, popped)
			stack.push(temp_pop)
		


	def add_values_to_stack(self, values):
		for value in values:
			self.stack.push(value)
			print value






### Questions

#### Describe how you could use a single array to implement three stacks

ts = ThreeStacks(9)
ts.push_to_smallest_stack(1)
ts.peek_from_stack(1)
ts.push_to_smallest_stack(2)
ts.peek_from_stack(2)
ts.push_to_smallest_stack(3)
ts.peek_from_stack(3)
ts.push_to_smallest_stack(4)
ts.push_to_smallest_stack(5)
ts.push_to_smallest_stack(6)
print("size of three stack", ts.size())
ts.push_to_smallest_stack(7)
ts.push_to_smallest_stack(8)
ts.push_to_smallest_stack(9)
print("size of three stack", ts.size())
ts.pop_from_largest()
print("size of three stack", ts.size())
ts.pop_stack2()
print("size of three stack", ts.size())
ts.peek_from_stack(2)

print("*"*50)




#### Describe a stack in which in addition to push and pop function also has a minimum function.
#### The push, pop and minimum functions should all operate in O(1) time.

print "created Stack with minimum"

s = StackWithMinumum()

s.push(10)
s.push(7)
s.push(14)
s.push(29)
s.push(105)



print("stacks minimum is ", s.minimumValue())
print("*"*50)

#### Implement a class which automatically creates a new stack when a certain limit is exceeded
#### This class should has a method to pop from any stack

print "Created Stack with automatic stack generator with limit of 3"

sa = AutomaticStackGenerator(3)

sa.push(2)
sa.push(24)
sa.push(98)
sa.push(21)

print("should be two stacks",sa.size())
sa.pop_from_stack(0)
print("should be two stacks, one with 2 items and another with 1", sa.stack_sizes())


#### Implement a myqueue class which implements a queue using two stacks

mq = MyQueue()
mq.queue(1)
mq.queue(2)
mq.queue(3)
mq.dequeue()
mq.show_items()

#### Write a program to sort a stack such that the smallest items are on top.
#### You can use an additional temporary stack but no other data structure. 
#### The stack supports push, pop, peek and isEmpty.

#### Wasn't able to sort stack using another stack but was able to use recursion. I will come back to this problem at a later date.

stack_sorter = StackSorter()
stack_sorter.add_values_to_stack([1,97,34,56,23,21,12,89,1090])
stack_sorter.sort_stack()


#### write a program for an animal shelter where customers who wish to adopt
#### an animal must choose the oldest animal (in terms of time at the shelter)
#### or they may choose a cat or a dog in which they will then recieve the oldest
#### cat or dog.
#### This queue will have four functions enqueue, dequeueAny, dequeueDog, dequeueCat



