from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.db.session import init_db
from app.routers import auth

app = FastAPI()
init_db()

@app.get("/")
async def read_root():
    # return {"Message": "This app is working!"}
    return RedirectResponse(url="/docs", status_code=302)


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
