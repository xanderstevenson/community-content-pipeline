## This is the version of text-2-mp3.py to be run in GitHub actions


import sys
import os
import rich_click as click
from gtts import gTTS
import ntpath
import time

# without this, pygame prints a header in the console
import contextlib

with contextlib.redirect_stdout(None):
    import pygame

# main class
class GetAudio:
    def __init__(
        self,
        path,
        accent,
    ):
        self.path = path
        # function to assign accent code based on numerical choice
        def match_accent(accent):
            match accent:
                case "1":
                    return "com.au"
                case "2":
                    return "co.uk"
                case "3":
                    return "com"
                case "4":
                    return "ca"
                case "5":
                    return "co.in"
                case "6":
                    return "ie"
                case "7":
                    return "co.za"
                case _:
                    return "com"

        self.accent = match_accent(accent)

    # main function
    def create_mp3(self):
        language = "en"
        # load text, convert to mp3, save file and play sample for user
        try:
            with open(self.path) as f:
                the_text = f.read()
                # conversion magic
                mp3 = gTTS(the_text, lang=language, tld=self.accent)
                # strip filename from filepath
                file_name = ntpath.basename(self.path)
                # strip file type extension from name
                file_name = (
                    file_name.replace(".txt", "").replace(".md", "")
                )
                # save mp3
                mp3_folder = '\\'.join(file_name.split('\\')[0:-1])
                mp3.save(f"{mp3_folder}/mp3s/{file_name}.mp3")
                # Alert use of success and location of mp3
                click.secho(
                    f"\n\nMP3 file created at { sys.path[0] }/mp3s/{file_name}.mp3\n\n",
                    fg="green",
                )
#                 # Automatically play audio sample and alert user
#                 pygame.mixer.init()  # initialize mixer module
#                 pygame.mixer.music.load(f"{ sys.path[0] }/mp3s/{file_name}.mp3")
#                 pygame.mixer.music.play()
#                 print("Audio sample will play for 3 seconds\n\n")
#                 time.sleep(3)
        # handle exception (exits program)
        except FileNotFoundError:
            print(
                "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(
                    self.path
                )
            )


# # Prompt user for file input, store as 'path'
# @click.command()
# @click.option(
#     "--path",
#     prompt="\n\nWELCOME to TEXT-2-MP3\n\nEnter the path of the file to convert text to speech (.txt, .rtf or .md)\n\n",
#     help="Enter the path of the file to convert text to speech (.txt, .rtf or .md)",
#     required=True,
# )
# # Prompt user for accent input, store as 'accent'
# @click.option(
#     "--accent",
#     prompt="\nPlease choose an English accent (type a number and hit ENTER)\n\n\
#         1. English (Australia)\n\
#         2. English (United Kingdom)\n\
#         3. English (United States)\n\
#         4. English (Canada)\n\
#         5. English (India)\n\
#         6. English (Ireland)\n\
#         7. English (South Africa)\n\n",
#     help="Please choose an English accent",
#     required=True,
# )


# Call main class and function
def cli(path, accent):
    invoke_class = GetAudio(path, accent)
    invoke_class.create_mp3()


if __name__ == "__main__":
    #import environmental variable from the GitHub actions workflow
    # strip the brackets and quotes
    the_filename = "./" + os.getenv('TEST_VAR').replace('[','').replace(']','').replace('"','')
    #run the program with the file and 3 for American accent
    cli(the_filename, 3)
    print(f"the file name is {the_filename}")
