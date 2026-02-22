"""smart-link-controller-iot-vmi - AI Infrastructure Component"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "smart-link-controller-iot-vmi", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
