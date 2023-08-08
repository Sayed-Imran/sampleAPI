from fastapi import FastAPI, Request
from jinja2 import FileSystemLoader, Environment
import httpx
from dotenv import load_dotenv
load_dotenv()
from schema import Image
from typing import List
from config import API_Key
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/{query}")
async def collage(request: Request,query:str):
    
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {API_Key.unsplash_access_key}"
    }
    params = {
        "query": query
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response_data = response.json()
    env = Environment(loader=FileSystemLoader("."), autoescape=True)
    template = env.get_template("templates/index.html.j2")

    variables = {
        f"IMAGE_{index + 1}": json_obj['urls']['full']
        for index, json_obj in enumerate(response_data.get("results")[:-1])
    }
    print(variables)
    with open("templates/index.html", "w") as fh:
        fh.write(template.render(variables))
    return templates.TemplateResponse("index.html", {"request": request})
    

@app.get("/search-photos", response_model=List)
async def search_photos(query: str):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {API_Key.unsplash_access_key}"
    }
    params = {
        "query": query
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response_data = response.json()
    print(response_data.keys())
    return [Image(**data) for data in response_data.get("results")]
