Luna: Personal assistant


Luna is my attempt at creating my smart personal assistant.

## Setup:

Luna uses the OpenAI and it requires you setup your `OPENAI_API_KEY` as an environment variable ([see OpenAI article](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)).


```shell
export OPENAI_API_KEY="your-openai-key"

```

Other requirements can be installed via Conda. Create the Conda environment using the following command:
```shell
conda env create --name luna --file=conda/luna.yml
conda activate luna
```

## [Whisper requirements](https://github.com/openai/whisper/blob/3e1780fd37686666f568be9c99f5b5e3e4f2eb92/README.md#setup):
Luna uses Whisper which require `ffmpeg`.
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg
```


## Usage:

```shell
./luna.py --help
usage: luna.py [-h] [-d AUDIO_DEVICE] [-p PROMPT_SECONDS] [-i INTRO_SECONDS]

options:
  -h, --help            show this help message and exit
  -d AUDIO_DEVICE, --audio-device AUDIO_DEVICE
                        Index of the audio device that Luna will listen to.
  -p PROMPT_SECONDS, --prompt-seconds PROMPT_SECONDS
                        How long (in seconds) will Luna keep listening for
                        questions.
  -i INTRO_SECONDS, --intro-seconds INTRO_SECONDS
                        How long (in seconds) will Luna wait for "Hello
                        Luna!".

```
Please note that once the script runs, **Luna will always be listening and recording all audio**. All recorded audio will be converted to text, then an answer to the question will be displayed in the command line. Luna will send ALL recordings to OpenAI and Whisper inference models. Recordings will be stored to disk but overwritten regularly. You are responsible for your own privacy and following OpenAI terms of services.

Example conversation:

```shell
Listening....
You:   Hello Luna.
Starting conversation with Luna..
Listening....
Transcribing....
You:  Hey Luna, can you recommend a movie for me to watch?
Luna:

That's a tough one! It really depends on what kind of movies you like. 
If you don't have any particular genre in mind, I'd recommend trying out the movie "Inside Out" 
or the Netflix original movie "The Kissing Booth" for a good laugh.
Listening....
Transcribing....
Listening....
Transcribing....
You:  Hey Luna, who starts Inside Out?
Luna:

The main characters of Inside Out are voiced by Amy Poehler,
Phyllis Smith, Bill Hader, Lewis Black, Mindy Kaling, and Richard Kind.
Listening....
Transcribing....
You:  Luna, where can I watch inside out?
Luna:

You can watch Inside Out on Disney+, Netflix, Amazon Prime Video, and YouTube.
Listening....
Transcribing....
You:  Bye, Luna.

```

# License
See [LICENSE](LICENSE) for the python file License.

- [Whisper](https://github.com/openai/whisper/blob/3e1780fd37686666f568be9c99f5b5e3e4f2eb92/README.md#license)

