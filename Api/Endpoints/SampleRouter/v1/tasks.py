"""SampleRouter v1 라우터 정의 파일
API 엔드포인트를 정의하고 요청을 받아 서비스 로직으로 처리
"""
from fastapi import APIRouter
from Schemas.req_schemas import SampleRequest
from Schemas.res_schemas import SampleResponse
from Services.SampleService.service_logic import SampleService

router = APIRouter()
service = SampleService()


@router.post("/sample", response_model=SampleResponse)
def create_sample(request: SampleRequest) -> SampleResponse:
    return service.process_sample(request)


@router.get("/sample/{sample_id}", response_model=SampleResponse)
def get_sample(sample_id: int) -> SampleResponse:
    return service.get_sample(sample_id)
