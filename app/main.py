from fastapi import FastAPI
import uvicorn
from routes import graph_route

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello World!"}

app.include_router(graph_route.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)