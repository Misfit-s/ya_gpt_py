import os
import json
import YaGPT


token = YaGPT.AuthData.Token = os.getenv("YA_IAM_TOKEN")
id = YaGPT.AuthData.CatalogID(os.getenv("YA_FOLDER_ID"))

input_message = input("Введите сообщение: ")

message = YaGPT.Messages.user(input_message)

response = YaGPT.Response.getResponse(token, id, message).text

data = json.loads(response)

text = data['result']['alternatives'][0]['message']['text']
input_tokens = data['result']['usage']['inputTextTokens']
completion_tokens = data['result']['usage']['completionTokens']
total_tokens = data['result']['usage']['totalTokens']

print(f'Текст: {text}')
print(f'Токены ввода: {input_tokens}')
print(f'Токены ответа: {completion_tokens}')
print(f'Всего токенов: {total_tokens}')
