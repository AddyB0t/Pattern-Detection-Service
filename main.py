from fastapi import FastAPI
from functioncaller.Function_router import router
from functioncaller.database import engine
from functioncaller import model
import uvicorn

# Create database tables
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Pattern Detection Service. POST a file to /api/upload to detect patterns like PAN numbers, contact numbers, driving license numbers, and registration numbers."}














if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)





