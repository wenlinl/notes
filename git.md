Github使用教程-黑马程序员 https://www.bilibili.com/video/BV1st411r7Sj?spm_id_from=333.788.videopod.episodes&vd_source=a2b94abb30c6e58f1774bbf718480c2b&p=2

git version

Pull Request

Working Directory
Index
Git Repository

initialise the user info:
git config --global use.name 'github username'
git config --global user.name 'github email'
git config --list

initialise the git:
cd test
git init 
git status

add file to index:
git add test.py
git add .

add file to repository:
git commit -m "description"
git commit
a/i
esc
:wq(write&quit)
enter

remove the file from working repository:
rm test.py

remove the file from git repository:
git rm test.py

copy the online repository to local:
git clone repository URL

update the local file to online git repository:
git push 

git log

return to certain version:
git reset --hard gitId 

copy current version to branch:
git checkout 0.2
git checkout master
git merge

create branch main and add local file to online repository
git branch -M main
git remote add origin onlineRepositoryUrl
git push -u origin main

fork other repository, change and pull request to other repostiroy
folk
git clone myRepositoryUrl
git remote -v
git remote add upstream othersRepositoryUrl
git checkout -b newbranch
git add.
git commit -m "description"
git push -u origin newbranch
pull request 

if push fail due to version reason
git ferch upstream
git merge upstream/main
git push
VSCode:Git History Diff
