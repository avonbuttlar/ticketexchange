from typing import List
from beanie import PydanticObjectId
from backend.database.connection import Database
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from backend.models.card import Card, CardUpdate



card_router = APIRouter(tags=["cards"])
card_database = Database(Card)
templates = Jinja2Templates(directory="backend/templates/")


@card_router.post("/")
async def add_card(request: Request, card: Card = Depends(Card.as_form)):   
        await card_database.save(card)
        card = await card_database.get_all()
        return templates.TemplateResponse("cards.html", 
            {
            "request": request,
            "cards": card
            })



@card_router.get("/", response_model=List[Card])
async def retrieve_all_cards(request: Request) -> List[Card]:
    cards = await card_database.get_all()
    return templates.TemplateResponse("cards.html", 
    {
        "request": request,
        "cards": cards
    })


@card_router.get("/{id}", response_model=Card)
async def retrieve_event(id: PydanticObjectId,request: Request) -> Card:
    card = await card_database.get(id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tod with supplied ID does not exist"
        )
    return templates.TemplateResponse("card.html", 
    {
        "request": request,
        "card": card
    })


@card_router.put("/{id}", response_model=Card)
async def update_card(id: PydanticObjectId, body: CardUpdate,) -> Card:
    updated_card = await card_database.update(id, body)
    if not updated_card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card with supplied ID does not exist"
        )
    return updated_card


@card_router.delete("/{id}")
async def delete_card(id: PydanticObjectId) -> dict:
    card = await card_database.delete(id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card with supplied ID does not exist"
        )

    return card_router.get("/")