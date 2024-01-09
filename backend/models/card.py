from beanie import Document
from fastapi import Form
from pydantic import BaseModel

class Card(Document):
    user:str
    type:str
    block:str
    seat:str
    description:str
    
    class Config:
        schema_extra={
            "example":{
                "user":"AvB",
                "type":"Stehblock",
                "block":"51a",
                "seat":"31",
                "description":"Nur Tausch"
            }
        }
    
    @classmethod
    def as_form(cls,user:str=Form(...),type:str=Form(...),block:str=Form(...),seat:str=Form(...),description:str=Form(...)):
        return cls(user=user,type=type,block=block,seat=seat,description=description)
            
 

class CardUpdate(BaseModel):
    user:str
    type:str
    block:str
    seat:str
    description:str
    
    class Config:
        schema_extra={
            "example":{
                "user":"Mehdi",
                "type":"Stehblock",
                "block":"51a",
                "seat":"31",
                "description":"Tausch oder verkauf"
            }
        }             