from pydantic.main import BaseConfig
from pydantic import BaseConfig


def to_camel(string: str) -> str:
    words = string.split("_")
    return string if len(words) <= 1 else words[0] + "".join(word.capitalize() for word in words[1:])


class ModelConfig(BaseConfig):
    alias_generator = to_camel
    allow_population_by_field_name = True
