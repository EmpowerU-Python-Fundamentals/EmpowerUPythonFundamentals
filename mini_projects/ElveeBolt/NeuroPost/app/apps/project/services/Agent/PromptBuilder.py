import yaml
from django.conf import settings

from .types import PromptType


class PromptBuilder:
    prompt_name: str = None

    def __init__(self):
        self._prompts = self._load_file()

    def build(self, **kwargs) -> PromptType:
        if not self.prompt_name:
            raise ValueError("prompt_name is not set in the subclass")

        if self.prompt_name not in self._prompts:
            raise ValueError(f"Prompt '{self.prompt_name}' not found in YAML")

        raw_prompt = self._prompts.get(self.prompt_name)

        return PromptType(
            instructions=raw_prompt["instructions"].format(**kwargs),
            input=raw_prompt["user"].format(**kwargs),
        )

    @staticmethod
    def _load_file():
        with open(settings.PROMPT_PATH, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


class PlanPromptBuilder(PromptBuilder):
    prompt_name = "create_plan"


class PostPromptBuilder(PromptBuilder):
    prompt_name = "create_post"
