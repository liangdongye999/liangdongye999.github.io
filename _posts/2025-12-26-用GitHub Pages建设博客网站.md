---
title: 用GitHub Pages建设博客网站
tags:
  - 网站
---

访问[https://github.com/cotes2020/chirpy-starter/](https://github.com/cotes2020/chirpy-starter/)，这是一个模板仓库，点`Use this template`、`Create a new repository`就创建好了；注意，不是`Fork`。

主要修改以下内容，不用对着我的改，你可以问AI我改了什么，意味着什么：

```patch
diff --git a/.github/workflows/pages-deploy.yml b/.github/workflows/pages-deploy.yml
index cc28f99..364e2c6 100644
--- a/.github/workflows/pages-deploy.yml
+++ b/.github/workflows/pages-deploy.yml
@@ -50,12 +50,6 @@ jobs:
         env:
           JEKYLL_ENV: "production"
 
-      - name: Test site
-        run: |
-          bundle exec htmlproofer _site \
-            \-\-disable-external \
-            \-\-ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"
-
       - name: Upload site artifact
         uses: actions/upload-pages-artifact@v3
         with:
diff --git a/2927e4796c7a20da2e651442cf2ed00cc44ec4e3.jpg b/2927e4796c7a20da2e651442cf2ed00cc44ec4e3.jpg
new file mode 100644
index 0000000..181fa23
Binary files /dev/null and b/2927e4796c7a20da2e651442cf2ed00cc44ec4e3.jpg differ
diff --git a/README.md b/README.md
deleted file mode 100644
index 793cd08..0000000
--- a/README.md
+++ /dev/null
@@ -1,43 +0,0 @@
-# Chirpy Starter
-
-[![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy)][gem]&nbsp;
-[![GitHub license](https://img.shields.io/github/license/cotes2020/chirpy-starter.svg?color=blue)][mit]
-
-When installing the [**Chirpy**][chirpy] theme through [RubyGems.org][gem], Jekyll can only read files in the folders
-`_data`, `_layouts`, `_includes`, `_sass` and `assets`, as well as a small part of options of the `_config.yml` file
-from the theme's gem. If you have ever installed this theme gem, you can use the command
-`bundle info --path jekyll-theme-chirpy` to locate these files.
-
-The Jekyll team claims that this is to leave the ball in the user’s court, but this also results in users not being
-able to enjoy the out-of-the-box experience when using feature-rich themes.
-
-To fully use all the features of **Chirpy**, you need to copy the other critical files from the theme's gem to your
-Jekyll site. The following is a list of targets:
-
-```shell
-.
-├── _config.yml
-├── _plugins
-├── _tabs
-└── index.html
-```
-
-To save you time, and also in case you lose some files while copying, we extract those files/configurations of the
-latest version of the **Chirpy** theme and the [CD][CD] workflow to here, so that you can start writing in minutes.
-
-## Usage
-
-Check out the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).
-
-## Contributing
-
-This repository is automatically updated with new releases from the theme repository. If you encounter any issues or want to contribute to its improvement, please visit the [theme repository][chirpy] to provide feedback.
-
-## License
-
-This work is published under [MIT][mit] License.
-
-[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
-[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
-[CD]: https://en.wikipedia.org/wiki/Continuous_deployment
-[mit]: https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE
diff --git a/_config.yml b/_config.yml
index 02f6b7c..88eee23 100644
--- a/_config.yml
+++ b/_config.yml
@@ -6,40 +6,40 @@ theme: jekyll-theme-chirpy
 # The language of the webpage › http://www.lingoes.net/en/translator/langcode.htm
 # If it has the same name as one of the files in folder `_data/locales`, the layout language will also be changed,
 # otherwise, the layout language will use the default value of 'en'.
-lang: en
+lang: zh-CN
 
 # Change to your timezone › https://zones.arilyn.cc
-timezone:
+timezone: Asia/Shanghai
 
 # jekyll-seo-tag settings › https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md
 # ↓ --------------------------
 
-title: Chirpy # the main title
+title: Geek晚班车 # the 
 
-tagline: A text-focused Jekyll theme # it will display as the subtitle
+tagline: 不喜欢上学，没学历，喜欢编程和养龟。 # it will display as the subtitle
 
 description: >- # used by seo meta and the atom feed
-  A minimal, responsive and feature-rich Jekyll theme for technical writing.
+  Geek晚班车的个人网站，炸了也没人看。
 
 # Fill in the protocol & hostname for your site.
 # E.g. 'https://username.github.io', note that it does not end with a '/'.
 url: ""
 
 github:
-  username: github_username # change to your GitHub username
+  username: liangdongye999 # change to your GitHub username
 
-twitter:
-  username: twitter_username # change to your Twitter username
+# twitter:
+  # username: twitter_username # change to your Twitter username
 
 social:
   # Change to your full name.
   # It will be displayed as the default author of the posts and the copyright owner in the Footer
-  name: your_full_name
-  email: example@domain.com # change to your email address
+  name: Geek晚班车
+  email: 3813563706@qq.com # change to your email address
   links:
     # The first element serves as the copyright owner's link
-    - https://twitter.com/username # change to your Twitter homepage
-    - https://github.com/username # change to your GitHub homepage
+    # - https://twitter.com/username # change to your Twitter homepage
+    - https://github.com/liangdongye999 # change to your GitHub homepage
     # Uncomment below to add more social links
     # - https://www.facebook.com/username
     # - https://www.linkedin.com/in/username
@@ -88,7 +88,7 @@ pageviews:
 #     light — Use the light color scheme
 #     dark — Use the dark color scheme
 #
-theme_mode: # [light | dark]
+theme_mode: light # [light | dark]
 
 # The CDN endpoint for media resources.
 # Notice that once it is assigned, the CDN url
@@ -98,18 +98,18 @@ theme_mode: # [light | dark]
 cdn:
 
 # the avatar on sidebar, support local or CORS resources
-avatar:
+avatar: 2927e4796c7a20da2e651442cf2ed00cc44ec4e3.jpg
 
 # The URL of the site-wide social preview image used in SEO `og:image` meta tag.
 # It can be overridden by a customized `page.image` in front matter.
-social_preview_image: # string, local or CORS resources
+social_preview_image: 2927e4796c7a20da2e651442cf2ed00cc44ec4e3.jpg
 
 # boolean type, the global switch for TOC in posts.
 toc: true
 
 comments:
   # Global switch for the post-comment system. Keeping it empty means disabled.
-  provider: # [disqus | utterances | giscus]
+  provider: giscus # [disqus | utterances | giscus]
   # The provider options are as follows:
   disqus:
     shortname: # fill with the Disqus shortname. › https://help.disqus.com/en/articles/1717111-what-s-a-shortname
@@ -119,15 +119,15 @@ comments:
     issue_term: # < url | pathname | title | ...>
   # Giscus options › https://giscus.app
   giscus:
-    repo: # <gh-username>/<repo>
-    repo_id:
-    category:
-    category_id:
-    mapping: # optional, default to 'pathname'
-    strict: # optional, default to '0'
-    input_position: # optional, default to 'bottom'
-    lang: # optional, default to the value of `site.lang`
-    reactions_enabled: # optional, default to the value of `1`
+    repo: liangdongye999/liangdongye999.github.io # <gh-username>/<repo>
+    repo_id: R_kgDOQu4mUw
+    category: Announcements
+    category_id: DIC_kwDOQu4mU84C0PRc
+    mapping: pathname # optional, default to 'pathname'
+    strict: 0 # optional, default to '0'
+    input_position: top # optional, default to 'bottom'
+    lang: zh-CN # optional, default to the value of `site.lang`
+    reactions_enabled: 1 # optional, default to the value of `1`
 
 # Self-hosted static assets, optional › https://github.com/cotes2020/chirpy-static-assets
 assets:
@@ -138,7 +138,7 @@ assets:
     env: # [development | production]
 
 pwa:
-  enabled: true # The option for PWA feature (installable)
+  enabled: false # The option for PWA feature (installable)
   cache:
     enabled: true # The option for PWA offline cache
     # Paths defined here will be excluded from the PWA cache.
diff --git a/_tabs/about.md b/_tabs/about.md
index ddb2bc4..fa06e11 100644
--- a/_tabs/about.md
+++ b/_tabs/about.md
@@ -4,5 +4,4 @@ icon: fas fa-info-circle
 order: 4
 ---
 
-> Add Markdown syntax content to file `_tabs/about.md`{: .filepath } and it will show up on this page.
-{: .prompt-tip }
+我的个人网站……我不喜欢上学，谁爱上谁上；网站炸了也没人看。
```
