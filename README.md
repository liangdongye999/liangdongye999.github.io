# 项目介绍

你好，这是一个基于 Chirpy 的博客模版项目，能生成一个以 Issues 为 CMS 的前端静态博客网站，他会在每夜的 00:00 自动从 Gitee 仓库中拉取最新的 Issues 内容并生成静态博客网站。

# 如何使用

把本项目 Fork 到你的仓库，名字叫 `yourname.gitee.io`，`yourname` 改成你自己的 Gitee 用户名，以后你的文章就在这个仓库的 Issues 写了。

# 运行脚本

克隆到本地，用 Python3 运行 `generate_blogs_website.py` 脚本，就配置好了。

# 提交到云端

使用 Git 命令提交到 Gitee 仓库。

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

# 想办法把网站部署到 Github Pages

这一步需要你想办法访问 GitHub，把你的仓库导入到 GitHub 中，名字是 `yourname.github.io`，`yourname` 改成你自己的 GitHub 用户名。

在仓库设置的 Pages 里选择从 Actions 构建，分支选择 `main`。

最后你就可以去 Issues 里快乐地写文章了，每篇文章就是一个 Issue，标题就是文章的标题，内容就是文章的内容。