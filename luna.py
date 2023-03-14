#!/usr/bin/env python

import openai
import os
import json
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import argparse
import sys


whisper_model = whisper.load_model("small.en")

def record_command(filename='audio.mp3', seconds = 10, device = 14):
    fs = 44100
    sd.default.device = device
    audio_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio_recording)

def transcribe(filename='audio.mp3'):
    result = whisper_model.transcribe(filename)
    return result["text"]

def ask_luna(text):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.7,
    max_tokens=1024,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    return response

def is_valid_prompt(prompt):
    prompt=prompt.lower()
    if(len(prompt) < 10):
        return False
    return ("luna" in prompt) or ("Luna" in prompt)

def is_hello(prompt):
    prompt=prompt.lower()
    return ("hello" in prompt) or ("hi" in prompt)

def is_bye(prompt):
    prompt=prompt.lower()
    return ("bye" in prompt)


def start_convo(prompt_seconds = 10, device = 14):
    print("Starting conversation with Luna..")

    while(True):
        filename='audio.mp3'
        print("Listening....")
        record_command(filename=filename, seconds=prompt_seconds, device=device)
        print("Transcribing....")
        text = transcribe(filename=filename)
        if (is_valid_prompt(text)):
            response = ask_luna(text=text)
            json_object = json.loads(str(response))
            response_str = json_object['choices'][0]['text']
            print('You:', text)
            print('Luna:', response_str)
        elif(is_bye(text)):
            print('You:', text)
            sys.exit()


def main():

    openai.api_key = os.getenv("OPENAI_API_KEY")

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--audio-device', default=14, type=int,
                         help='Index of the audio device that Luna will listen to.')
    parser.add_argument('-p', '--prompt-seconds', default=10, type=int,
                         help='How long (in seconds) will Luna keep listening for questions.')
    parser.add_argument('-i', '--intro-seconds', default=5, type=int,
                         help='How long (in seconds) will Luna wait for "Hello Luna!".')
    args = parser.parse_args()


    filename='audio.mp3'
    while(True):
        print("Listening....")
        record_command(filename=filename, seconds = args.intro_seconds, device=args.audio_device)
        prompt = str(transcribe(filename=filename))
        print("You: ", prompt)
        if(is_valid_prompt(prompt=prompt) and is_hello(prompt=prompt)):
            start_convo(prompt_seconds = args.prompt_seconds, device=args.audio_device)
        elif(is_bye(prompt)):
            break
        else:
            print(prompt)

if __name__ == "__main__":
    main()
