import templates
from flask import Flask, Response,render_template
import pyaudio
import wave
import os
app = Flask(__name__)


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

cwd = os.getcwd()

#audio1 = pyaudio.PyAudio()
p = pyaudio.PyAudio()
chunk = 1024

"""
def genHeader(sampleRate, bitsPerSample, channels):
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o
"""

@app.route('/audio')
def audio():
    # start Recording
    def sound():
        """
        CHUNK = 1024
        sampleRate = 44100
        bitsPerSample = 16
        channels = 2
        wav_header = genHeader(sampleRate, bitsPerSample, channels)

        stream = audio1.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,input_device_index=1,
                        frames_per_buffer=CHUNK)
        print("recording...")
        #frames = []
        first_run = True
        while True:
           if first_run:
               data = wav_header + stream.read(CHUNK)
               first_run = False
           else:
               data = stream.read(CHUNK)
           yield(data)

    return Response(sound())

    """
        # open the file for reading.
        wf = wave.open(cwd+"\\data\\output2.wav") #sys.argv[1], 'rb')
        # open stream based on the wave object which has been input.
        stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(), input = True, input_device_index=1, output = True,
                        rate = wf.getframerate())
        
        
        # read data (based on the chunk size)
        data = wf.readframes(chunk)
        counter = 0
        # play stream (looping from beginning of file to the end)
        while data != '':
            if len(data)< chunk: ## load new data if old data is streamed
                counter += 1
                print("end")

                wav_files = [file for file in os.listdir(cwd+"\\data\\") if file.endswith(".wav")]
                sorted_by_mtime_ascending = sorted(wav_files, key=lambda t: os.stat(cwd+"\\data\\"+t).st_mtime)
                print(wav_files)
                wf = wave.open(cwd+"\\data\\"+sorted_by_mtime_ascending[counter])
                #data = wf.readframes(chunk)
            # writing to the stream is what *actually* plays the sound.
            stream.write(data)
            data = wf.readframes(chunk)
            
           
        """   
        counter = 0    
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
        """
    return Response(sound())
        # cleanup stuff.
     #   stream.close()    
     #   p.terminate()



@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True,port=5001)