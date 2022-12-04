## This is the version of txt-2-mp3.py to be run in GitHub actions

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

# main function
def create_mp3(text_file, accent, mp3_base_path):
    language = "en"
    
    # load text, convert to mp3, save file and play sample for user
    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            the_text = f.read()
            
            # conversion magic
            mp3 = gTTS(the_text, lang=language, tld=accent)
            
            # strip filename from filepath
            file_name = str(os.path.basename(text_file).rsplit('.', 1)[0])

            # strip file type extension from name
            file_name = (
                file_name.replace(".txt", "")
            )
            # save mp3
            mp3_filename = mp3_base_path + '/mp3s/' + file_name + '.mp3'
            mp3.save(mp3_filename)
            
            # Alert use of success and location of mp3
            click.secho(
                f"\n\nAn MP3 file named '{file_name}' created.\n\n",
                fg="green",
            )
            
    # handle exception (exits program)
    except FileNotFoundError:
        print(
            "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(
                text_file
            )
        )

if __name__ == "__main__":
   
    #import environmental variable from the GitHub actions workflow
    # get the file that changed or was added and strip the brackets and quotes
    the_modified_filename = (os.getenv('MODIFIED_FILE').replace('[','').replace(']','').replace('"',''))
    the_added_filename = (os.getenv('ADDED_FILE').replace('[','').replace(']','').replace('"',''))
    
    #compare to see if a file was added or modified, keep the one which is not './'
    if len(the_modified_filename) > len(the_added_filename):
        the_filename = the_modified_filename
    else:
        the_filename = the_added_filename
    the_filename = str(the_filename)
    print(f"the filename is {the_filename}")
    
    for each_file in the_filename.split(','):
        each_file = "./" + each_file
    
        #strip the filename and get the path where the file changed
        mp3_base_path = os.path.dirname(each_file)
    #     mp3_base_path = os.path.dirname(os.path.abspath(the_filename))
        mp3_base_path = str(mp3_base_path)
        print(f"the mp3_base_path is {mp3_base_path}")

        # if the 'mp3s' directory does not exist, create it
        if not os.path.exists(mp3_base_path + '/mp3s/'):
            os.makedirs(mp3_base_path + '/mp3s/')
            time.sleep(3)

        #run the program with the file, American accent and path

        create_mp3(each_file, "com", mp3_base_path)

#     #Debuggging
#     print(f"the mp3_base_path is {mp3_base_path}")
#     print(f"the TMODIFIED_FILE is {os.getenv('MODIFIED_FILE')}")
#     print(type(the_filename))
#     print(f"the filename is {the_filename} and it is type {type(the_filename)}")
#     print(type(mp3_base_path))
