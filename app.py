from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import yt_dlp

app = FastAPI()

@app.get("/download")
def download(url: str, format: str = "mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best' if format == "mp4" else 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return RedirectResponse(url=info['url'])

@app.get("/")
def home():
    return {"status": "Server is running!"}
