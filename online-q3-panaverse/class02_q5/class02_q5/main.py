from fastapi import FastAPI

app = FastAPI()

# req aye ge get method sa fast api ka server pr index func chal jaye ga
@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/piaic/")
def piaic():
    return {"organization": "Piaic"}