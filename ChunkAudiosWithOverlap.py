#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os,sys
import pydub
from pydub import AudioSegment


# Create directory to save chunked files
destdir_chunked = "chunkedfiles"

# Parent Directory path
parent_dir_chunked = "F:\\Capstone Project"

# Path to save chunked files
path_chunked = os.path.join(parent_dir_chunked, destdir_chunked)

# Create the directory
os.mkdir(path_chunked)
print("Directory '% s' created" % destdir_chunked)

# Path of the original files (nonsilencedfiles)
origindir_chunked = "F:\\Capstone Project\\convertedfiles"

# Desired duration to chunk files (in ms)
duration=5*1000

# This part of code read the directory of the nonsilenced files and create another directory with the
# same structure to save the chunked files                  
for root, subdirectories, _ in os.walk(origindir_chunked):
    for subdir in subdirectories:
        os.makedirs(os.path.join(path_chunked, subdir))
        path1=os.path.join(path_chunked,subdir)
        X_chunked=os.path.join(origindir_chunked,subdir)
        for _, _, files in os.walk(X_chunked):
            for i , file in enumerate(files):
                sound = AudioSegment.from_wav(os.path.join(X_chunked,file))
                # uncomment these two lines if you dont want to run the NonSilenceMakerFile because that file already converts
                # the audios to 1channel and do downsampling
                #sound.set_channels(1) 
                #sound.set_frame_rate(16000)    
                sound_duration=len(sound)
                print(sound_duration)

                # If the duration of files is less that desired duration, add silence to the end of file
                if sound_duration<duration:
                    pad_needed=duration-sound_duration
                    silence_seg = AudioSegment.silent(pad_needed+1000) #duration in milliseconds
                    #Add above two audio segments
                    trimmed_sound = sound + silence_seg
                    trimmed_soundname = os.path.join(path1, (file+"{0}.wav").format(i))
                    # Store the sliced audio file to the defined path
                    trimmed_sound.export(trimmed_soundname, format ="wav")
                    print("The sound needs padding")

                # If duration of the file equals to desired duration, save the file without change
                elif sound_duration==duration:
                    soundname = os.path.join(path1, (file+".wav").format(i))
                    # Store the sliced audio file to the defined path
                    sound.export(soundname, format ="wav")
                    print("The sound doesnt need to split")

                # If duration of the file is larger than the desired duration, chunk the file with overlap
                elif sound_duration>duration:
                    # Variable to count the number of sliced chunks
                    counter = 1
                    # Length of audio to overlap. 
                    overlap = 1.5 * 1000
                    # Initialize start and end seconds to 0
                    start = 0
                    end = 0
                    # Iterate from 0 to end of the file, with increment = interval
                    N=int(duration/2)
                    for i in range(0, sound_duration+N, duration):
                        # During first iteration, start is 0, end is the interval
                        if i == 0:
                            start = 0
                            end = duration
                        # All other iterations,start is the previous end - overlap
                        # end becomes end + interval
                        else:
                            start = end - overlap
                            # Create a temporary point for the end of the file
                            temp_end = start + duration
                            # If the temporary end is larger than the end of the original file, add silence
                            if temp_end > sound_duration:
                                pad_needed=temp_end-sound_duration
                                silence_seg = AudioSegment.silent(pad_needed) #duration in milliseconds
                                sound = sound + silence_seg
                                end= start + duration
                                print("Some pads added to the last file")
                                chunk = sound[start:end]
                                # Filename / Path to store the sliced audio
                                convertedfilename = os.path.join(path1, (file+"chunk{0}.wav").format(i)) 
                                # Store the sliced audio file to the defined path
                                chunk.export(convertedfilename, format ="wav")
                            else:
                                end = start + duration  
                                # Storing audio file from the defined start to end
                                chunk = sound[start:end]
                                # Filename / Path to store the sliced audio
                                convertedfilename = os.path.join(path1, (file+"chunk{0}.wav").format(i))
                                #convertedfilename = os.path.join(path2, 'chunked'+file+f'{i}')

                                # Store the sliced audio file to the defined path
                                chunk.export(convertedfilename, format ="wav")
                                # Print information about the current chunk
                        print("Processing chunk "+str(counter)+". Start = "+str(start)+" end = "+str(end))
                        # Increment counter for the next chunk
                        counter = counter + 1


# In[ ]:




