from flask import Flask, request, jsonify  
from config import API_KEY, SECRET_KEY  
import requests  
import json  
  
app = Flask(__name__)  
  
@app.route('/generate', methods=['POST'])  
def process_request():  
    context_preset = "我想让你充当一个有丰富经验的软件开发工程师。我可能会提供一些关于软件开发的具体问题，这些问题信息可能是需要您修改的有Bug无法运行的程序，也有可能是终端中的报错代码，还有可能是其他相关内容。您的工作是简明扼要地站在初学者的角度，分析程序故障原因，作出修改，并指出错在哪里和为什么这样修改，这可能包括建议代码、代码逻辑思路策略。"  
    context_code = request.json.get('code')  
    context_word = request.json.get('word')  
    context = context_preset + context_code + context_word  
  
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
  
    response = requests.post(url, headers=headers, data=payload)  
    aso = response.text  
    result = json.loads(aso)  
    return jsonify({'result': result})  


def get_access_token():  
    """  
    使用 AK，SK 生成鉴权签名（Access Token）  
    :return: access_token，或是None(如果错误)  
    """  
    url = "https://aip.baidubce.com/oauth/2.0/token"  
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}  
    return str(requests.post(url, params=params).json().get("access_token"))  
  
if __name__ == '__main__':  
    app.run(host='127.0.0.1', port=3000)