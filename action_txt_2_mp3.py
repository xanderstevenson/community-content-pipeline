#!/usr/bin/env python3
"""
This is the version of txt-2-mp3.py to be run in GitHub actions
"""

import os
import re
import time
import rich_click as click
from gtts import gTTS
import docx2txt


# main function
def create_mp3(docx_filepath, accent, mp3_base_path):
    """take a docx and convert to txt, saving the docx and txt to new dorectory we create"""
    # rename docx to text
    txt_filepath = docx_filepath.replace('docx', 'txt')
    # get the filename of the document
    file_name = str(os.path.basename(txt_filepath).rsplit(".", 1)[0])
    file_name = file_name.replace(" ", "-")
    txt_dirname = mp3_base_path + f"/{file_name}/"
    if not os.path.exists(txt_dirname):
        os.makedirs(txt_dirname)
        time.sleep(1)
    # cp docx file into new dir
    new_docx = txt_dirname  + f"{file_name}.docx"
    os.system(f"cp {docx_filepath} {new_docx}")
    # make name for new txt file
    txt_file = txt_dirname + f"{file_name}.txt"
    try:
        # convert docx to txt
        my_text = docx2txt.process(docx_filepath)
        # remove all URLs from text
        my_text = re.sub(r"http\S+", "", my_text)
        # create and write text to txt file
        with open(txt_file, "w") as text_file:
            print(my_text, file=text_file)
        #remove original docx
        os.remove(docx_filepath)
    ### removing empty lines
        # Read lines as a list
        workable_txt = open(txt_file, "r")
        lines = workable_txt.readlines()
        workable_txt.close()
        # Weed out blank lines with filter
        lines = filter(lambda x: not x.isspace(), lines)
        # Write
        workable_txt = open(txt_file, "w")
        workable_txt.write("".join(lines))
        # should also work instead of joining the list:
        # workable_txt.writelines(lines)
        workable_txt.close()
    ###

    # handle exception (exits program)
    except FileNotFoundError:
        print(
            f"\n\nERROR\n\nA file named {txt_filepath} does not exist. Please try again.\n\n"
            )

    try:

        # open and read .txt file
        with open(txt_file, 'r') as f:
            the_text = f.read()

            # conversion to MP3
            mp3 = gTTS(the_text, lang="en", tld=accent)

            # strip filename from filepath
            file_name = str(os.path.basename(txt_file).rsplit('.', 1)[0])

            # if the 'mp3s' directory does not exist, create it
            if not os.path.exists(txt_dirname + '/mp3s/'):
                os.makedirs(txt_dirname + '/mp3s/')
                time.sleep(3)

            # save mp3
            mp3_filename = txt_dirname + '/mp3s/' + file_name

            # if mp3 file exists, add a number at the end, but before '.mp3'
#             for i in range(1,6):
#                 if os.path.exists(mp3_filename + '.mp3'):
#                     mp3_filename = mp3_filename + '-' + str(i)
            mp3_filename += '.mp3'

            #save mp3
            mp3.save(mp3_filename)

            # Alert use of success and location of mp3
            click.secho(
                f"\n\nAn MP3 file named '{file_name}' created.\n\n",
                fg="green",
            )

    # handle exception - sometimes the gTTS works and retuned a 200 but it's interpreted as an error
    except Exception:
        pass


if __name__ == "__main__":
    #import environmental variable from the GitHub actions workflow
    # get the file that changed or was added and strip the brackets and quotes
    the_modified_filename = os.getenv('MODIFIED_FILE')
    the_modified_filename = the_modified_filename.replace('[','').replace(']','').replace('"','')
    the_added_filename = os.getenv('ADDED_FILE')
    the_added_filename = the_added_filename.replace('[','').replace(']','').replace('"','')

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
        base_path = os.path.dirname(each_file)
        base_path = str(base_path)
        print(f"the mp3_base_path is {base_path}")



        #run the program with the file, American accent and path
        create_mp3(each_file, "com", base_path)

#     #Debuggging
#     print(f"the mp3_base_path is {base_path}")
#     print(f"the TMODIFIED_FILE is {os.getenv('MODIFIED_FILE')}")
#     print(type(the_filename))
#     print(f"the filename is {the_filename} and it is type {type(the_filename)}")
#     print(type(base_path))
