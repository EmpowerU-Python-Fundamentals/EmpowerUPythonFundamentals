import json
from typing import Any

from openai import OpenAI
from openai.types.responses import Response
from django.conf import settings


from .types import PromptType

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class Agent:
    def __init__(self, model: str = settings.OPENAI_MODEL_NAME):
        self._model = model

    def create_response(self, prompt: PromptType) -> Response:
        response = client.responses.create(
            model=self._model,
            instructions=prompt.instructions,
            input=prompt.input,
        )
        return self.prepare_response(response)


    def prepare_response(self, response: Response) -> Any:
        return response.output_text


class PostAgent(Agent):
    def prepare_response(self, response: Response):
        content = response.output_text
        return content


class PlanAgent(Agent):
    def prepare_response(self, response: Response):
        content = response.output_text
        return json.loads(content)



