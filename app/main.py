from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
from app.tokenizer import Tokenizer 

class ToBeTokenized(BaseModel):
    text: str
    lang: Optional[str] = None

app = FastAPI()


@app.post("/tokenizer")
async def feature(item: ToBeTokenized):

    item = jsonable_encoder(item)

    if item["lang"] != None:

        tokenizer = Tokenizer(language = item["lang"])
        tokens = tokenizer.do(item["text"])
        return tokens

    else: 

        tokenizer = Tokenizer(detect_language=True)
        tokens = tokenizer.do(item["text"])
        return tokens


