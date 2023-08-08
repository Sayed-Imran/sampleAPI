from fastapi import FastAPI
import httpx
from schema import Image
from typing import List
from dotenv import load_dotenv
from config import API_Key


app = FastAPI()


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

if __name__ == "__main__":
    load_dotenv()