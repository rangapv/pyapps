#!/usr/bin/env python
#author: rangapv@yahoo.com 21-10-23

import os

class Node:
    def __init__(self):
        self.data = input("enter the Node data:")
        self.left = input('enter the left Child:')
        self.right = input('enter the Right Child:')
    def child(self):
        self.left = input(f'enter the left Child for {current_node.left}:')
        self.right = input(f'enter the Right Child for {current_node.right}:')

class buildtree:
    def __init__(self):
        current_node = Node()
        self.point = current_node
        list = []
        list.append(current_node.data)

    def AddNode(self):
        #list.pop()
        print(f'the list is {list}')
        if self.point is None:
           self.point = current_node
           list.append(current_node.data)
           return
        else:
           self.point = current_node.data


    def display1(self):
        print("inside display")
        print(f'The enterd integer is {b1.data}')

if __name__ == "__main__":
   b1 = buildtree()
   #b1.display1()
   while(True):
       inpu = input('Do yo want to add new node(y/n)')
       if inpu == 'y':
        b1.AddNode()
       else:
        break

