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
	![lifecycle](https://git-scm.com/book/en/v2/images/lifecycle.png)
	* File LifeCycle
		1. Tracked  
			1. Un-modified  
			2. Modified　`M`  
			3. Staged　　`A`    
		2. Un-Traked　　 `??`  
	> 
	> $ git clone \<URL by https/git/ssh> [DirName]
	> $ git clone git@github.com:chenkl1995/help.git  
	> $ git clone https://github.com/chenkl1995/help.git 
	> 
	> $ cd \<RepoDir>  
	> $ git init  
	> $ git add \<files> / `.` / `readme.txt`　　　　　　 -- 添加文件到 暂存区(`Add the file`, `Stage the file`)  
	> $ git commit [-m "\<Commit Msg>"]　　　　　　-- 把 暂存区 提交到 当前分支(`Commit`)  
	> 
	> $ git commit -a [-m "\<Commit Msg>"]　　　　　-- 跳过 暂存区(不用git add)  
	> $ git commit --amend　　　　　　　　　　　　-- 修正提交(覆盖提交信息, 添加提交文件)  
	> $ git rm \<file>　　　　　　　　　　　　　　　　-- 从 工作目录 和 暂存区 移除(从 已跟踪列表 移除)  
	> $ git rm --cached \<file>　　　　　　　　　　　 -- 保留文件在 工作目录 但从 暂存区 移除  
	> $ git mv <file_from> <file_to>　　　　　　　　  -- 重命名, <==> `mv` + `git rm` + `git add`  
4. Make Changes
	![areas](https://git-scm.com/book/en/v2/images/areas.png)
	> $ git status [-s/--short]
	> 
	> $ git diff　　　　　　　　　　　　　 -- 查看 尚未添加到 暂存区 的 变更, Working Dir VS Staging Area  
	> $ git diff -staged/-cached　　　　　　-- 查看哪些 已暂存 的内容 会进入下一次提交, Staging Area VS Repository  
	> $ git diff HEAD -- \<file> / `readme.txt`　-- 比较 工作区 和 版本库最新版本 的 区别, Working Dir VS Respository  
	> $ git diff \<file> / `readme.txt`  
	> 
	> $ git reset HEAD \<file> / `readme.txt`　　　-- 丢弃 暂存区 的 修改, 返回到工作区  
	> $ git checkout -- \<file> / readme.txt　　　　-- 丢弃 工作区 的 修改, 可用于恢复误删    
5. Version Control
	* HEAD		-- current version
	* HEAD^		-- last version
	* HEAD^^	-- 2 before
	* HEAD~100	-- 100 before
	> $ git log　　　　　　　　　　　　　　　-- for previous version  
	> 　　　　-p　　　显示每次提交所引入的差异(patch)  
	> 　　　　-stat　　查看每个提交的摘要信息  
	> 　　　　--pretty=oneline/short/full/fuller  
	> 　　　　--pretty=format:"..."　更改日志输出的默认格式  
	> 　　　　--graph　　显示ASCII图表  
	> 
	> 　　　　-N　　　只输出最近的N次提交  
	> 　　　　--since=<Time>, --until=<Time>  
	> 　　　　--author<Str>, --commiter<Str>, --grep<Str>  
	> 　　　　--S<Function Name>  
	> $ git reset --hard \<commit_id> / HEAD^  
	> $ git reflog　　　　　　　　　　　　　　-- for future version  
7. Local 2 Remote
	> $ cd \<Repo Dir\>  
	> $ git remote add <ShortName> <URL>  
	> $ git remote add origin git@github.com:chenkl1995/\<repo name\>.git  
	> $ git remote add origin https://github.com/chenkl1995/<repo name\>.git  
	> $ git remote -v  
	> 
	> $ git remote show <RemoteName>  
	> $ git remote show origin  
	> 
	> $ git pull　　　　　　　　　　　　　　　-- 自动合并入当前本地分支  
	> $ git fetch <RemoteName>　　　　　　　　-- 手动合并到本地内容  
	> 
	> $ git push <RemoteName> <BranchName>
	> $ git push -u origin master　　　　　　　-- 1st push  
	> $ git push origin master　　　　　　　　-- later push  
	> 
	> $ git remote rename <OldName> <NewName>  
	> $ git remote rm <RemoteName>  
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
