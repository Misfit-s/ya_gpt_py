import requests
import json
from typing import Optional


class AuthData:
    '''Class responsible for requesting and verifying authentication data of Yandex Cloud API.'''
    def Token(iam_token: str = None) -> None:
        '''Function for requesting and verifying the token of Yandex Cloud API.'''
        if not iam_token:
            raise TypeError("It is necessary to specify a IAM token.")
        else:
            return iam_token

    def CatalogID(catalog_id: str = None) -> None:
        '''Function for requesting and verifying the catalouge ID of YandexGPT API.'''
        if not catalog_id:
            raise TypeError("It is necessary to specify a Catalog ID.")
        else:
            return catalog_id


class Messages:
    '''Class responsible for requesting and verifying message data of YandexGPT API.'''
    def system(system_message: Optional[str] = None) -> None:
        '''Function for requesting and verifying the system message of YandexGPT API.'''
        return system_message

    def user(user_message: str = None) -> None:
        '''Function for requesting and verifying the user message of YandexGPT API.'''
        if not user_message:
            raise TypeError("It is necessary to specify a message.")
        else:
            return user_message


class Response:
    """
    Class responsible for generating a request and returning a response from the YandexGPT API.
    
    :param token: Your IAM token
    :param id: YandexGPT folder ID
    :param user_message: Your message to YandexGPT
    :param system_message: System(context) message for YandexGPT
    """
    def getResponse(
        token: str,
        id: str,
        user_message: str,
        system_message: Optional[str] = None,
        max_tokens: Optional[int] = 2000,
        stream: Optional[bool] = False,
        temperature: Optional[float] = 0.6,
    ) -> None:
        '''
        Function responsible for generating a request and returning a response from the YandexGPT API.
        '''
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "x-folder-id": f"{id}",
        }

        data = {
            "modelUri": f"gpt://{id}/yandexgpt-lite",
            "completionOptions": {
                "stream": stream,
                "temperature": temperature,
                "maxTokens": max_tokens,
            },
            "messages": [
                {"role": "system", "text": f"{system_message}"},
                {"role": "user", "text": f"{user_message}"},
            ],
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        return response
