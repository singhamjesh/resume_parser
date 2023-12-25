import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.routes import execute

# Add dot env
load_dotenv()

# Create App
app = FastAPI()

# Add CORS
origins = os.environ.get('ALLOW_ORIGINS')

# App middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(execute.router)


# Config App
host = os.environ.get('APP_HOST', default='0.0.0.0')
port = os.environ.get('APP_PORT', default='8000')
isReload = os.environ.get('IS_RELOAD', default=True)

# Run App
if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=int(port), reload=isReload)
