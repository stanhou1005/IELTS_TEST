import os
from dotenv import load_dotenv
#从env文件中加载环境变量
load_dotenv(override=True)
###也可以显示地指定
#load_dotenv(dotenv_path='/path/to/.env')

###如果有多种类型的环境：
# 先加载默认配置
#load_dotenv()

# 根据 ENV 变量加载特定环境配置
#env = os.getenv('ENV', 'development')
#if env == 'production':
#    load_dotenv('.env.production', override=True)
#elif env == 'test':
#    load_dotenv('.env.test', override=True)
###
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")
SILICONFLOW_BASE_URL = os.getenv("SILICONFLOW_BASE_URL")

# Tavily Search API 配置（用于网络搜索功能）
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

"""
	注释内容 1
	注释内容 2
	注释内容 3
"""