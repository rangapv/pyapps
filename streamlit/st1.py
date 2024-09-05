#!/usr/bin/env python3
#author: rangapv@yahoo.com

import streamlit as st

import os
import subprocess
import sys


st.write("Doker Statistics")


imgcnt = st.checkbox("I want Image count")

if imgcnt:
   #imgcnt(on_change(python3 /Users/rangapv/pydok/dokarg.py -img))
   #t = on_change("python3 /Users/rangapv/pydok/dokarg.py -img")
   t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
   imgtlen = t1.stdout
   #print(contlen)
   len1 = len(imgtlen.splitlines())
   print("**********************")
   print(f'total images are {len1-1}')

   st.write(f'Image total is {len1-1}')

concnt = st.checkbox("I want container count")

if concnt:
   t1 = subprocess.run("docker container ps", capture_output=True, shell=True, text=True, check=True)
   contlen = t1.stdout
   #print(contlen)
   len2 = len(contlen.splitlines())
   print("**********************")
   print(f'total containers are {len2-1}')
 
   st.write(f'total containers are {len2-1}')
   
