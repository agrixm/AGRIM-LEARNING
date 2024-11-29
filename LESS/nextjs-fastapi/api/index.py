from fastapi import FastAPI
from pydantic import BaseModel
import instaloader

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

class ProfileRequest(BaseModel):
    username: str

@app.post("/api/py/profile-pic")
def get_profile_pic(request: ProfileRequest):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, request.username)
    profile_pic_url = profile.profile_pic_url
    return {"profile_pic_url": profile_pic_url}