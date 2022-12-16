## This is the version of txt-2-mp3.py to be run in GitHub actions

import sys
import os
import rich_click as click
from gtts import gTTS
import ntpath
import time
import docx2txt

# without this, pygame prints a header in the console
import contextlib

with contextlib.redirect_stdout(None):
    import pygame

# main function
def create_mp3(txt_filepath, accent, mp3_base_path):
    docx_filepath = txt_filepath.replace('docx', 'txt')
      # strip filename from filepath
#     new_file_name = str(os.path.basename(docx_filepath).rsplit('.', 1)[0])
#     new_file_name = docx_filepath.replace('docx', 'txt')
    try:
        MY_TEXT = docx2txt.process(txt_filepath)
        with open(docx_filepath, "w", encoding='latin-1"') as text_file:
            print(MY_TEXT, file=text_file)   

    # handle exception (exits program)
    except FileNotFoundError:
        print(
            "\n\nERROR\n\nA file named '{}' does not exist. Please try again.\n\n".format(
                text_file
            )
        )

    try:

            # open and read .txt file
            
        with open(docx_filepath, 'r', encoding='latin-1"') as f:
            the_text = f.read()

            # conversion magic
            mp3 = gTTS(the_text, lang="en", tld=accent)

            # strip filename from filepath
            file_name = str(os.path.basename(docx_filepath).rsplit('.', 1)[0])

            # strip file type extension from name
    #             file_name = (
    #                 file_name.replace(".txt", "")
    #             )
            # save mp3
            mp3_filename = mp3_base_path + '/mp3s/' + file_name 

            # if mp3 file exists, add a number at the end, but before '.mp3'
            for i in range(1,6):
                if os.path.exists(mp3_filename + '.mp3'):
                    mp3_filename = mp3_filename + '-' + str(i)
            mp3_filename += '.mp3'

            #save mp3
            mp3.save(mp3_filename)

            # Alert use of success and location of mp3
            click.secho(
                f"\n\nAn MP3 file named '{file_name}' created.\n\n",
                fg="green",
            )

    # handle exception
    except Exception:
        pass
    
    
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
    
    #handle multiple .txt files added or modified
    for each_file in the_filename.split(','):
        each_file = "./" + each_file
    
        #strip the filename and get the path where the file changed
        mp3_base_path = os.path.dirname(each_file)
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
