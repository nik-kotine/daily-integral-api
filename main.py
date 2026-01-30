from fastapi import FastAPI
from datetime import date
import csv

app = FastAPI()

@app.get("/")
def root():
    return { "message" : "Echo!" }

def load_integrals():
    with open("integral-test.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row["integral"] for row in reader]

INTEGRALS = load_integrals()

@app.get("/daily")
def get_daily_integral():
    today_idx = date.today().timetuple().tm_yday - 1
    idx = today_idx % len(INTEGRALS)
    return { "integral" : INTEGRALS[idx], "day" : idx + 1 }
