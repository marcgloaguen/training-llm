import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from langserve import add_routes
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from custom_chain import TranslationChain

parser = StrOutputParser()
model = ChatOllama(model="llama3:8b")

translate_italian = TranslationChain(model,parser).language('italian')

templates = Jinja2Templates(directory="templates")

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

@app.get("/")
async def read_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

add_routes(
    app,
    translate_italian,
    path="/translate_italian",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
