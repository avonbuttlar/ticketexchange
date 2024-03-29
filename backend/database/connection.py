from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from backend.models.card import Card
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings, BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = os.getenv('DATABASE_URL') #Ob das hier richtig ist? :D TODO: Schauen ob das richtig ist.

    async def initialize_database(self):
        if self.DATABASE_URL:
            client = AsyncIOMotorClient(self.DATABASE_URL)
            database_name = "cardDB"  # Specify your database name here
            database = client[database_name]
            await init_beanie(database=database, document_models=[Card])
        else:
            raise ValueError("No DATABASE_URL provided")#

#
class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs


    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()

        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc


    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True