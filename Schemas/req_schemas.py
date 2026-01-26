"""요청 스키마 정의 파일
API 요청시 클라이언트로부터 받을 데이터의 형식을 정의
"""
from pydantic import BaseModel
from typing import Optional


class SampleRequest(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "sample_name",
                "description": "sample description"
            }
        }
