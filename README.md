# MindPalace - 知识宫殿

> 化心为殿，万念不湮

## 项目简介

MindPalace 是一个综合性的知识导航网站，涵盖人工智能、大模型、Agent开发、农业科技等领域的学习资源和资讯汇总。

## 网站地址

- **外网访问**: https://sddxl150-star.github.io/MindPalace/
- **本地访问**: http://localhost:8080/

---

## 页面导航

### 核心板块

| 页面 | 文件名 | 功能描述 | 公网链接 |
|------|--------|----------|----------|
| 首页 | index.html | 网站主页，导航中心 | [访问](https://sddxl150-star.github.io/MindPalace/index.html) |
| AI基础 | ai-basics.html | AI基础知识导航与技术概念时间轴 | [访问](https://sddxl150-star.github.io/MindPalace/ai-basics.html) |
| 经典论文 | papers.html | AI领域经典论文汇总 | [访问](https://sddxl150-star.github.io/MindPalace/papers.html) |
| 项目展示 | projects.html | AI相关开源项目展示 | [访问](https://sddxl150-star.github.io/MindPalace/projects.html) |
| 大模型公司 | companies.html | 主要大模型公司介绍 | [访问](https://sddxl150-star.github.io/MindPalace/companies.html) |
| 大模型社区 | community.html | 大模型社区资源汇总 | [访问](https://sddxl150-star.github.io/MindPalace/community.html) |

### Agent 开发

| 页面 | 文件名 | 功能描述 | 公网链接 |
|------|--------|----------|----------|
| Agent开发 | agentdev.html | Agent开发问答和学习资料 | [访问](https://sddxl150-star.github.io/MindPalace/agentdev.html) |
| Agent Skills | skills.html | Anthropic Claude Agent Skills 文档 | [访问](https://sddxl150-star.github.io/MindPalace/skills.html) |
| Claude Code架构 | claude-code-architecture.html | Claude Code泄露框架技术架构解析 | [访问](https://sddxl150-star.github.io/MindPalace/claude-code-architecture.html) |

### 本体与语义

| 页面 | 文件名 | 功能描述 | 公网链接 |
|------|--------|----------|----------|
| 本体构建 Step 1 | dify-workflow.html | 语义测试和本体构建教程 | [访问](https://sddxl150-star.github.io/MindPalace/dify-workflow.html) |
| 本体+AI | ontology-ai.html | 本体与AI结合应用 | [访问](https://sddxl150-star.github.io/MindPalace/ontology-ai.html) |
| 农业本体 | ontology.html | 农业领域本体论 | [访问](https://sddxl150-star.github.io/MindPalace/ontology.html) |

### 行业应用

| 页面 | 文件名 | 功能描述 | 公网链接 |
|------|--------|----------|----------|
| AI+海洋牧场 | ocean-ranch.html | AI在海洋牧场中的应用 | [访问](https://sddxl150-star.github.io/MindPalace/ocean-ranch.html) |
| 流程图 | ocean-ranch-flow.html | 海洋牧场项目流程图 | [访问](https://sddxl150-star.github.io/MindPalace/ocean-ranch-flow.html) |
| 农业期刊 | agriculture.html | 全球农业顶刊与顶会大全 | [访问](https://sddxl150-star.github.io/MindPalace/agriculture.html) |
| USDA & Palantir | usda-palantir.html | USDA与Palantir合作新闻 | [访问](https://sddxl150-star.github.io/MindPalace/usda-palantir.html) |
| 农业模型算法 | agriculture-models.html | GitHub开源农业AI模型精选 | [访问](https://sddxl150-star.github.io/MindPalace/agriculture-models.html) |

### 专题研究

| 页面 | 文件名 | 功能描述 | 公网链接 |
|------|--------|----------|----------|
| Palantir专题 | palantir.html | Palantir公司专题介绍 | [访问](https://sddxl150-star.github.io/MindPalace/palantir.html) |
| Openclaw探索 | openclaw.html | Openclaw项目探索 | [访问](https://sddxl150-star.github.io/MindPalace/openclaw.html) |
| FishTest | fishtest.html | FishTest相关测试 | [访问](https://sddxl150-star.github.io/MindPalace/fishtest.html) |

### 系统管理

| 页面 | 文件名 | 功能描述 | 公网链接 |
|------|--------|----------|----------|
| 评论管理 | admin.html | 用户评论审核和管理后台 | [访问](https://sddxl150-star.github.io/MindPalace/admin.html) |
| 离线页面 | offline.html | 离线状态提示页面 | [访问](https://sddxl150-star.github.io/MindPalace/offline.html) |

---

## 核心功能

### 📱 响应式设计
- 完美适配桌面端、平板、手机等多种设备
- 移动端优化的导航和布局

### 💬 评论系统
- 用户可提交评论和反馈
- 评论数据使用 localStorage 本地存储
- 后台评论审核管理

### 🌐 多语言支持
- 部分页面支持中英文切换
- 翻译内容存储于页面中

### 🚀 快速导航
- 左侧导航栏快速定位
- 分类清晰，内容结构化
- 平滑滚动动画效果

---

## 技术栈

- **前端**: HTML5 + CSS3 + JavaScript
- **样式**: 原生CSS（Flexbox + Grid布局）
- **存储**: localStorage
- **部署**: GitHub Pages

---

## 本地运行

```bash
# 进入项目目录
cd MindPlace

# 启动本地服务器
python -m http.server 8080

# 浏览器访问
http://localhost:8080/
```

---

## 部署说明

### GitHub Pages 自动部署
- 推送代码到 `main` 分支
- GitHub Actions 自动构建并发布
- 约 1-2 分钟生效

### 手动推送
```bash
git add .
git commit -m "Update description"
git push origin main
```

---

## 农业模型算法特色

新上线的**农业领域模型算法**页面收录了 GitHub 开源社区中的优秀农业AI项目，按四大领域分类：

- 🔬 **植物病害识别**: ResNet、YOLO等深度学习模型
- 📊 **作物产量预测**: 环境因子分析与建模
- 📱 **移动端应用**: 面向农户的移动解决方案
- ⚙️ **部署与工程化**: 生产级部署方案

每个项目包含：
- ✅ 详细的功能介绍
- ✅ 技术栈标签（PyTorch/TensorFlow/FastAPI等）
- ✅ 直达GitHub仓库的链接

---

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建新分支 (`git checkout -b feature/xxx`)
3. 提交更改 (`git commit -m 'Add xxx'`)
4. 推送到分支 (`git push origin feature/xxx`)
5. 创建 Pull Request

---

## 许可证

本项目仅供学习交流使用。

---

> 🌱 **化心为殿，万念不湮** - 让知识在数字世界中永存
