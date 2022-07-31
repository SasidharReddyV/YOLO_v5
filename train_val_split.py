#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:32:10 2022

@author: sasidharreddy
"""

import os
import shutil


src = '/Users/sasidharreddy/Desktop/train_g1/labels/train'

dst = '/Users/sasidharreddy/Desktop/train_g1/labels/val'

l = sorted(os.listdir(src))
print(l[0])
for i,v in enumerate(l):
    if(i%5==0):
        shutil.move(src+'/'+v, dst+'/'+v)