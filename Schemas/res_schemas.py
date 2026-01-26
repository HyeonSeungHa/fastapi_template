"""응답 스키마 정의 파일
API 응답시 클라이언트에게 반환할 데이터의 형식을 정의
"""
from pydantic import BaseModel
from typing import Optional


class SampleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    status: str = "success"

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "sample_name",
                "description": "sample description",
                "status": "success"
            }
        }
