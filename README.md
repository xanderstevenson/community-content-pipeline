<p align="center"><img src="https://github.com/xanderstevenson/community-content-pipeline/blob/main/media/community-content-pipeline-teal-transparent.png?raw=true" width=300 /></p>
<h2 align="center">A Source of Truth for  the Cisco Community Engagement, with creation and storage of Text and MP3 files.</h1>


### What this repository accomplishes

**A)** Provides a template for your blog or article and shows you how to check it for spelling and grammar errors </br>
**B)** Shows how to create a directory and upload your blog or article in .docx format </br>
**C)** An automated workflow will create a new directory based on your .docx file name. So, uploading a .docx named "UCCE Script Generation" will create a directory with the name "UCCE_Script_Generation". Automation will convert the docx to an MP3, saving it in an 'mp3s' folder in your new directory. All URLS and empty lines will have been removed, to give your audio a smooth, consistent flow. In the end, you'll have:
- A new directory named for your .docx file, inside of which will be:
  - A downloadable copy of you original .docx document
  - A readable .txt version of your document
  - A downloadable MP3, inside of an 'mp3s' sub-folder</br>

**D)** Explains the need to compress your MP3 into a ZIP in order to attach it to your article or blog </br>
**E)** Gives alternate means of generating your MP3, for more control over spoken accent. </br>

The final result is a text source of truth in the relative directory in this repo, along with an MP3. This data structure of blogs and articles serves as a record, backup and can eventually serve as an archive for artivles on the Cisco Community - Developer Hub.

---

### Step 1


Write your post. If needed, download the [post template](https://github.com/xanderstevenson/community-content-pipeline/blob/main/community-post-template.docx) and adjust as necessary. Use the Spelling and Grammar check, under the Review tab, in MS Word, or do the same in another text editor


### Step 2

A colleague moderator can review the document. A good tool to use, when the document is online, in this repo, in the Community as a draft, etc., is the Grammar & Spell Checker — LanguageTool extension for the browser to check for spelling and grammar
https://chrome.google.com/webstore/detail/grammar-spell-checker-%E2%80%94-l/oldceeleldhonbafppcapldpdifcinji?hl=en-US

If changes need to be made, the moderator will make the changes or the writer will make the changes themself. 


### Step 3


Once all the edits are finished, find the [directory](https://github.com/xanderstevenson/community-content-pipeline/tree/main/developer-hub) where your article/blog will be. 

**Upload your article or blog in .docx format**
<p align="center"><img src="https://github.com/xanderstevenson/community-content-pipeline/blob/main/media/create-file.png?raw=true" width=900 /></p>

At the bottom of the page, comment and commit to the 'main' branch. This will start a workflow to create a folder with all your files, including a sub-folder called 'mp3s', where it will place the MP3.

<p align="center"><img src="https://github.com/xanderstevenson/community-content-pipeline/blob/main/media/comment-commit.png?raw=true" width=500 /></p>

**Details:** It will create your project folder and 'mp3s' sub-folder, if they do not already exist. It will convert the .docx to .txt using the docxtotxt library, removing all images, empty lines and URLs. Then it will convert the .txt to an MP3 using gTTs. If you change your .docx and re-upload, it will overwrite the .txt and MP3. Whenever the process, is run, the .docx file you've upploaded is copied into the project folder and the original is deleted from the repo.


### Step 4



Now, just download the MP3 from the 'mp3s' folder, compress it into a ZIP file, and attach it to your blog or article post on the Cisco Community!



**In order to attach your MP3 to the blog post or article, you will need to compress it into a ZIP file.**


### Alternate ways to create your MP3.

* With either way below, don't forget to add and commit your .docx or .txt and MP3 files in the repo, to serve as backups.


1. Use [txt_2_mp3](https://github.com/xanderstevenson/txt_2_mp3) - this will give you more control over the accent you want. When it's finished, upload the MP3 to your project folder in the this repo, under developer-hub and don't forget to attach it to your blog/article on the community.

2. Use an online text to MP3 converter and attach the results to you post. Attach it to your blog/article on the Community.


**Remember to In order to attach your MP3 to the blog post or article, you will need to compress it into a ZIP file.**


