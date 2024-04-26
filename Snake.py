# import
from __future__ import annotations
import random
import dudraw
class Node:
    # nodes
    def __init__(self,value=None,next=None,prev=None):
        # inits the node stuff
        self.value=value
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    # whole lotta classes that do stuff with linked lists
    def __init__(self):
        # initializes header trailer size
        self.header=Node()
        self.trailer=Node()
        self.trailer.prev=self.header
        self.header.next=self.trailer
        self.size=0

    def get_size(self):
        # returns length of list
        return self.size
    
    def is_empty(self):
        # checks if list is empty
        if self.header.next is self.trailer:
            return True
        else:
            return False

    def remove_between(self, node1:Node, node2:node):
        # removes node between specified nodes
        # check if either node1 or node2 is None. Raise a ValueError if so.
        if node1 is None:
            raise ValueError("Node1 is empty.") 
        elif node2 is None:
            raise ValueError("Node2 is empty.") 
        # Check that node1 and node 2 has exactly 1 node between them. Raise a ValueError if so.
        elif node1.next.next is not node2 and node2.prev.prev is not node1:
            raise ValueError("Nodes must only have 1 node between them.")
        # Everything is in order, so delete the node between node1 and node2 
        else:
            # get the value of the node being removed to return it
            return_node=node1.next.value
            # set the next and previous to each other
            node1.next=node2
            node2.prev=node1
            # returning the value that was stored in it
            self.size-=1
            return return_node

    def add_between(self,value,A:Node,B:Node):
        # adds node between specified nodes
        # nodes must be one after another
        if A.next is not B:
            raise ValueError("Nodes must be consecutive.")
        else:
            temp_node=Node(value,B,A)
            temp_node.next.prev=temp_node
            temp_node.prev.next=temp_node
            self.size+=1

    def add_first(self,value):
        # adds node to beginnning using add betweeen
        self.add_between(value,self.header,self.header.next)

    def add_last(self,value):
        # adds node to end using add between
        self.add_between(value,self.trailer.prev,self.trailer)

    def remove_first(self):
        # remove and return first node using remove between
        return self.remove_between(self.header,self.header.next.next)

    def remove_last(self):
        # remove and return last node using remove between
        return self.remove_between(self.trailer.prev.prev,self.trailer)
        
    def first(self):
        # returns value of first node
        return self.header.next.value

    def last(self):
        # returns value of last node
        return self.trailer.prev.value

    def get(self, ind):
        # gets value of node at specified index
        #IndexError
        if ind>=self.size:
            raise IndexError("Index is out of range.")
        #step 1: create variable to track the index
        ind_value=0
        #step 2: create a second variable to traverse the list 
        temp_node=self.header.next
        #step 3: traverse list until the given index and return value
        while True:
            if ind_value==ind:
                return temp_node.value
            temp_node=temp_node.next
            ind_value+=1

    def remove_at_index(self,ind:int):
        # remove node at specific index
        if self.header.next is self.trailer:
            return "list is empty"
        else:
            # goes thorugh until it gets to right node
            temp_node=self.header.next
            temp_ind=0
            while temp_ind is not ind:
                temp_ind+=1
                temp_node=temp_node.next
        # uses remove between with prev and next node to get rid of it
        node1=temp_node.prev
        node2=temp_node.next
        remove_between(node1,node2)

    def search(self, value):
    #    returns index of the specific value
        ind=0
        temp_node=self.header.next
        #get to right vlaue
        while temp_node.value is not None:
            if temp_node.value==value:
                return ind
            else:
                ind += 1
                temp_node=temp_node.next
        #if the value is not found, return -1
        return -1

    def __str__(self)->str:
        # makes string look nice to print out
        if self.header.next is self.trailer:
            # print [] if empty
            return "[]"
        else:
            # start with[ end with] and have values with , inbetween
            temp_str="["
            temp_node=self.header.next
            while temp_node is not None and temp_node.value is not None:
                temp_str+=str(temp_node.value)
                # interior Node
                if temp_node.next is not self.trailer:
                    temp_str+=", "
                # end node
                else:
                    temp_str+="]"
                temp_node=temp_node.next
        return temp_str

