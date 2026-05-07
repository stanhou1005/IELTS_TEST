"""
构造模型方法1：
以具体模型自身的结构来构建，而非统一
"""
import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

# 确保加载 .env 文件
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path, override=True)

from langchain_openai import ChatOpenAI

# 验证环境变量
api_key = os.getenv('DEEPSEEK_API_KEY')
base_url = os.getenv('DEEPSEEK_BASE_URL')
print(f"[DEBUG] DEEPSEEK_API_KEY: {api_key[:8]}...{api_key[-4:] if api_key else ''}")
print(f"[DEBUG] DEEPSEEK_BASE_URL: {base_url}")

# 使用 ChatOpenAI 调用硅基流动 API（完全兼容 OpenAI 协议）
# deepseek = ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V3",  # 不需要 openai/ 前缀
#     api_key=api_key,
#     base_url=base_url,
# )

# 这个也是deepseek-v4-flash
deepseek = ChatDeepSeek(
    model="deepseek-chat",  # 不需要 openai/ 前缀
    api_key=api_key,
    base_url=base_url,
)

# 使用dp的推理模型
llm = ChatDeepSeek(
    model="deepseek-reasoner",  # 关键配置，注意后续这个改名为deepseek-v4-flash，也具有推理能力
    temperature=0,               # 推荐设为0以获得确定性结果
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=api_key,
    base_url=base_url,
)

def get_llm():
    return deepseek

def get_reasoner():
    return llm

"""测试"""
print(f"模型为：{deepseek.model}")
resp = deepseek.invoke("你好，你是什么模型?是否具有推理能力？")
print(type(resp))
#回答就是下方一大段 说自己为deepseek-chat模型 但是实际上他模型名称为deepseek-ai/DeepSeek-V3
print(resp.response_metadata['model_name'])
print(resp)
"""
输出
<class 'langchain_core.messages.ai.AIMessage'>
content='你好！我是 **DeepSeek Chat**，由 **深度求索（DeepSeek）** 研发的 **大语言模型（LLM）**。
目前我的版本是 **DeepSeek-V3**，知识更新至 **2024年7月**，具备较强的文本理解和生成能力，可以支持 **128K 上下文**，还能处理包括 **TXT、PDF、PPT、Word、Excel** 在内的多种文件内容，并为你解答问题、提供分析和建议。
  \n\n我是 **免费** 的，不进行语音交互，主要擅长以文本方式和你交流。如果你有任何问题，欢迎随时向我提问！😊' 
  additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 135, 'prompt_tokens': 8, 'total_tokens': 143, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_provider': 'openai', 'model_name': 'deepseek-ai/DeepSeek-V3', 'system_fingerprint': '', 'id': '019de6800a6193520e3b58a0ec274736', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019de680-052a-7663-a991-074cd7501bf4-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 8, 'output_tokens': 135, 'total_tokens': 143, 'input_token_details': {}, 'output_token_details': {}}

"""