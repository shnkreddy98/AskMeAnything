import sounddevice as sd
from scipy.io.wavfile import write
import datetime

def recordAudio():
    # creating audiofile with timestamp as filename (no use of saving audio files)
    filename = "audiofiles/"+str(datetime.datetime.now().timestamp())+".wav"
    # print(filename)

    # Sample rate
    fs = 44100
    # Duration of recording
    seconds = 4

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("recording...")

    # Wait until recording is finished
    sd.wait()

    # Save as WAV file 
    write(filename, fs, myrecording)
    
    return filename