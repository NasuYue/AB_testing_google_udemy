
### 1. Introduction to Version Control Systems

```console
/home/dq$ git init random_numbers
Initialized empty Git repository in /home/dq/random_numbers/.git/
```

### 2. The .Git Folder

```console
/home/dq$ cd random_numbers/
/home/dq/random_numbers$ ls -al
total 16
drwxr-xr-x 3 dq dq 4096 Oct 13 10:20 .
drwxr-xr-x 1 dq dq 4096 Oct 13 10:20 ..
drwxr-xr-x 7 dq dq 4096 Oct 13 10:20 .git
```

### 3. Creating Files in the Repository

```console
/home/dq/random_numbers$ echo -e "Random number generator" > README.md
/home/dq/random_numbers$ echo -e "if __name__ == "__main__":\n\tprint("10")" > script.py
```

### 4. Checking File Status

Three states in Git:
- `committed` - The current version of the file has been added to a commit, and Git has stored it.
- `staged` - The file has been marked for inclusion in the next commit, but hasn't been committed yet (and Git hasn't stored it yet). You might stage one file before working on a second file, for example, then commit both files at the same time when you're done.
- `modified` - The file has been modified since the last commit, but isn't staged yet.

Instructions
1. Check the status of the repo.
2. Add script.py to the staging area.
3. Add README.md to the staging area.

```console
/home/dq/random_numbers$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md
        script.py

nothing added to commit but untracked files present (use "git add" to track)
/home/dq/random_numbers$ git add script.py 
/home/dq/random_numbers$ git add README.md 
/home/dq/random_numbers$ git add README.md 
```

### 5. Configuring Identity in Git

```console
/home/dq/random_numbers$ git config --global user.email "wade@dataquest.io"
/home/dq/random_numbers$ git config --global user.name "Dataquest user"
```


### 6. Committing Changes
```console
/home/dq/random_numbers$ git commit -m "Initial commit. Added script.py and README.md"
[master (root-commit) e5c9dd3] Initial commit. Added script.py and README.md
 2 files changed, 3 insertions(+)
 create mode 100644 README.md
 create mode 100644 script.py
 ```

 ### 7. Viewing File Differences
1. Edit script.py for random 0-10
2. Check git status
3. Check git diff

 ```console
 /home/dq/random_numbers$ echo -e 'import random\nif __name__ == "__main__":\n    print(random.randint(0,10))' > script.py
/home/dq/random_numbers$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   script.py

no changes added to commit (use "git add" and/or "git commit -a")
/home/dq/random_numbers$ git diff
diff --git a/script.py b/script.py
index 9bf7d31..0262b9d 100644
--- a/script.py
+++ b/script.py
@@ -1,2 +1,3 @@
+import random
 if __name__ == "__main__":
-    print("10")
+    print(random.randint(0,10)) 
 ```

### 8. Making a Second Commit
1. Add changes to staging 
2. commit

```console
/home/dq/random_numbers$ git add script.py 
/home/dq/random_numbers$ git commit
```


### 9. Reviewing the Commit History

```console
/home/dq/random_numbers$ git log
commit 022b85fe0864753385fca576186e1544aef5376c
Author: Dataquest User <user@dataquest.io>
Date:   Thu Oct 13 10:44:28 2022 +0000

    Initial commit.  Added script.py and README.md
```


### 10. Viewing Commit Differences
```console
/home/dq/random_numbers$ git log --stat
commit 022b85fe0864753385fca576186e1544aef5376c
Author: Dataquest User <user@dataquest.io>
Date:   Thu Oct 13 10:44:28 2022 +0000

    Initial commit.  Added script.py and README.md

 README.md | 1 +
 script.py | 2 ++
 2 files changed, 3 insertions(+)
/home/dq/random_numbers$ 
```