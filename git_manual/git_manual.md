# git record

## git三种状态
* committed（已提交）
* modified（已修改）
* staged（已暂存）

## git三个工作区域
* git 仓库 --> 提交更新
* 工作目录 --> 修改文件 
* 暂存区域 --> 暂存文件

## installed
`sudo apt-get install git`

## git config
* /etc/gitconfig 文件（*所有用户*）：包含系统上每个用户及他们仓库的通用配置。如果使用带有--system选项的git config时，他会从此文件读写配置变量。
* ~/.gitconfig 或 ~/.config/git/config 文件（*当前用户*）：针对当前用户。可以传递--global选项让Git读写此文件。
* 当前使用仓库的Git目录中的config文件（就是.git/config）（*当前仓库*）:针对该仓库。

## git 设置user --> name/email
`git config --global user.name "***"`
`git config --global user.email "***@example.com"`

* *\! 当你想针对不同的项目使用不用的用户名和邮件地址时，可以在那个项目目录下运行没有--global选项的命令*

## git 文本编辑器
`git config --global core.editor emacs`

## 检查配置信息
* 如果想要检查你的配置信息，`git config --list` 命令列出所有的配置信息。
* 可以使用`git config <key>`检查某一项配置。
```git config user.name
   git config user.email
```

## 获取帮助
* git help <verb>
* git <verb> --help
* man git-<verb>

## 获取git仓库
* 从现有的目录或者仓库中导入文件到git中
  --> `git init`
  --> `git add *.c`
  --> `git add LICENSE`
  --> `git commit -m 'init'`
* 从一个服务器克隆一个现有的Git仓库
  --> `git clone https://....`    /   `git clone ssh://`
 
## 检查当前文件的状态
* `git status`
* `git status -s` 
   * ?? 新添加未跟踪的文件
   * A 新添加到暂存区
   * M（靠左）修改过的文件放入暂存
   * M（靠右）修改过未放入暂存
   * MM 修改-> 放入暂存-> 又修改

## 忽略文件
* 总有一些文件不需要加入Git的管理，所以可以创建一个.gitgnore文件，列出要忽略的文件模式。
```
cat .gitgnore
*.[oa]
*~
```
   - 第二行忽略所有.a或.o结尾的文件。
   - 第三行忽略所有~结尾的文件。

* 所有空行或者以 ＃ 开头的行都会被 Git 忽略。
* 可以使用标准的 glob 模式匹配。
* 匹配模式可以以（/）开头防止递归。
* 匹配模式可以以（/）结尾指定目录。
* 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。
```
# no .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in the build/ directory
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory
doc/**/*.pdf
```

## 查看已暂存和未暂存的修改 
* 查看尚未暂存的文件修改了哪些部分
`git diff`

* 查看已暂存的将要添加到下次提交里的内容 --> git diff --cached -->更高版本可以使用`git diff --staged`

## 提交更新
* `git commit -m "改动说明"`
* `git commit -a` 把所有已经跟踪过的文件暂存并提交。

## 移除文件 -->	从暂存区文件中移除
* `git rm --cached filename` 暂存区移除

## 移动文件
* `git mv file1 file2` --> 将文件1修改为文件2

## 查看历史提交
* `git log`
* `git log -P -2` --> 查看最近两次的提交差异
* `git log --stat` --> 每次提交的统计信息。
* `git log --since=2.weeks` --> 显示指定时间之后的提交
* `git log --until=2008-01-15` --> 显示指定时间之前的提交

## 撤销操作
* `git commit --amend` --> 撤销commit后的错误操作。

## 取消暂存的文件
* 取消其中某一个文件的add操作 --> `git reset HEAD filename`

## 撤销对文件的修改
* `git checkout -- filename` --> 撤销对文件的所有修改。（warning）

## 远程仓库的使用
### 查看远程仓库
* `git remote` --> 查看git克隆的仓库服务器的默认名字
* `git remote -v` --> 显示需要读写远程仓库使用的Git保存的简写与其对应的URL

### 添加远程仓库
* `git remote add <shortname> <url>` --> 添加新的远程仓库并指定简称

### 从远程仓库中抓取并拉取
* `git fetch [remote-name]` --> 从远程仓库中拉取你还没有的数据，执行完成后，可以拥有远程仓库所有的分支的引用，可以随时合并和查看
* *\! remote-name = shortname*
* `git pull` --> 自动抓取然后合并远程分支到当前分支
* `git clone` --> 自动设置本地master分支跟踪克隆的远程仓库的master分支

### 推送到远程仓库
* `git push [remote-name] [branch-name]` --> 将branch分支推送到远程仓库

### 查看远程仓库
* `git remote show origin`

### 远程仓库的移除与重命名
* `git remote rename [old_name] [new_name]` --> 重命名
* `git remote rm paul` --> 删除paul仓库

## 打标签
### 列出标签
* `git tag` --> 列出已有的标签
* `git tag -l 'v1.8.5*'` --> 对v1.8.5系列感兴趣

### 创建标签
#### 附注标签
* `git tag -a v1.4 -m 'my version 1.4'` --> -a 创建，-m 指定
* *\！附注标签是存储在 Git 数据库中的一个完整对象。 它们是可以被校验的；其中包含打标签者的名字、电子邮件地址、日期时间；还有一个标签信息；并且可以使用 GNU Privacy Guard （GPG）签名与验证。 通常建议创建附注标签，这样你可以拥有以上所有信息；但是如果你只是想用一个临时的标签，或者因为某些原因不想要保存那些信息，轻量标签也是可用的*
* `git show v1.4` --> 查看标签信息与对应的提交信息

#### 轻量标签
* *\! 轻量标签本质上是将提交校验和存储到一个文件中 - 没有保存任何其他信息。 创建轻量标签，不需要使用 -a、-s 或 -m 选项，只需要提供标签名字* 
* `git tag v1.4-lw`

### 后期打标签
```
git log --pretty=oneline
15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment'
a6b4c97498bd301d84096da251c98a07c7723e65 beginning write support
0d52aaab4479697da7686c15f77a3d64d9165190 one more thing
6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'
0b7434d86859cc7b8c3d5e1dddfed66ff742fcbc added a commit function
4682c3261057305bdd616e23b64b0857d832627b added a todo file
166ae0c4d3f420721acbb115cc33848dfcc2121a started write support
9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile
964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo
8a5cbc430f1a9c3d00faaeffd07798508422908a updated readme
```
`git tag -a v1.2 9fceb02`

### 共享标签
* `git push origin v1.5` --> 将v1.5这个标签push到远程仓库
* `git push origin --tags` --> 推送所有标签到远程仓库

### 检出标签
* `git checkout -b version2 v2.0.0` --> 将工作目录version2和仓库中特定的标签版本完全一样，并创建一个新分支

### git 别名
* *\! 给每一个命令设置别名*
* `git config --global alias.co checkout` -->用co替代checkout

















