# FASDH25
A repository for the Text-Based Digital Humanities course

## contents

```
|- test_commit/    folder for a first git exercise: add and commit a file here
|- meta/           contains a tsv export from the metadata spreadsheet
|- mARkdown/       contains the exported OCR'ed texts in OpenITI mARkdown format
|- README.md       this file
|- .gitignore      tells git which files and folders not to commit
|- convert_escriptorium_exports.py    
|                  script that converts eScriptorium exports to OpenITI mARkdown format
|- check_empty_pages.py
|                  script that checks how many pages are empty in an OpenITI text file
```

## commit exercise:

**Before you make this exercise**, make sure that you have correctly configured git on your computer: 

Run this command in Git Bash / Terminal: 

`git config --list`

If the output does not contain your email address, please provide your GitHub user name and the email address you made your GitHub account with by running the following two commands in Git Bash/Terminal:

```
git config --global user.name "your_github_username"
$ git config --global user.email "your_email_address"
```

-----

After this, start the exercise:

Clone this repository and make your first commit. Commands (to execute in Git Bash / Terminal): 

1. `cd ~/Downloads` (move into your Downloads folder, which is in your home directory `~`)
2. `git clone https://github.com/OpenITI/FASDH25.git`
3. `cd FASDH25`  (to move into the downloaded folder)
4. (In Kate editor, create a new file and save it to the test_commit folder in the FASDH25 folder in your downloads folder. Give the file this name: {FirstName}.{GroupName}.txt (leave out the curly braces and use your own name and group name!))
5. `git add .` (prepare to save your changes to git)
6. `git commit -m "your message"` (save your changes to the local repository in your Downloads folder; replace "your message" with a message that describes what you did)
7. `git pull` (download any recent changes in the remote (= online) the repository, on GitHub)
8. `git push` (push your changes to the remote repository)
9. (if this is the first time you're pushing something to GitHub, a browser window will open that asks you to authenticate with your GitHub username and password)
