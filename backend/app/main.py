from fastapi import FastAPI

app = FastAPI(title="Coop Gig Platform")

@app.get("/")
def health():
    return {"status": "ok"}