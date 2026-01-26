# FastAPI Template

간단한 FastAPI 템플릿 프로젝트입니다.

## 빠른 시작

### 1. 가상환경 생성 및 의존성 설치

\`\`\`bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\\Scripts\\activate  # Windows

pip install -r requirements.txt
\`\`\`

### 2. 로컬에서 서버 실행

\`\`\`bash
python main.py
\`\`\`

서버는 http://localhost:8000 에서 실행됩니다.

### 3. API 테스트

#### Root 경로 (hello 반환)
\`\`\`bash
curl http://localhost:8000/
\`\`\`

응답:
\`\`\`json
{"message": "hello"}
\`\`\`

#### Sample API 테스트
\`\`\`bash
curl -X POST http://localhost:8000/api/sample \\
  -H "Content-Type: application/json" \\
  -d '{"name": "test", "description": "test description"}'
\`\`\`

### 4. Docker로 실행

\`\`\`bash
docker-compose up
\`\`\`

## 프로젝트 구조

\`\`\`
fastapi_template/
├── Api/Endpoints/SampleRouter/    # API 라우터
├── Models/                         # 데이터 모델
├── Orm/                           # ORM 설정
├── Schemas/                       # Pydantic 스키마 (요청/응답)
├── Services/                      # 비즈니스 로직
├── Settings/                      # 환경설정, 로거 등
├── Utils/                         # 유틸리티 함수
├── main.py                        # FastAPI 앱 진입점
├── requirements.txt               # 의존성
├── Dockerfile                     # Docker 설정
├── docker-compose.yml             # Docker Compose 설정
└── .env-dev, .env-prod           # 환경변수 파일
\`\`\`

## 주요 파일

- **main.py**: FastAPI 애플리케이션 진입점
- **Api/Endpoints/SampleRouter/v1.py**: 라우터 정의
- **Schemas/**: 요청/응답 스키마 정의
- **Services/**: 비즈니스 로직 구현

## 다음 단계

이 템플릿을 기반으로:
1. 새로운 라우터 추가 (e.g., `PDFRouter`, `GetAddrRouter`)
2. 서비스 로직 구현
3. 데이터베이스 연결 (ORM 설정)
4. 로거 구성
5. 환경 변수 설정

모두 같은 구조로 확장할 수 있습니다!
