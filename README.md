# Audio-Pre-Processing
**Data Preprocessing-Files Usage**

1.	Convert files from mp3 to wav
    - [ ] File: AudioConverter.py
    - [ ] Usage:
        - Select a name for your destination folder (line6)
        - Set the path of the parent directory (line9)
        - Set the path of the original directory-audio files you need to convert (line19)
        - Select the desired format (line33,34)
        - run the code

2.	Remove silence parts from the audios
    - [ ] File: Nonsilencedfilemaker.py
    - [ ] Parameters:
        - Select the sampling rate (it should be 8000/16000/32000/48000) (line186)
        - Select the aggressiveness parameter (an integer between 0 to 3) (line194)
    - [ ] Usage:
        - Set the path of the parent directory (line144,145)
        - Set the path of the directory of wav files you need to clean(remove silence) (line159)
        - Run the code

3.	Split audio files in chunks
    - [ ] File: ChunkAudiosWithOverlap.py
    - [ ] Parameters:
        - Select a desired duration for chunks (in ms) (line23)
        - Select a desired overlap for chunks (in ms) (line65)
    - [ ] Usage:
        - Set the path of the parent directory (line10)
        - Set the path of the directory of cleaned(nonsilenced) wav files you need to clean (line20)
        - Run the code
4.	Convert files from wav to ogg
    - [ ] File: AudioConverter.py
    - [ ] Usage:
        - Select a name for your destination folder (line6)
        - Set the path of the parent directory (line9)
        - Set the path of the original directory-audio files you need to convert (line19)
        - Select the desired format (line34)
        - run the code

