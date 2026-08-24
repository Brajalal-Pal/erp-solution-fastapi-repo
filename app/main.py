from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv(override=True)
app = FastAPI(title="DevOps Demo API")


@app.get("/")
def root():
    return {
        "message": "DevOps CI/CD Demo",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    import uvicorn as uv
    uv.run("app.main:app", host="127.0.0.1", port=8080, reload=True)