class Snake:
    # all the snake stuff
    # the directions
    still=' '
    right='d'
    left='a'
    up='w'
    down='s'

    def __init__(self, x, y):
        # inits the important stuff
        self.body=DoublyLinkedList()
        self.body.add_first((x, y))
        self.direction=Snake.still

    def move(self):
        # moves snake
        temp_value=self.body.first()
        x=temp_value[0]
        y=temp_value[1]
        # directions
        if self.direction==Snake.left:
            (x, y)=temp_value[0] - 1, temp_value[1]
        elif self.direction==Snake.right:
            (x, y)=temp_value[0] + 1, temp_value[1]
        elif self.direction==Snake.down:
            (x, y)=temp_value[0], temp_value[1] - 1
        elif self.direction==Snake.up:
            (x, y)=temp_value[0], temp_value[1] + 1
        # add head to top and remove tail
        self.body.add_first((x, y))
        self.body.remove_last()

    def eat_and_grow(self, food):
        # head of the snake
        head=self.body.first()
        # tail of the snake
        tail=self.body.last()
        x=tail[0]
        y=tail[1]
        #add in the opposite direction of the head
        if head[0]==food[0] and head[1]==head[1]:
            if self.direction==Snake.left:
                (x, y)=tail[0] + 1, tail[1]
            elif self.direction==Snake.right:
                (x, y)=tail[0] - 1, tail[1]
            elif self.direction==Snake.down:
                (x, y)=tail[0], tail[1] + 1
            elif self.direction==Snake.up:
                (x, y)=tail[0], tail[1] - 1
            self.body.add_last((x, y))

    def check_crash(self):
        # check if snake hit wall or itself
        head=self.body.first()
        if (head[0] + .5 < 0 or head[0] + .5 > 20 or head[1] + .5 > 20 or head[1] + .5 < 0):
            return True
        x=head[0]
        y=head[1]
        for i in range(1, self.body.size):
            if self.body.get(i)[0]==x and self.body.get(i)[1]==y:
                return True   
        return False
    
    def draw(self):
        # draws snake
        temp_node=self.body.header.next
# draw green snake entire body unitl gets to end
        while temp_node.value is not None:
            dudraw.set_pen_color(dudraw.DARK_GREEN)
            dudraw.filled_square(temp_node.value[0], temp_node.value[1], .5)
            temp_node=temp_node.next

class Food:
    # does all the food stufrf
    def __init__(self):
        # init stuff
        self.loc=(0, 0)
        self.spawn_food()

    def draw(self):
        # draw food orange that looks yellow
        dudraw.set_pen_color(dudraw.ORANGE)
        dudraw.filled_square(self.loc[0], self.loc[1], .5) 

    def spawn_food(self):
        # spawn food
        while True:
            # make food random place
            x=random.randint(0 ,19)
            y=random.randint(0, 19)
# if no snake then make food
            if snake.body.search((x, y))==-1:
                self.loc=(x, y)
                break

#main 
#canvas
scale=500
dudraw.set_canvas_size(scale, scale)
dudraw.set_x_scale(-.5, 19.5)
dudraw.set_y_scale(-.5, 19.5)
# set key
key=' '
# make snake and food
snake=Snake(10, 10)
food=Food()
game_over=False
base_limit=20 #base number of frames till snake moves
timer=0  #keep track of frames
# repeat until over
while not game_over:
    timer += 1

    # check key typed
    if dudraw.has_next_key_typed():
        key=dudraw.next_key_typed()
    # directions
    if key=='w':
        snake.direction=Snake.up
    elif key=='a':
        snake.direction=Snake.left
    elif key=='s':
        snake.direction=Snake.down
    elif key=='d':
        snake.direction=Snake.right
    # calculate limit based on snake size
    limit = max(1, base_limit - snake.body.get_size())
    # timer limit
    if timer==limit:
        dudraw.clear(dudraw.LIGHT_GRAY)
        timer=0
        #draw and move snake
        snake.draw()
        food.draw()
        snake.move()
        # snake eat food and grow and more food appear
        if snake.body.first()==food.loc:
            snake.eat_and_grow(food.loc)
            food.spawn_food()
        # check if snake dead
        if snake.check_crash()==True:
            game_over=True
    # ded
    snake.draw()
    # show
    dudraw.show(40)
