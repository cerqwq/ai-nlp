"""
AI NLP - AI自然语言处理工具
支持文本分析、情感分析、文本生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AINLPTools:
    """
    AI NLP工具
    支持：分析、情感、生成
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def analyze_text(self, text: str, analysis_type: str) -> Dict:
        """分析文本"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请对以下文本进行{analysis_type}分析：

{text[:2000]}

请返回JSON格式：
{{
    "summary": "总结",
    "key_points": ["要点"],
    "entities": ["实体"],
    "topics": ["主题"],
    "sentiment": "情感"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def sentiment_analysis(self, texts: List[str]) -> List[Dict]:
        """情感分析"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        texts_text = "\n".join(f"{i+1}. {t}" for i, t in enumerate(texts[:10]))

        prompt = f"""请对以下文本进行情感分析：

{texts_text}

请返回JSON格式：
[
    {{"text": "文本", "sentiment": "positive/negative/neutral", "score": 1-10, "keywords": ["关键词"]}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"sentiment": content}]

    def extract_entities(self, text: str, entity_types: List[str]) -> Dict:
        """提取实体"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        types_text = ", ".join(entity_types)

        prompt = f"""请从以下文本中提取{types_text}类型的实体：

{text[:2000]}

请返回JSON格式：
{{
    "entities": [
        {{"text": "实体文本", "type": "类型", "start": 起始位置, "end": 结束位置}}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"entities": content}

    def summarize_text(self, text: str, style: str, length: str) -> str:
        """文本摘要"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请对以下文本进行{style}风格的摘要：

{text[:3000]}

要求：
1. 长度：{length}
2. 保留关键信息
3. 语言流畅"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def classify_text(self, text: str, categories: List[str]) -> Dict:
        """文本分类"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        categories_text = ", ".join(categories)

        prompt = f"""请将以下文本分类到{categories_text}中的一个或多个类别：

{text[:2000]}

请返回JSON格式：
{{
    "categories": ["分类结果"],
    "confidence": {{"类别": 置信度}},
    "reasoning": "分类理由"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"classification": content}

    def generate_text(self, prompt_text: str, style: str, length: str) -> str:
        """生成文本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请以{style}风格生成以下内容：

{prompt_text}

长度：{length}

要求：
1. 语言流畅
2. 逻辑清晰
3. 内容丰富"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def translate_text(self, text: str, source_lang: str, target_lang: str) -> str:
        """翻译文本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下{source_lang}文本翻译成{target_lang}：

{text[:3000]}

要求：
1. 翻译准确
2. 语言自然
3. 保持原意"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AINLPTools:
    """创建NLP工具"""
    return AINLPTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI NLP Tools")
    print()

    # 测试
    analysis = tools.analyze_text("人工智能正在改变世界", "综合")
    print(json.dumps(analysis, ensure_ascii=False, indent=2))
