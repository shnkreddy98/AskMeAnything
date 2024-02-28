import audiorecording
import transcribe
import chatgeneration
import os
import sys

if __name__ == "__main__":
    
    try:
        apikey = sys.argv[1]
    
    except:
        apikey = os.getenv("OPENAI_API_KEY")

    if apikey is None:
        print("APIKEY not set properly")
        exit()

    filename = audiorecording.recordAudio()

    client, user_text = transcribe.speechToText(filename, apikey)

    response = chatgeneration.generateText(client, user_text)

    print(" ".join(response))
