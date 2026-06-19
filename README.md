# 每日文献追踪报告

自动从 arXiv + Semantic Scholar 检索计算化学/电催化领域最新论文，生成结构化精读报告并部署到 GitHub Pages。

## 工作流程

1. **每日定时运行**（北京时间 09:00, GitHub Actions cron）
2. 读取 `keywords.json` 搜索主题
3. 检索 arXiv + Semantic Scholar
4. 自动去重（跨天）
5. PDF 下载 + 文本提取
6. LLM 生成 8 模块结构化摘要 + 亮点/Key Gap 分析
7. 生成 HTML 报告并推送至 GitHub Pages

也可手动触发：GitHub → Actions → Daily Literature Review → Run workflow

## 修改搜索配置

编辑仓库内的 `keywords.json` 即可，下次运行时自动生效。

**直接在 GitHub Web UI 修改：**
1. 打开仓库的 `keywords.json` 文件
2. 点击铅笔图标 ✏️ 开始编辑
3. 修改后填写 Commit message → **Commit changes**

### keywords.json 完整结构

```json
{
  "_comment": "搜索主题列表，每行一个关键词/短语",
  "topics": [
    "machine learning force field",
    "neural network potential"
  ],
  "arxiv": {
    "enabled": true,
    "max_results": 10
  },
  "semantic_scholar": {
    "enabled": true,
    "query_a_limit": 30,
    "query_b_limit": 20,
    "fields_of_study": ["Chemistry", "Physics", "Materials Science", "Computer Science"],
    "year_range": "2023-"
  }
}
```

### 配置项说明

| 字段 | 说明 | 默认值 |
|------|------|--------|
| `topics` | 搜索主题列表，每个字符串一个关键词 | - |
| `arxiv.enabled` | 是否检索 arXiv | `true` |
| `arxiv.max_results` | arXiv 最大返回篇数 | `10` |
| `semantic_scholar.enabled` | 是否检索 Semantic Scholar | `true` |
| `semantic_scholar.query_a_limit` | S2 第一次查询返回篇数 | `30` |
| `semantic_scholar.query_b_limit` | S2 第二次查询返回篇数 | `20` |
| `semantic_scholar.fields_of_study` | 限制 S2 研究领域 | `["Chemistry", "Physics", "Materials Science", "Computer Science"]` |
| `semantic_scholar.year_range` | 限制 S2 出版年份范围 | `"2023-"`（2023 至今） |

### 修改 fields_of_study 和 year_range

这两个字段在 `keywords.json` 的 `semantic_scholar` 下：

- **`fields_of_study`**: S2 允许的领域值包括 `"Computer Science"`, `"Chemistry"`, `"Physics"`, `"Materials Science"`, `"Medicine"`, `"Biology"`, `"Engineering"`, `"Mathematics"` 等
- **`year_range`**: 格式如 `"2023-"`（2023 至今）、`"2024-2025"`（区间）、`"-2023"`（2023 之前）

### 通过 GitHub Issues 添加关键词

同事无需编辑代码，直接在仓库提交 Issue：
1. 仓库页面 → Issues → New Issue → 选择 **关键词建议** 模板
2. 填写关键词/短语 → Submit
3. 下次运行时自动纳入搜索

## GitHub Secrets 配置

以下 Secrets 需要在仓库 Settings → Secrets and variables → Actions 中配置：

| Secret | 必需 | 说明 | 获取方式 |
|--------|------|------|----------|
| `S2_API_KEY` | 否 | Semantic Scholar API Key（提高速率限制） | https://api.semanticscholar.org/api-docs/#authentication |
| `LLM_API_KEY` | 否 | DashScope/OpenAI 兼容 API Key（用于摘要生成） | https://bailian.console.aliyun.com/ |
| `LLM_MODEL` | 否 | LLM 模型名，默认 `qwen-plus` | 可选 `qwen-max`, `gpt-4o` 等 |
| `LLM_BASE_URL` | 否 | API 地址，默认阿里云 DashScope | 改用 OpenAI 时设为 `https://api.openai.com/v1` |

未配置 LLM 时，报告会使用论文原始摘要作为代替，亮点/Key Gap 显示占位符。

## 项目结构

```
.
├── .github/
│   ├── workflows/daily-review.yml   # GitHub Actions 工作流
│   └── ISSUE_TEMPLATE/              # Issue 模板
├── keywords.json                    # 搜索关键词 + 配置（核心！）
├── pipeline.py                      # 检索→精读→报告主脚本
├── generate_site.py                 # 从 markdown 报告生成 HTML 站点
├── requirements.txt                 # Python 依赖
├── seen_papers.json                 # 已读论文缓存（自动维护）
├── reports/                         # 每日 markdown 报告
├── pdfs/                            # 已下载的 PDF
└── index.html + daily-*.html        # 生成的 HTML 站点（GitHub Pages）
```

## GitHub Pages

站点地址：https://yx-yuanpei.github.io/daily-review-reports/

部署配置：Settings → Pages → Source: **Deploy from branch**, Branch: **main**, Directory: **/** (root)
