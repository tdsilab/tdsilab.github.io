# 网站维护交接文档

## 项目概述

本项目是团队官方网站，使用纯HTML静态页面部署在GitHub Pages上。

### 技术栈
- 纯HTML静态页面
- GitHub Pages 托管
- GitHub Actions 自动化部署
- Git 版本控制

---

## 项目结构

```
tdsilab.github.io/
├── .github/
│   └── workflows/
│       ├── static.yml          # GitHub Pages 部署工作流
│       └── jekyll-docker.yml   # Jekyll 构建工作流（备用）
├── assets/
│   ├── direction/              # 研究方向页面图片
│   ├── fonts/                  # 字体文件
│   ├── inline/                 # 内联图片资源
│   ├── photo/                  # 团队照片
│   └── team/                   # 团队成员头像
├── index.html                  # 首页
├── team.html                   # 团队介绍页
├── direction.html              # 研究方向页
└── joinus.html                 # 加入我们页
```

---

## 开始使用

### 前置要求
1. Git 已安装
2. GitHub 账户，拥有仓库访问权限
3. 基本的HTML知识

### 克隆项目
```bash
git clone https://github.com/tdsilab/tdsilab.github.io.git
cd tdsilab.github.io
```

### 本地预览
直接在浏览器中打开 `index.html` 文件即可预览网站。

---

## 日常维护

### 修改网页内容

#### 1. 首页 (index.html)
- 打开 `index.html` 文件
- 查找需要修改的文本内容
- 保存文件后提交更改

#### 2. 团队介绍页 (team.html)
- 打开 `team.html` 文件
- 修改团队成员信息
- 更新头像图片（放在 `assets/team/` 目录）

#### 3. 研究方向页 (direction.html)
- 打开 `direction.html` 文件
- 修改研究方向描述
- 更新相关图片（放在 `assets/direction/` 目录）

#### 4. 加入我们页 (joinus.html)
- 打开 `joinus.html` 文件
- 修改招聘信息或联系方式

### 添加图片资源

1. 将图片文件放入对应的目录：
   - 团队照片：`assets/photo/`
   - 研究方向图片：`assets/direction/`
   - 团队头像：`assets/team/`

2. 在HTML文件中引用图片：
```html
<img src="assets/team/新成员头像.webp" alt="新成员姓名">
```

### 图片优化建议

- 推荐使用 WebP 格式（已在项目中使用）
- 图片大小建议控制在 500KB 以内
- 尺寸适中，避免过大的原始图片

---

## 部署流程

### 自动化部署

项目已配置 GitHub Actions 自动部署，只需：

1. 提交更改到本地仓库
   ```bash
   git add .
   git commit -m "描述你的更改"
   ```

2. 推送到 GitHub
   ```bash
   git push origin main
   ```

3. 自动部署会触发，可以在 GitHub 仓库的 **Actions** 标签页查看进度

### 手动触发部署

如需手动重新部署：

1. 进入 GitHub 仓库
2. 点击 **Actions** 标签
3. 选择 **Deploy static content to Pages** 工作流
4. 点击 **Run workflow** → **Run workflow**

---

## Git 常用操作

### 查看状态
```bash
git status
```

### 查看修改
```bash
git diff
```

### 提交更改
```bash
git add <文件名>
git commit -m "提交说明"
```

### 拉取更新
```bash
git pull origin main
```

### 推送更改
```bash
git push origin main
```

### 查看历史
```bash
git log --oneline
```

---

## GitHub Pages 配置

### 仓库设置

1. 进入 GitHub 仓库
2. 点击 **Settings**
3. 在左侧菜单选择 **Pages**
4. 确认：
   - Source: Deploy from a branch
   - Branch: gh-pages (由 Actions 自动生成)
   - Folder: / (root)

### 自定义域名

如需设置自定义域名：

1. 在仓库根目录创建 `CNAME` 文件
2. 写入你的域名（例如：`www.example.com`）
3. 在域名服务商处配置 DNS 解析

---

## 常见问题

### 1. 部署失败
- 检查 Actions 日志中的错误信息
- 确认文件格式正确，没有语法错误
- 尝试手动触发工作流重新部署

### 2. 页面更新不生效
- 等待 5-10 分钟让 GitHub Pages 生效
- 清除浏览器缓存或使用无痕模式查看
- 确认已推送到 main 分支

### 3. 图片不显示
- 检查图片路径是否正确
- 确认图片文件已提交到仓库
- 检查图片文件名大小写（GitHub 区分大小写）

### 4. Git 推送问题
- 如遇大文件推送失败，已配置 `http.postBuffer`：
  ```bash
  git config --global http.postBuffer 524288000
  ```

---

## 工作流详解

### static.yml 工作流

文件位置：`.github/workflows/static.yml`

主要功能：
- 监听 main 分支的推送
- 配置 Pages 环境
- 上传整个仓库作为构建产物
- 部署到 GitHub Pages

关键配置：
```yaml
timeout-minutes: 30  # 部署超时时间设置
```

---

## 交接清单

- [ ] 确认拥有仓库的写入权限
- [ ] 熟悉项目结构
- [ ] 了解日常内容修改流程
- [ ] 测试本地预览功能
- [ ] 确认部署流程正常
- [ ] 了解常见问题解决方法
- [ ] 保存本文档以备查阅

---

## 联系方式

如有问题，请联系团队负责人或前维护人员。

---

**文档版本**：1.0  
**最后更新**：2026-07-04
