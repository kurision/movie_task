from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import aiohttp

app = FastAPI()
templates = Jinja2Templates(directory="templates")
api_key = "2f9ec8b17725ce7d200b06b69a98ade8"  


@app.get("/")

async def read_root(request: Request):
    # Fetch popular movies from the API
        async with aiohttp.ClientSession() as session:
            url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"
            async with session.get(url) as response:
                data = await response.json()

        movies = data.get("results", [])  # Extract the movie list from the API response
        print(movies)
        return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

