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
        text_file,
        accent,
        mp3_base_path
    ):
        self.text_file = file
        self.mp3_base_path = mp3_base_path
        self.accent = accent

    # main function
    def create_mp3(self):
        language = "en"
        # load text, convert to mp3, save file and play sample for user
        try:
            with open(self.text_file) as f:
                the_text = f.read()
                # conversion magic
                mp3 = gTTS(the_text, lang=language, tld=self.accent)
                # strip filename from filepath
                file_name = ntpath.basename(self.text_file)
                # strip file type extension from name
                file_name = (
                    file_name.replace(".txt", "").replace(".md", "")
                )
                # save mp3
                mp3.save(mp3_base_path + '/mp3s/' + file_name + '.mp3')
                # Alert use of success and location of mp3
                click.secho(
                    f"\n\nMP3 file created at {self.mp3_base_path}/mp3s/{file_name}.mp3\n\n",
                    fg="green",
                )
        # handle exception (exits program)
        except FileNotFoundError:
            print(
                "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(
                    self.path
                )
            )

# Call main class and function
def cli(text_file, accent, mp3_base_path):
    invoke_class = GetAudio(path, accent, mp3_base_path)
    invoke_class.create_mp3()


if __name__ == "__main__":
    #import environmental variable from the GitHub actions workflow
    # get the file that changed and strip the brackets and quotes
    the_filename = "./" + (os.getenv('TEST_VAR').replace('[','').replace(']','').replace('"',''))
    #strip the filename and get the path where the file changed
    mp3_base_path = os.path.dirname(os.path.abspath(the_filename))
    #run the program with the file, American accent and path
    cli(the_filename, "com", mp3_base_path)

