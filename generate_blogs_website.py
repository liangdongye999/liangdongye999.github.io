#!/usr/bin/python3

# 本项目由梁栋烨独立制作 Copyleft (c) 2025 梁栋烨
# 基于 Chirpy Starter 项目
# 开发原则是：保持简单、保持可维护性、保持可扩展性、保持可定制性
# 遵守驼峰变量名规范

class generateBlogsWebsite:
    def getGiteeInfo(self, userName):
        with self.urlopen(f'https://gitee.com/api/v5/users/{userName}') as response:
            return response.read().decode('utf-8')
    
    def editChirpyStarter(self, getGiteeInfoResult):
        """
        返回结果示例：
        {
            "id":16360804,
            "login":"hanxingwan",
            "name":"寒行晚",
            "avatar_url":"https://foruda.gitee.com/avatar/1761768741799764932/16360804_hanxingwan_1761768741.jpeg",
            "url":"https://gitee.com/api/v5/users/hanxingwan",
            "html_url":"https://gitee.com/hanxingwan",
            "remark":"",
            "followers_url":"https://gitee.com/api/v5/users/hanxingwan/followers",
            "following_url":"https://gitee.com/api/v5/users/hanxingwan/following_url{/other_user}",
            "gists_url":"https://gitee.com/api/v5/users/hanxingwan/gists{/gist_id}",
            "starred_url":"https://gitee.com/api/v5/users/hanxingwan/starred{/owner}{/repo}",
            "subscriptions_url":"https://gitee.com/api/v5/users/hanxingwan/subscriptions",
            "organizations_url":"https://gitee.com/api/v5/users/hanxingwan/orgs",
            "repos_url":"https://gitee.com/api/v5/users/hanxingwan/repos",
            "events_url":"https://gitee.com/api/v5/users/hanxingwan/events{/privacy}",
            "received_events_url":"https://gitee.com/api/v5/users/hanxingwan/received_events",
            "type":"User",
            "blog":null,
            "weibo":null,
            "bio":"我永远是最帅的呢哼哼！",
            "public_repos":6,
            "public_gists":0,
            "followers":0,
            "following":2,
            "stared":0,
            "watched":7,
            "created_at":"2025-10-30T04:12:06+08:00",
            "updated_at":"2025-11-30T21:45:38+08:00",
            "company":null,
            "profession":null,
            "wechat":null,
            "qq":null,
            "linkedin":null,
            "email":"13232183076@163.com"
        }
        """
        with open('_config.yml','r') as f:
            config = f.read()
        config = (
            config.replace("lang: en","lang: zh-CN")
                .replace("timezone:","timezone: Asia/Shanghai")
                .replace("title: Chirpy # the main title","title: %s" % getGiteeInfoResult['name'])
                .replace("tagline: A text-focused Jekyll theme # it will display as the subtitle","tagline: %s" % getGiteeInfoResult['bio'])
                .replace("description: >- # used by seo meta and the atom feed\n  A minimal, responsive and feature-rich Jekyll theme for technical writing.","description: >- # used by seo meta and the atom feed\n  %s" % getGiteeInfoResult['bio'])
                .replace("github:\n  username: github_username # change to your GitHub username","#github:\n#  username: github_username # change to your GitHub username")
                .replace("twitter:\n  username: twitter_username # change to your Twitter username","#twitter:\n#  username: twitter_username # change to your Twitter username")
                .replace("  name: your_full_name","  name: %s" % getGiteeInfoResult['name'])
                .replace("  email: example@domain.com # change to your email address","  email: %s" % getGiteeInfoResult['email'])
                .replace("avatar:","avatar: %s" % getGiteeInfoResult['avatar_url'])
        )
        with open('chirpy-starter/_config.yml','w') as f:
            f.write(config)

    def generateBlogsWebsite(self):
        getGiteeInfoResult = self.loads(self.getGiteeInfo(input('请输入 Gitee 用户名：')))
        self.editChirpyStarter(getGiteeInfoResult)

    def generateAutoGenerateArticlesScript(self, getGiteeInfoResult):
        with open('_posts/generate_articles.py','r') as f:
            script = f.read()
        script = script.replace("GenerateBlogs(\"\",\"\")","GenerateBlogs(\"%s\",\"%s\")" % (getGiteeInfoResult['login'],getGiteeInfoResult['login'] + ".gitee.io"))
        with open('_posts/generate_articles.py','w') as f:
            f.write(script)

    def __init__(self):
        from json import loads
        from urllib.request import urlopen

        self.loads = loads
        self.urlopen = urlopen

        # 先获取Gitee信息
        getGiteeInfoResult = self.loads(self.getGiteeInfo(input('请输入 Gitee 用户名：')))
        
        # 然后执行网站生成和脚本生成
        self.editChirpyStarter(getGiteeInfoResult)
        self.generateAutoGenerateArticlesScript(getGiteeInfoResult)

def main():
    generateBlogsWebsite()
    return 0

if __name__ == '__main__':
    main()