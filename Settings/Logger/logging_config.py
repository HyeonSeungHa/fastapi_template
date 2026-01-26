"""로거 설정 파일
애플리케이션 전역 로깅 설정 및 logger 인스턴스 생성
"""
import logging
from Settings.Env.env_settings import get_settings

settings = get_settings()

logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
