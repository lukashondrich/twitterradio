# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:12:13 2021

@author: lukas
"""
import pyaudio
import wave
import os

# length of data to read.
chunk = 1024
# validation. If a wave file hasn't been specified, exit.
"""
if len(sys.argv) < 2:
    print("Plays a wave file.\n\n" +\
          "Usage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
"""
'''
************************************************************************
      This is the start of the "minimum needed to read a wave"
************************************************************************
'''


#for file in os.listdir("./"):
   #if file.endswith(".wav"):
       #print(os.path.join(file))
wav_files = [file for file in os.listdir("./") if file.endswith(".wav")]       
       
print(wav_files)
       
# create an audio object
p = pyaudio.PyAudio()

# open the file for reading.
wav_to_play = "output2.wav"
wf = wave.open(wav_to_play) #sys.argv[1], 'rb')
# open stream based on the wave object which has been input.
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(), input = True, input_device_index=1, output = True,
                rate = wf.getframerate())


# read data (based on the chunk size)
data = wf.readframes(chunk)
counter = 0
# play stream (looping from beginning of file to the end)
while data != '':

    if len(data)< chunk: 

        wav_files = [file for file in os.listdir("./") if file.endswith(".wav")]  
        sorted_by_mtime_ascending = sorted(wav_files, key=lambda t: os.stat(t).st_mtime)
        
        print(sorted_by_mtime_ascending)
        wav_to_play = sorted_by_mtime_ascending[counter]
        
        print(wav_to_play)
        wf = wave.open(wav_to_play)
        
        data = wf.readframes(chunk)
        counter+=1
    # writing to the stream is what *actually* plays the sound.
    stream.write(data)
    data = wf.readframes(chunk)

# cleanup stuff.
stream.close()    
p.terminate()