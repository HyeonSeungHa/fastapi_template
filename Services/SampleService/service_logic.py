"""SampleService 비즈니스 로직 파일
Router에서 받은 요청을 처리하는 비즈니스 로직이 구현되는 곳
"""
from Schemas.req_schemas import SampleRequest
from Schemas.res_schemas import SampleResponse


class SampleService:
    """Sample service logic"""

    def process_sample(self, request: SampleRequest) -> SampleResponse:
        """Process sample request"""
        return SampleResponse(
            id=1,
            name=request.name,
            description=request.description,
            status="success"
        )

    def get_sample(self, sample_id: int) -> SampleResponse:
        """Get sample by id"""
        return SampleResponse(
            id=sample_id,
            name="sample_name",
            description="sample description",
            status="success"
        )
