### git

1. Install  
	`$ sudo apt install git`
2. Initial　　　　　　　--> ~/.gitconfig  
	`$ git help tutorial`  
	> $ git config --global user.name "MornSun"  
	> $ git config --global user.email "chenkl1995@gmail.com"  
	> $ git config --global core.editor vim  
	> 
	> git config --system　　　　--> etc/gitconfig  
	> git config --global　　　　 --> ~/.gitconfig ~/.config/git/config  
	> git config　　　　　　　　 --> .git/config  
	> 
	> git config --list
	> git config <key>　`git config user.name`
	> 
	> git help \<verb>　　　　　 `git help config`  
	> git <verb> --help  
	> man git-\<verb>  
6. Remote Repository
	> $ ls ~/.ssh/id_rsa ~/.ssh/id_rsa.pub  
	> $ ssh-keygen -t rsa -C "chenkl1995@gmail.com"  
3. New Repository　　　--> ./.git/
	> $ cd \<Repository Dir\>  
	> $ git init  
	> $ git add \<file> / . / readme.txt　　　　　　-- 添加文件到 暂存区  
	> $ git commit [-m "\<commit message>"]　　-- 把 暂存区 提交到 当前分支  
	> $ git rm \<file>  
4. Make Changes
	> $ git status  
	> $ git diff \<file> / readme.txt  
	> $ git diff HEAD -- readme.txt　　　　　　　-- 比较 工作区 和 版本库最新版本 的 区别  
	> $ git checkout -- \<file> / readme.txt　　　　-- 丢弃 工作区 的 修改, 可用于恢复误删  
	> $ git reset HEAD \<file> /readme.txt　　　　-- 丢弃 暂存区 的 修改, 返回到工作区   
5. Version Control
	* HEAD		-- current version
	* HEAD^		-- last version
	* HEAD^^	-- 2 before
	* HEAD~100	-- 100 before
	> $ git log [--pretty=oneline]　　　　　　　-- for previous version  
	> $ git reset --hard \<commit_id> / HEAD^  
	> $ git reflog　　　　　　　　　　　　　　-- for future version  
7. Local 2 Remote
	> $ cd \<Repository Dir\>  
	> $ git remote add origin git@github.com:chenkl1995/\<repo name\>.git  
	> $ git remote add origin https://github.com/chenkl1995/<repo name\>.git  
	> $ git remote -v  
	> $ git push -u origin master　　　　　　　-- 1st push  
	> $ git push origin master　　　　　　　　-- later push  
	> $ git clone git@github.com:chenkl1995/help.git  
	> $ git clone https://github.com/chenkl1995/help.git  
	> $ git pull  
8. Branch
	> $ git branch  
	> $ git branch \<branch name>  
	> $ git checkout \<branch name>  
	> $ git checkout -b \<branch name>　　　<==>　　　git branch dev && git checkout dev  
	> $ git merge \<branch name>  
	> $ git branch -d \<branch name>    
	> $ git branch -D \<branch name>　　　　-- 丢弃一个没有被合并过的分支  
	> $ git log --graph　　　　　　　　　　　-- 查看分支合并图  
	> $ git merge --no-ff -m "\<merge message>" \<branch name>　　-- no `Fast forward`
9. Stash -- bug branch
	> $ git stash　　　　　　　　　　　-- 保存工作现场  
	> $ git stash list  
	> $ git stash apply  
	> $ git stash drop  
	> $ git stash pop　　　<==>　　　git stash apply && git stash drop  

10. Ignore
	* [https://github.com/github/gitignore](https://github.com/github/gitignore)
	> $ touch .gitignore  
	> $ echo "\<ignore>"  > .gitignore  
	> $ git add -f \<SomeAreIgnoredByGitignore>  
	> $ git check-ignore -v \<SomeAreIgnoredByGitignore>  


<br /><br /><br />
- Reference  
	* [Git Introduction Translation in CSDN](https://blog.csdn.net/hudashi/article/details/7661198)  
	* [Git by liaoxuefeng](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)  

<br /><br />
- [Only clone a subdir of a repo](https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository)
	 
	> $ mkdir \<repo>  
	> $ cd \<repo>  
	> $ git init  
	> $ git remote add -f origin \<url>  
	> 
	> $ git config core.sparseCheckout true  
	> 
	> $ echo "some/dir/" >> .git/info/sparse-checkout  
	> $ echo "another/sub/tree" >> .git/info/sparse-checkout   
	> 
	> $ git pull origin master  
