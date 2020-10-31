from pydantic import BaseModel, Field
from typing import Optional
from app.core.models.config_base import ModelConfig
from bson import ObjectId

id_description = "The Id of the text in the database."
text_description = "The text to be used to train the spam filter."
is_spam_description = "Indicates whether the text should be considering as a spam or not when training the spam filter."


class TrainingTextBase(BaseModel):
    class Config(ModelConfig):
        pass


class TrainingText(TrainingTextBase):
    id: str = Field(..., min_length=24, max_length=24, description=id_description)
    text: str = Field(..., description=text_description)
    is_spam: bool = Field(..., description=is_spam_description)

    def __init__(self, _id: ObjectId = None, **fields) -> None:
        if (_id != None):
            fields["id"] = str(_id)

        super().__init__(**fields)


class TrainingTextInCreate(TrainingTextBase):
    text: str = Field(..., description=text_description)
    is_spam: bool = Field(..., description=is_spam_description)


class TrainingTextInUpdate(TrainingTextBase):
    id: str = Field(..., min_length=24, max_length=24, description=id_description)
    text: Optional[str] = Field(None, description=text_description)
    is_spam: Optional[bool] = Field(None, description=is_spam_description)
