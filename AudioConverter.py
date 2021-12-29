#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os,sys
import pydub
from pydub import AudioSegment

# Directory to save converted files
destdirectory = "convertedfiles"

# Parent Directory path
parent_dir = "F:\Capstone Project"

# Path of the destination directory
path = os.path.join(parent_dir, destdirectory)

# Create the directory
os.mkdir(path)
print("Directory '% s' created" % destdirectory)

# Directory to read mp3 files
origindirectory = "F:\Capstone Project\Birdsdataset"

# In this part, the code read the original directory and create another directory with the same structure
# to save wave files
for root, subdirectories, _ in os.walk(origindirectory):
    for subdirectory in subdirectories:
        # Create directory to save converted (wave) files
        os.makedirs(os.path.join(path, subdirectory))
        path2=os.path.join(path,subdirectory)
        X=os.path.join(origindirectory,subdirectory)
        for _, _, files in os.walk(X):
            for i , file in enumerate(files):
                if file.endswith(".mp3"):
                    song = AudioSegment.from_mp3(os.path.join(X,file))
                    convertedfilename = os.path.join(path2, (subdirectory+"{0}.wav").format(i))
                    song.export(convertedfilename, format="wav")


# In[ ]:




