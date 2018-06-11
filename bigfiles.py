#! /usr/bin/env python3
# bigfiles.py - searches for bigfiles

import os,shutil

def bigfile(folder,size):
    
    folder = os.path.abspath(folder)
    os.chdir(folder)
    os.chdir('..')
    
  
   
    

    for foldername, subfolders,filenames in os.walk(folder):
        print('Searching files in %s...' %(foldername))
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername,filename))>size
                print(os.path.join(foldername,filename))
                print( '/t' + os.path.getsize(os.path.join(foldername,filename)))
            
    print('Done.')
            

bigfile('/Users/Adil/Documents/Python','10')
