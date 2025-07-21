# FastMCP Basic Example Server

FastMCP 프레임워크를 사용한 기초 MCP 서버 구현 예제입니다.

## 🚀 Quick Start

### 1. 설치

```bash
# 프로젝트 루트 디렉토리에서
cd examples/fastmcp_basic

# 의존성 설치
uv add fastmcp

# 또는 pip 사용
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
python server.py
```

## 🛠️ 기능

### 도구 (Tools)

#### 계산기 도구
- `add(a, b)`: 두 숫자 더하기
- `subtract(a, b)`: 두 숫자 빼기  
- `multiply(a, b)`: 두 숫자 곱하기
- `divide(a, b)`: 두 숫자 나누기

#### 날씨 도구
- `get_weather(city)`: 도시별 날씨 정보 (목 데이터)
- 지원 도시: seoul, tokyo, newyork, london

#### 파일 읽기 도구
- `read_file(file_path, max_lines)`: 텍스트 파일 읽기
- `list_files(directory_path)`: 디렉토리 파일 목록

#### 텍스트 처리 도구
- `to_uppercase(text)`: 대문자 변환
- `to_lowercase(text)`: 소문자 변환
- `reverse_text(text)`: 텍스트 뒤집기
- `count_words(text)`: 단어/문자 수 세기

### 리소스 (Resources)

- `get_config()`: 서버 설정 정보
- `get_help()`: 일반 도움말
- `get_tool_help(category)`: 도구별 상세 도움말
- `get_logs(max_lines, level)`: 서버 로그

## 📁 프로젝트 구조

```
fastmcp_basic/
├── server.py              # 메인 서버 파일
├── config.json           # 서버 설정
├── requirements.txt      # Python 의존성
├── tools/               # 도구 구현
│   ├── __init__.py
│   ├── calculator.py    # 계산기 도구
│   ├── weather.py       # 날씨 도구
│   ├── file_reader.py   # 파일 읽기 도구
│   └── text_processor.py # 텍스트 처리 도구
├── resources/           # 리소스 구현
│   ├── __init__.py
│   ├── config.py        # 설정 리소스
│   ├── help.py          # 도움말 리소스
│   └── logs.py          # 로그 리소스
└── README.md            # 이 파일
```

## 🔧 VS Code 연동

### 1. MCP 설정 파일 업데이트

`.vscode/mcp.json`에 다음 서버 설정 추가:

```json
{
  "servers": {
    "fastmcp_basic": {
      "type": "stdio",
      "command": "python",
      "args": ["examples/fastmcp_basic/server.py"],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

### 2. VS Code에서 사용

1. **Command Palette** (`Ctrl+Shift+P`) 열기
2. `MCP: Show Installed Servers` 실행하여 서버 확인
3. **Chat View** (`Ctrl+Cmd+I`) 열기
4. **Agent mode** 선택
5. **Tools** 버튼에서 FastMCP 도구들 확인

### 3. 사용 예제

Chat에서 다음과 같이 사용:

```
# 계산하기
10과 5를 더해주세요

# 날씨 조회  
서울 날씨 알려주세요

# 파일 읽기
README.md 파일을 읽어주세요

# 텍스트 처리
"Hello World"를 대문자로 변환해주세요
```

## 🧪 테스트

### 기본 테스트

```bash
# 서버 시작 테스트
python server.py

# 개별 도구 테스트 (Python 인터렉티브 모드)
python -c "
from tools.calculator import CalculatorTool
calc = CalculatorTool()
print(calc.add(10, 5))
"
```

### VS Code Agent Mode 테스트

1. VS Code에서 Agent mode 활성화
2. 각 도구별로 테스트 수행
3. 에러 처리 확인
4. 로그 파일 확인 (`server.log`)

## 🔒 보안

- 파일 접근은 허용된 디렉토리로 제한
- 모든 작업이 로깅됨
- 입력 검증 및 에러 처리 구현
- 안전한 파일 읽기 제한

## 📝 로깅

모든 작업은 `server.log` 파일에 기록됩니다:

```
2025-07-21 10:30:00,123 - tools.calculator - INFO - Calculator: 10 + 5 = 15
2025-07-21 10:30:05,456 - tools.weather - INFO - Weather: Retrieved data for Seoul
```

## 🛠️ 커스터마이징

### 새 도구 추가

1. `tools/` 디렉토리에 새 파일 생성
2. `@tool` 데코레이터로 함수 정의
3. `server.py`에서 도구 등록

### 새 리소스 추가

1. `resources/` 디렉토리에 새 파일 생성  
2. `@resource` 데코레이터로 함수 정의
3. `server.py`에서 리소스 등록

## 🐛 문제 해결

### 자주 발생하는 문제

1. **서버가 시작되지 않음**
   - FastMCP 설치 확인: `pip list | grep fastmcp`
   - Python 버전 확인: 3.8+ 필요

2. **파일을 읽을 수 없음**
   - 파일 경로가 허용된 디렉토리 내에 있는지 확인
   - 파일 권한 확인

3. **VS Code에서 도구가 보이지 않음**
   - MCP 서버 설정 확인
   - 서버 로그 확인
   - VS Code MCP extension 활성화 확인

### 로그 확인

```bash
# 서버 로그 확인
tail -f server.log

# 특정 레벨 로그만 확인
grep ERROR server.log
```

## 🔗 참고 자료

- [FastMCP 공식 문서](https://github.com/jlowin/fastmcp)
- [MCP 사양 문서](https://modelcontextprotocol.io/)
- [VS Code MCP 가이드](https://code.visualstudio.com/docs/copilot/mcp-servers)

## 📄 라이선스

이 예제는 학습 목적으로 제공됩니다.