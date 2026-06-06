# 📝 AI NLP

AI自然语言处理工具，支持文本分析、情感分析、文本生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📊 文本分析
- 💭 情感分析
- 🏷️ 实体提取
- 📝 文本摘要
- 📂 文本分类
- ✍️ 文本生成
- 🌐 文本翻译

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_nlp import create_tools

tools = create_tools()

# 文本分析
analysis = tools.analyze_text(text, "综合")

# 情感分析
sentiment = tools.sentiment_analysis(["好评", "差评"])

# 实体提取
entities = tools.extract_entities(text, ["人名", "地点"])

# 文本摘要
summary = tools.summarize_text(text, "简洁", "100字")

# 文本分类
classification = tools.classify_text(text, ["科技", "娱乐", "体育"])

# 文本生成
generated = tools.generate_text("写一篇关于AI的文章", "专业", "500字")

# 翻译
translated = tools.translate_text(text, "中文", "英文")
```

## 📁 项目结构

```
ai-nlp/
├── tools.py       # NLP工具核心
└── README.md
```

## 📄 许可证

MIT License
