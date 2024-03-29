from fastapi import FastAPI, Request
import uvicorn
from backend.database.connection import Settings
from backend.routes import routelist
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


settings=Settings()
app=FastAPI()

app.mount("/static",StaticFiles(directory="backend/static",html=True),name="static")
templates = Jinja2Templates(directory="backend/templates")



@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

@app.get("/")
def root(request:Request)-> dict:
    return templates.TemplateResponse("base.html",
                                      {
                                          "request":request
                                      })
    
    
app.include_router(routelist.card_router,prefix="/card")    
    
    
if __name__ == "__main__":
 uvicorn.run("root:app", host="0.0.0.0", port=8080,reload=True)  