"""유틸리티 함수 모음 파일
애플리케이션 전역에서 공용으로 사용하는 헬퍼 함수들이 정의되는 곳
"""
def format_response(status: str, data: dict, message: str = "") -> dict:
    """Format API response"""
    return {
        "status": status,
        "data": data,
        "message": message
    }
