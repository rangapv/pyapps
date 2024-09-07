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
   #print("t1 is {}".format(t1.stdout))
   len1 = len(t1.stdout)
   #print("the lengthis {}".format(len1))
   d2 = t1.stdout
   #print (d2[0])
   d1 = (t1.stdout).split(",")
   #st.table(pd.DataFrame({
   # d1[0]: [d1[1]],
   #}))
   st.json(
      {
        d1[0]: d1[1],
        d1[2]: [d1[3],d1[4]],
        d1[5]: d1[6]
      }
   )
  #st.table(df)

imgsha = st.checkbox("Image sha layers")

if imgsha:
   b = './dokarg.py -sha 02e46c0524df'
   t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
   #st.write(f'{t1.stdout}')

   st.table(pd.DataFrame({
    'Image Layers': [t1.stdout],
   }))
