from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from typing import List, Dict, Any

load_dotenv()

app = FastAPI()

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise ValueError("Supabase URL and Anon Key must be set in environment variables")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Cities data
CITIES = [
    { 
        "id": "nyc", 
        "name": "New York City", 
        "lat": 40.7128, "lng": -74.0060, 
        "population": 8400000, 
        "baseline_co2": 50, "baseline_aqi": 60,
    },
    { 
        "id": "ldn", 
        "name": "London", 
        "lat": 51.5074, "lng": -0.1278, 
        "population": 8980000, 
        "baseline_co2": 40, "baseline_aqi": 50,
    },
    { 
        "id": "tok", 
        "name": "Tokyo", 
        "lat": 35.6762, "lng": 139.6503, 
        "population": 13929286, 
        "baseline_co2": 60, "baseline_aqi": 70,
    },
    { 
        "id": "syd", 
        "name": "Sydney", 
        "lat": -33.8688, "lng": 151.2093, 
        "population": 5312000, 
        "baseline_co2": 30, "baseline_aqi": 35,
    },
    { 
        "id": "sp", 
        "name": "São Paulo", 
        "lat": -23.5505, "lng": -46.6333, 
        "population": 12325000, 
        "baseline_co2": 45, "baseline_aqi": 65,
    },
]

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.get("/cities")
def get_cities():
    return {"cities": CITIES}

@app.get("/test-supabase")
def test_supabase():
    try:
        # Test connection by fetching from a table, e.g., if you have a 'test' table
        # For now, just return success
        return {"message": "Supabase connected successfully"}
    except Exception as e:
        return {"error": str(e)}