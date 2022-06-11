from fastapi import FastAPI

# instance of FastAPI
app = FastAPI()

@app.get("/")
def index():
    return 'hey'