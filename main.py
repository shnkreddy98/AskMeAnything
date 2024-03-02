import audiorecording
import transcribe
import chatgeneration
import os
import sys
import argparse

def main(params):

    apikey = params.apikey
    
    filename = audiorecording.recordAudio()
    client, user_text = transcribe.speechToText(filename, apikey)
    response = chatgeneration.generateText(client, user_text)
    print("ANSWER: ")
    print(" ".join(response))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='AskMeAnything')
    parser.add_argument('--apikey', required=True, help='apikey for openAI')

    args = parser.parse_args()

    main(args)

    