from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Подключаем фронтенд
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/api/anthem")
def get_anthem_data():
    return {"game": "Anthem", "developer": "BioWare", "year": 2019}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
