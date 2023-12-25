import requests
import json
from typing import Optional


class AuthData:
    def Token(iam_token: str = None) -> None:
        if not iam_token:
            raise TypeError("It is necessary to specify a IAM token.")
        else:
            return iam_token

    def CatalogID(catalog_id: str = None) -> None:
        if not catalog_id:
            raise TypeError("It is necessary to specify a Catalog ID.")
        else:
            return catalog_id


class Messages:
    def system(system_message: Optional[str] = None) -> None:
        return system_message

    def user(user_message: str = None) -> None:
        if not user_message:
            raise TypeError("It is necessary to specify a message.")
        else:
            return user_message


class Response:
    def getResponse(
        token: str,
        id: str,
        user_message: str,
        system_message: Optional[str] = None,
        max_tokens: Optional[int] = 2000,
        stream: Optional[bool] = False,
        temperature: Optional[float] = 0.6,
    ) -> None:
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
