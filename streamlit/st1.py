#!/usr/bin/env python3
#author: rangapv@yahoo.com
#TO-RUN: python3 -m streamlit run ./st1.py

import streamlit as st
import os
import subprocess
import sys
import pandas as pd


st.write("Doker Statistics")

imgcnt = st.checkbox("I want Image count")

if imgcnt:
 def icnt():
   t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
   imgtlen = t1.stdout
   #print(contlen)
   len1 = len(imgtlen.splitlines())
   print("**********************")
   print(f'total images are {len1-1}')
   st.write(f'Image total is {len1-1}')
 icnt()

concnt = st.checkbox("I want container count")

if concnt:
 def ctntn():
   t1 = subprocess.run("docker container ps", capture_output=True, shell=True, text=True, check=True)
   contlen = t1.stdout
   #print(contlen)
   len2 = len(contlen.splitlines())
   print("**********************")
   print(f'total containers are {len2-1}')
 
   st.write(f'total containers are {len2-1}')
 ctntn()


newcnt = st.checkbox("New Count")

if newcnt:
   b = './dokarg.py -ctan'
   t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
   st.write(f'{t1.stdout}')


dokstat = st.checkbox("Docker status")

if dokstat:
   b = './dokarg.py -dstat f'
   t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
   #st.write(f'{t1.stdout}')


   st.table(pd.DataFrame({
    'Docker status': [t1.stdout],
   }))

imgsha = st.checkbox("Image sha layers")

if imgsha:
   b = './dokarg.py -sha 02e46c0524df'
   t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
   #st.write(f'{t1.stdout}')

   st.table(pd.DataFrame({
    'Image Layers': [t1.stdout],
   }))
