import requests
import json

# API_KEY = "填充你应用的API Key"
# SECRET_KEY = "填写你应用的Secret Key"
# 从 config.py 引入
from config import API_KEY,SECRET_KEY  # 导入密钥
 
context_preset = "我想让你充当一个有丰富经验的软件开发工程师。我可能会提供一些关于软件开发的具体问题，这些问题信息可能是需要您修改的有Bug无法运行的程序，也有可能是终端中的报错代码，还有可能是其他相关内容。您的工作是简明扼要地站在初学者的角度，分析程序故障原因，作出修改，并指出错在哪里和为什么这样修改，这可能包括建议代码、代码逻辑思路策略。"
context_code = "以下是报错的代码：" + input("请输入问题代码：")
context_word = "以下是补充描述内容：" + input("请输入补充描述：")
context = context_preset + context_code + context_word

print("正在处理中，请稍后...")

def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
 
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": context
            },
 
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
 
    response = requests.request("POST", url, headers=headers, data=payload)
 
    aso = response.text
    result = json.loads(aso)
    print(result['result'])
 
 
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 
 
if __name__ == '__main__':
    main()