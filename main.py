"""FastAPI 애플리케이션 진입점
Router들을 모두 import해서 실제 API 서버를 실행하는 메인 파일
"""
from fastapi import FastAPI
from Api.Endpoints.SampleRouter.v1.tasks import router as sample_router

app = FastAPI(title="FastAPI Template")

# Include routers
app.include_router(sample_router, prefix="/api", tags=["sample"])


@app.get("/")
def read_root():
    return {"message": "hello"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
