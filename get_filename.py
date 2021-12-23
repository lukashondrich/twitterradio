#!/usr/bin/python

import sys 

def main(argv):
    print("./audio/tweetaudio_"+str(argv[0])+".wav")

if __name__ == "__main__":
    main(sys.argv[1:])