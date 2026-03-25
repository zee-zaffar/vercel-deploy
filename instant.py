from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    try:
        return "Live from production!"
    except Exception as e:
        return {"error": str(e)}