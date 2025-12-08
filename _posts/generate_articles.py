#!/usr/bin/python3

# 本项目由梁栋烨独立制作 Copyleft (c) 2025 梁栋烨
# 基于 Chirpy Starter 项目
# 开发原则是：保持简单、保持可维护性、保持可扩展性、保持可定制性
# 遵守驼峰变量名规范

class GenerateArticles:
    def getIssues(self, owner=None, repo=None):
        """获取仓库的所有issues"""
        if owner is None:
            owner = self.owner
        if repo is None:
            repo = self.repo
            
        print(f"正在获取 {owner}/{repo} 的所有issues...")
        
        url = f'{self.baseUrl}/repos/{owner}/{repo}/issues'
        params = {
            'state': 'all',  # 获取所有状态的issues
            'sort': 'created',
            'direction': 'asc',
            'per_page': 100
        }
        
        # 构建请求URL
        queryString = '&'.join([f'{k}={v}' for k, v in params.items()])
        fullUrl = f"{url}?{queryString}"
        
        try:
            with self.urlopen(fullUrl) as response:
                data = response.read().decode('utf-8')
                issues = self.loads(data)
                print(f"成功获取 {len(issues)} 个issues")
                return issues
        except (self.URLError, self.HTTPError) as e:
            print(f"获取issues失败: {e}")
            return []

    def parseIssues(self, issues):
        """
        解析issues数据
        """
        if not issues:
            return []
            
        parsedIssues = []
        for issue in issues:
            # 提取关键信息
            parsedIssue = {
                'id': issue.get('id'),
                'number': issue.get('number'),
                'title': issue.get('title', ''),
                'body': issue.get('body', ''),
                'state': issue.get('state', ''),
                'createdAt': issue.get('created_at', ''),
                'updatedAt': issue.get('updated_at', ''),
                'htmlUrl': issue.get('html_url', ''),
                'user': {
                    'login': issue.get('user', {}).get('login', ''),
                    'name': issue.get('user', {}).get('name', '')
                }
            }
            parsedIssues.append(parsedIssue)
        
        return parsedIssues

    def sanitizeFilename(self, title):
        """将标题转换为安全的文件名"""
        # 移除或替换不安全的字符
        filename = self.re.sub(r'[<>:"/\\|?*]', '', title)
        filename = self.re.sub(r'\s+', '-', filename)  # 空格替换为短横线
        filename = self.re.sub(r'-+', '-', filename)   # 多个短横线替换为一个
        filename = filename.strip('-')  # 移除首尾的短横线
        
        # 确保文件名不为空
        if not filename:
            filename = f"article-{self.datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
        return filename

    def convertToJekyllPost(self, issue):
        """将issue转换为Jekyll文章格式"""
        # 提取issue信息
        title = issue['title']
        body = issue.get('body', '') or ''
        createdAt = issue['createdAt']
        updatedAt = issue.get('updatedAt', createdAt)
        number = issue.get('number', '')
        
        # 解析日期
        try:
            createdDate = self.datetime.datetime.fromisoformat(createdAt.replace('Z', '+00:00'))
            updatedDate = self.datetime.datetime.fromisoformat(updatedAt.replace('Z', '+00:00'))
        except ValueError:
            # 如果日期解析失败，使用当前时间
            createdDate = self.datetime.datetime.now()
            updatedDate = self.datetime.datetime.now()
        
        # 生成文件名
        dateStr = createdDate.strftime('%Y-%m-%d')
        safeTitle = self.sanitizeFilename(title)
        filename = f"{dateStr}-{safeTitle}.md"
        
        # 生成front matter
        frontMatter = f"""---
title: "{title}"
date: {createdDate.strftime('%Y-%m-%d %H:%M:%S %z')}
last_modified_at: {updatedDate.strftime('%Y-%m-%d %H:%M:%S %z')}
categories: [Gitee Issues]
tags: [{number}]  # 使用issue编号作为tag
comments: true
---

## 原始链接

本文档从Gitee Issue自动生成，原文地址：[Issue #{number}](https://gitee.com/{self.owner}/{self.repo}/issues/{number})

---

"""
        
        # 处理body内容（如果为空则使用标题作为内容）
        if not body.strip():
            content = f"**{title}**\n\n> 此文章来自Gitee Issue，内容为空，已自动使用标题作为内容。"
        else:
            # 处理markdown内容
            content = self.processMarkdown(body)
        
        # 组合完整的文章内容
        articleContent = frontMatter + content
        
        return filename, articleContent

    def processMarkdown(self, markdownContent):
        """处理markdown内容，适配Jekyll"""
        if not markdownContent:
            return ""
        
        # 基本的markdown处理
        lines = markdownContent.split('\n')
        processedLines = []
        
        for line in lines:
            # 移除Gitee特有的markdown语法（如果存在）
            line = self.re.sub(r'!\[.*?\]\(.*?\)', '', line)  # 临时移除图片，避免链接问题
            processedLines.append(line)
        
        return '\n'.join(processedLines)

    def writeArticle(self, issue):
        """将issue写入为文章文件"""
        try:
            # 转换为Jekyll文章格式
            filename, content = self.convertToJekyllPost(issue)
            
            # 保存文件
            filePath = self.postsDir / filename
            with open(filePath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ 成功生成文章: {filename}")
            return True
        except Exception as e:
            print(f"❌ 生成文章失败: {e}")
            return False

    def generateArticles(self):
        """主函数：生成所有文章"""
        print("🚀 开始从Gitee Issues生成Jekyll文章...")
        print("=" * 50)
        
        # 获取所有issues
        issues = self.getIssues()
        if not issues:
            print("没有获取到任何issues，程序退出")
            return
        
        # 解析issues
        parsedIssues = self.parseIssues(issues)
        
        generatedCount = 0
        
        for issue in parsedIssues:
            number = issue.get('number')
            if not number:
                continue
            
            print(f"\n📝 处理Issue #{number}: {issue['title'][:50]}...")
            
            # 检查文件是否已存在
            filename, _ = self.convertToJekyllPost(issue)
            filePath = self.postsDir / filename
            if filePath.exists():
                print(f"⚠️  文章已存在，跳过: {filename}")
                continue
            
            # 生成文章
            if self.writeArticle(issue):
                generatedCount += 1
        
        print("\n" + "=" * 50)
        print(f"🎉 文章生成完成！共生成 {generatedCount} 篇文章")
        print(f"📁 文章保存位置: {self.postsDir}")
        
        # 显示生成的文章列表
        mdFiles = list(self.postsDir.glob("*.md"))
        if mdFiles:
            print(f"\n📚 当前目录下的所有文章 ({len(mdFiles)} 篇):")
            for mdFile in sorted(mdFiles):
                print(f"  - {mdFile.name}")

    def __init__(self, owner, repo):
        # 首先导入需要的模块
        from pathlib import Path
        from urllib.request import urlopen, Request
        from urllib.error import URLError, HTTPError
        from json import loads, dumps
        import re
        import datetime
        
        # 将导入的模块赋值给self
        self.urlopen = urlopen
        self.Request = Request
        self.URLError = URLError
        self.HTTPError = HTTPError
        self.loads = loads
        self.dumps = dumps
        self.re = re
        self.datetime = datetime
        self.Path = Path
        
        # 然后设置实例属性
        self.owner = owner
        self.repo = repo
        self.baseUrl = "https://gitee.com/api/v5"
        self.postsDir = self.Path(__file__).parent
        
        self.generateArticles()

def main():
    """主函数 - 类当函数用，直接创建实例即可"""
    # 直接创建实例，__init__就是入口点
    GenerateArticles("liangdongye", "liangdongye.gitee.io")

if __name__ == '__main__':
    main()