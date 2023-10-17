#!/usr/bin/env python
import os

class str:
    def __init__(self):
       self.str1 = input('enter the string:')
       self.index = len(self.str1)
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        #print(self.index)
        self.index = self.index - 1
        #print(f'{self.str1[self.index]}')
        return self.str1[self.index] 


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class list:
    def __init__(self):
        self.head = None
        self.count = 0
        self.ecount = 0
        self.pcount = 0
        self.pecount = 0
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            self.count = self.count + 1
            return
        else:
            new_node.next = self.head
            self.head = new_node
            self.ecount = self.ecount + 1
    def pc(self):
        print(f'count is {self.count}')
        print(f'ecount is {self.ecount}')
    def pcf(self):
        print(f'pcount is {self.pcount}')
        print(f'pecount is {self.pecount}')
    def printLL(self):
        current_node = self.head
        if self.next is None:
            current_node = self.head
            self.pcount = self.pcount + 1
        else:
            print(current_node.data)
            self.pecount = self.pecount + 1
    def bprintLL(self):
        current_node = self.head
        #print(current_node.data)
        while(current_node):
            #print(current_node.data)
            current_node = current_node.next
    def nprint(self):
        current_node = self.head
        #print(f'inside nprint {current_node.data}')
        list = []
        rt = ' '
        rt2 = ' '
        while(current_node):
            if current_node.next is None:
                #print(f'inside nprint {current_node.data}')
                #print("inside nprint-2")
                list.append(current_node.data)
                break
            else:
                list.append(current_node.data)
                #print(f'inside nprint {current_node.data}')
                current_node = current_node.next 
                self.head = current_node
                #print("inside nprint-3")
        while len(list) > 0:
            rt = (list[-1])
            #rt1 = str(rt)
            list.pop()
            rt2 = rt2 + rt 
        print("Printing the Reverse of Input")
        print (f'The string is {rt2}')

if __name__ == "__main__":
  f = str()
  print(f'{f.str1} and the length is {f.index}')
  r = iter(f)
  rj = ''.join(r)
  print(f'Reversion using plain old iter() {rj}')
  #print(r)
  #n1 = Node('f.str1')
  n1 = list()
  for a in rj:
      #print(f'a is {a}')
      n1.insertAtBegin(a)
  #n1.printLL()
  n1.bprintLL()
  #n1.pc()
  #n1.pcf()
  n1.nprint()
