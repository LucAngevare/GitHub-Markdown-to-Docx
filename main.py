import os, sys
from zipfile import ZipFile

obj = {}

if len(sys.argv) >= 6:
    for i in range(len(sys.argv)):
        if sys.argv[i].startswith("--"):
            obj[sys.argv[i].replace("--", "")] = sys.argv[i + 1]
            i + 1
        else:
            continue
else:
    print("Not enough arguments provided. Defaulting to script instead of CLI form.")
    obj.clear()
    obj["repo"] = input("Which repo would you like to extract the markdown from? >>>   ")
    obj["markdown"] = input("Defined markdown file? (y/n) >>>    ")
    if ((obj["markdown"].lower() == "y") or (obj["markdown"].lower() == "yes")):
        obj["markdownFile"] = input("Filename? >>>    ")
    obj["push"] = input("Want to push to GitHub? (y/n) >>>    ")

os.system("git clone \"https://github.com/LucAngevare/" + obj["repo"] + ".git\"")

markdownList = []

if not hasattr(obj, "markdownFile"):
    for root, dirs, files in os.walk(os.path.join(obj["repo"])):
        for file in files:
            if (file.endswith(".md")):
                markdownList.append(os.path.join(root, file))
else:
    for root, dirs, files in os.walk(os.path.join(obj["repo"])):
        for file in files:
            if ((file == markdownFile) or (file == "{markdownFile}.md")):
                markdownList.append(os.path.join(root, file))

print("These files will be printed: " + ", ".join(markdownList))

os.system("if [ -d \"docxFiles\" ]; then rm -Rf \"docxFiles\"; fi && mkdir docxFiles")
for file in markdownList:
    os.system("pandoc --from gfm+tex_math_dollars --to docx \"" + file +"\" -o \"" + file.replace(".md", ".docx") + "\"")
    os.system("mv " + "\"/".join([file.replace(file.split("/")[-1], ""), file.split("/")[-1].replace(".md", ".docx")]) + "\" \"./docxFiles/" + file.split("/")[-1].replace(".md", ".docx") + "\"")

if (obj["push"].lower() == "y") or (obj["push"].lower() == "yes"):
    for file in markdownList:
        os.system("cp \"./docxFiles/" + file.split("/")[-1].replace(".md", ".docx") + "\" \"" + "/".join([file.replace(file.split("/")[-1], ""), file.split("/")[-1].replace(".md", ".docx")]) + "\"")
    os.system("cd " + repo + "/ && git add . && git commit -m \"Converted markdown to Word format! ;)\" && git push")
else:
    if (len(markdownList) > 1):
        zipObj = ZipFile('WordMarkdown.zip', 'w')
        for file in markdownList:
            zipObj.write("./docxFiles/" + file.split("/")[-1].replace(".md", ".docx"))
        print("Your ZIP file with the markdown files is ready!")
    else:
        print("{} is now in docx format!".format("".join(markdownList)))