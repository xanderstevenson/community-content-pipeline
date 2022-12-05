<img src="https://github.com/xanderstevenson/community-content-pipeline/blob/main/media/community-content-pipeline-black.png?raw=true" width=250) />

## A Source of Truth for  the Cisco Community Engagement Content Calendar, with creation and storage of .txt and MP3 files, as well as integration with Asana.


### Step 1


Write your post. If needed, download the [post template](https://github.com/xanderstevenson/community-content-pipeline/blob/main/community-post-template.docx) and adjust as necessary. Use Spelling and Grammar check, under the Review tab, in Word or do the same in another text editor

<img src="https://github.com/xanderstevenson/community-content-pipeline/blob/main/media/Word-Check.png?raw=true" width=800) />


### Step 2

A colleague moderator can review the document. A good tool to use, when the document is online, in this repo, in the Community as a draft, etc., is the Grammar & Spell Checker — LanguageTool extension for the browser to check for spelling and grammar
https://chrome.google.com/webstore/detail/grammar-spell-checker-%E2%80%94-l/oldceeleldhonbafppcapldpdifcinji?hl=en-US

If changes need to be made, the moderator will make the changes or the writer will make the changes themself. 


### Step 3


Once all the edits are finished, find the [directory](https://github.com/xanderstevenson/community-content-pipeline/tree/main/developer-hub) where your article/blog will be, create a folder, add your post, in docx or similar format and commit it, checking 'Create a new branch for this commit and start a pull request.' The temporary branch, with 'patch' in the name is automatically generated for you.



### Step 4

Now you want to create an MP3 from the post and attach it to the post. There are 3 ways to do this.

* With either step, you'll need to create a .txt file and paste in your post. Remove all URLs, links and any other long strings or numbintegration with Asanaers, which will not sound good while read out loud. Also, in order to attach your MP3 to the blog post or article, you will need to compress it into a ZIP file.


1. Use [txt_2_mp3](https://github.com/xanderstevenson/txt_2_mp3) - this will give you more control over the accent you want. When it's finished, upload the MP3 to your project folder in the this repo, under developer-hub and don't forget to attach it to your blog/article on the community.

2. If you save your .txt file in your project folder in developer-hub, it will automatically create an 'mp3s' folder in that directory, create your MP3 from the text and place it in there. It will also handle the pull-request/commit for you, so you don't have to worry about that. Now, just download the MP3 and attach it to your blog or article post on the Cisco Community.

3. Use an online text to MP3 converter and attach the results to you post. Attach it to your blog/article on the Community.



### Step 5

The Commit to main will notify those on the mailing list and and close the Asana task.




