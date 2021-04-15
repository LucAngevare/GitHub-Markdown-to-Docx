# GitHub-Markdown-to-Docx

Need to convert all the markdown files in a GitHub repository to Docx? I got ya covered!

## Usage

For normal usage just type `python3 main.py`, for CLI usage, use 

```python3 main.py --repo [repository name] --markdown [y/n] (if y --markdownFile [fileName]) --push [y/n]```

So to summarize: all the questions you would get asked normally can be merged into flags; see main.py (lines 16-20) for more information on which flags are required and which aren't

## Why?

I use [StackEdit.io](https://github.com/benweet/stackedit) for summaries for school (because GFM is hot), which allows me to upload the markdown files onto a private GitHub repository. Sadly, converting markdown to a different file format and downloading or uploading it to one of the options is a premium feature and they do not have a way to download or view the files from their service automatically (see: [my issue](https://github.com/benweet/stackedit/issues/1711)). Therefore, I decided to put my Python skills to the test after a while of programming in it and see whether or not I'm able to convert all or certain markdown files in a GitHub repository and pack them in a ZIP file or push them back onto the repository.

## How?

I'm using mostly simple `bash` commands: `cd`, `mv`, `cp`, `git` and `pandoc` along with one "script" to not have the output of "Can't remove folder: Directory does not exist" or "Can't create folder: Directory already exists" (with files inside) every time the program gets de-synced;

```
if [ -d "docxFiles" ]; then rm -Rf "docxFiles"; fi && mkdir docxFiles
```

This simply checks whether the directory path exists, if it does it deletes it and creates a new directory under the same name. If it doesn't, it just creates the new directory and that's it.

For the rest it really just consists out of for loops and `input` variables. It really is just a case of spending hours to automate a task that'd take 5 minutes in total to do manually.

#### Editor's note: With very minimal effort and changes (changing the `input`s for beauty purposes and changing line 22), this isn't only usable with GitHub, but rather any git service (perhaps just the git client itself)!