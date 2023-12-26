import os
import json
from yagpt_py.yagpt_py.response import Response as rp
from yagpt_py.yagpt_py.authData import AuthData as ad
from yagpt_py.yagpt_py.messages import Messages as ms

token = ad.iam_token = (os.getenv("YA_IAM_TOKEN"))
id = ad.catalog_id = (os.getenv("YA_FOLDER_ID"))

input_message = input("Input message: ")

message = ms.user_message_text = input_message

response = rp(token, id, message)

response_text = response.getResponse()

data = json.loads(response_text)

try:
    text = data['result']['alternatives'][0]['message']['text']
    input_tokens = data['result']['usage']['inputTextTokens']
    completion_tokens = data['result']['usage']['completionTokens']
    total_tokens = data['result']['usage']['totalTokens']

    print(f'Text: {text}')
    print(f'Input tokens: {input_tokens}')
    print(f'Answer tokens: {completion_tokens}')
    print(f'Total tokens: {total_tokens}')
    
except KeyError:
    print('Token has been expired.')
    print('Generating new token...')
    os.system('yc iam create-token')
    print('Replace the old token with this new one.')
    
