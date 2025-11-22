from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Koleksi Kalpataru API", version="1.0.0")

# CORS for frontend preview
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    status: str
    brand: str
    message: str


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok", brand="Koleksi Kalpataru", message="Service is alive")


@app.get("/seo/keywords")
async def seo_keywords() -> Dict[str, list]:
    return {
        "long_tail": [
            "Bakpia Jogja di Malang",
            "Tiramisusu Malang",
            "Oleh-oleh Premium Malang",
            "Pie Susu Bali di Malang",
            "Falala Chocolate Bali Malang",
        ]
    }
