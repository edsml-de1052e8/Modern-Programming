# Command Line & Github

- pwd: see what directory you're in
- cd: change working directory
- git clone: to clone git repo
- git push: push changes to git, after committing
- git diff: looks at differences between branches
- git status: to see where you are in terminal and if there are any changes

-a : applies commit to all files in repo
-m: stands for message
 - git remote -v:
- git branch: to check what branch you're in
- git checkout -b new feature: switched to a new branch called 'new feature'
- git commit -a -m "commit message"

To merge branches: "button should appear on Git on commit and pull request" can also add comments

Other Tool:
BitBucket: create repo, version control for teams.

vim editor: to add file to repo using command line eg. vim "sqrt.py" (filename)
To exit from terminal, press escape (insert button should disappear), :w to save text and :q then hit enter to leave.

If you're branching, make sure you are pulling everything to make sure you're building on the right data then make a separate branch and start editing and later committing and pushing.

To merge branches: 

- Work on your secondary branch
- git rebase main : to merge branches, if there is an issue, might need to push new files or edit them
- git rebase --continue
- then edits should show in the pull requests and appear green to say it is possible to merge them, and that there are no conflicts.
