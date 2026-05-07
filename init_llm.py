"""
构造模型方法2：硅基流动
采用统一的init_chat_model方式来初始化各种模型

注意硅基流动上还有v3 给ds官网充值后只能用v4-flash或者pro了
"""
from langchain.chat_models import init_chat_model
from env_utils import SILICONFLOW_API_KEY,SILICONFLOW_BASE_URL

# 硅基流动 API 兼容 OpenAI 协议，必须使用 model_provider="openai"
# 不能使用 model_provider="deepseek"，因为那会连接到 DeepSeek 官方 API

dslm = init_chat_model(
    model_provider="openai",  # 关键：使用 openai provider
    api_key=SILICONFLOW_API_KEY,
    base_url=SILICONFLOW_BASE_URL,
    model="deepseek-ai/DeepSeek-V3"  # 硅基流动的模型名称格式
)

# resp = dslm.invoke("你好，你是什么模型")
# print(resp)

