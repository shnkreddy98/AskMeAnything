from openai import OpenAI

def speechToText(filename, apikey):
    
    client = OpenAI(api_key=apikey)

    audio_file= open(filename, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print("Transcribing...")
    
    user_text = transcription.text

    print("QUESTION: ",user_text)

    return client, user_text