from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def main():
    return {"class": "wednesday dev container one"}