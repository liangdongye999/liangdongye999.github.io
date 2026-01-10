# 项目概述

这是一个基于 **Hexo** 的静态博客网站项目，使用 **Butterfly** 主题。

## 技术栈

- **Hexo 8.0.0** - 快速、简洁且高效的静态博客框架
- **Butterfly 主题** - 现代化、优雅且功能丰富的 Hexo 主题
- **Node.js** - 运行环境
- **Markdown** - 内容编写格式

## 项目结构

```
.
├── _config.yml              # Hexo 主配置文件
├── _config.landscape.yml    # 默认主题配置文件（已废弃）
├── source/                  # 源文件目录
│   └── _posts/             # 博客文章目录
├── themes/                  # 主题目录
│   └── butterfly/          # Butterfly 主题（从 Gitee 克隆）
├── scaffolds/              # 文章模板目录
├── node_modules/           # 依赖包目录
├── package.json            # 项目依赖配置
└── public/                 # 生成的静态文件目录（运行 build 后生成）
```

## 核心配置文件

### `_config.yml`
Hexo 的主配置文件，包含：
- 网站基本信息（标题、作者、描述等）
- URL 配置
- 目录结构配置
- 写作配置
- 主题设置（当前设置为 `landscape`，需要改为 `butterfly`）
- 部署配置

### `themes/butterfly/_config.yml`
Butterfly 主题的配置文件，包含丰富的主题设置选项：
- 导航栏设置
- 代码块样式
- 图片设置（头像、封面、背景等）
- 首页布局
- 文章设置（目录、版权、相关文章等）
- 侧边栏设置
- 评论系统（支持多种评论插件）
- 搜索功能
- 分享功能
- 统计分析
- 视觉效果（深色模式、打字机效果等）

## 构建和运行

### 可用命令

```bash
# 启动本地开发服务器
npm run server
# 或
hexo server

# 生成静态文件
npm run build
# 或
hexo generate

# 清理生成的文件
npm run clean
# 或
hexo clean

# 部署到远程服务器
npm run deploy
# 或
hexo deploy

# 创建新文章
hexo new "文章标题"

# 创建新页面
hexo new page "页面名称"
```

### 开发流程

1. **创建文章**
   ```bash
   hexo new "My New Post"
   ```
   这会在 `source/_posts/` 目录下创建一个新的 Markdown 文件

2. **本地预览**
   ```bash
   npm run server
   ```
   访问 `http://localhost:4000` 查看效果

3. **生成静态文件**
   ```bash
   npm run build
   ```
   生成的文件会保存在 `public/` 目录

4. **部署**
   ```bash
   npm run deploy
   ```

## 主题配置说明

### 启用 Butterfly 主题

需要在 `_config.yml` 中将主题设置为 `butterfly`：

```yaml
theme: butterfly
```

### 安装主题依赖

Butterfly 主题需要安装额外的渲染器：

```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

### 主题配置

主题的所有配置都在 `themes/butterfly/_config.yml` 文件中。建议不要直接修改主题目录下的配置文件，而是在项目根目录创建 `_config.butterfly.yml` 文件，这样可以避免主题更新时配置被覆盖。

## 开发约定

### 文章编写

- 文章使用 Markdown 格式编写
- 文章文件位于 `source/_posts/` 目录
- 每篇文章的 Front Matter 包含文章元数据（标题、日期、标签等）

### 图片资源

- 可以使用 `post_asset_folder` 选项为每篇文章创建独立的资源文件夹
- 图片可以放在 `source/img/` 目录下统一管理

### 主题定制

- 优先使用主题配置文件进行定制
- 如需深度定制，可以在 `source/` 目录下覆盖主题的模板文件
- 自定义 CSS 可以放在 `source/css/` 目录

## 重要注意事项

1. **主题切换**：当前主题设置为 `landscape`，需要手动改为 `butterfly`
2. **依赖安装**：Butterfly 主题需要安装 `hexo-renderer-pug` 和 `hexo-renderer-stylus`
3. **配置覆盖**：建议创建 `_config.butterfly.yml` 来覆盖主题配置，而不是直接修改主题文件
4. **部署配置**：需要在 `_config.yml` 中配置部署信息（如 GitHub Pages、Vercel 等）

## 常见问题

### 本地服务器无法启动
- 检查端口 4000 是否被占用
- 确保已运行 `npm install` 安装所有依赖

### 主题样式不生效
- 确认主题配置正确
- 运行 `hexo clean` 清理缓存
- 确保已安装主题所需的渲染器

### 部署失败
- 检查 `_config.yml` 中的部署配置
- 确认 Git 仓库配置正确
- 检查网络连接

## 参考资源

- [Hexo 官方文档](https://hexo.io/docs/)
- [Butterfly 主题文档](https://butterfly.js.org/)
- [Butterfly 主题 GitHub](https://github.com/jerryc127/hexo-theme-butterfly)
- [Butterfly 主题 Gitee 镜像](https://gitee.com/immyw/hexo-theme-butterfly)