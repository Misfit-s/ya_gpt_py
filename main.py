import os
import json
import YaGPT


token = YaGPT.AuthData.Token = os.getenv("YA_IAM_TOKEN")
id = YaGPT.AuthData.CatalogID(os.getenv("YA_FOLDER_ID"))

input_message = input("Input message: ")

message = YaGPT.Messages.user(input_message)

response = YaGPT.Response.getResponse(token, id, message).text

data = json.loads(response)

text = data['result']['alternatives'][0]['message']['text']
input_tokens = data['result']['usage']['inputTextTokens']
completion_tokens = data['result']['usage']['completionTokens']
total_tokens = data['result']['usage']['totalTokens']

print(f'Text: {text}')
print(f'Input tokens: {input_tokens}')
print(f'Answer tokens: {completion_tokens}')
print(f'Total tokens: {total_tokens}')
