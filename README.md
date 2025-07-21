# Let's Learn MCP 🚀

MCP(Model Context Protocol) 학습을 위한 한국어 프로젝트입니다.

## 📋 프로젝트 개요

이 프로젝트는 MCP(Model Context Protocol)를 배우고 실습하기 위한 종합적인 학습 리소스를 제공합니다. FastMCP 프레임워크를 사용한 실제 동작하는 서버 예제와 VS Code 연동까지 포함하고 있습니다.

## 🎯 주요 기능

### ✅ FastMCP 서버 예제
- **계산기 도구**: 사칙연산 (덧셈, 뺄셈, 곱셈, 나눗셈)
- **날씨 조회**: 4개 도시 목 데이터 (서울, 도쿄, 뉴욕, 런던)
- **파일 읽기**: 안전한 파일 접근 및 디렉토리 목록
- **텍스트 처리**: 대소문자 변환, 텍스트 뒤집기, 단어 수 세기

### ✅ VS Code 통합
- MCP 서버 자동 설정
- Agent Mode에서 도구 사용 가능
- 자연어로 도구 제어

### ✅ 완전한 문서화
- 단계별 설치 가이드
- 사용법 예제
- 문제 해결 가이드

## 📁 프로젝트 구조

```
letslearnmcp/
├── 📁 .vscode/
│   └── mcp.json                    # MCP 서버 설정
├── 📁 .github/
│   └── ISSUE_TEMPLATE/             # GitHub 이슈 템플릿
├── 📁 examples/
│   ├── README.md                   # 예제 개요
│   └── 📁 fastmcp_basic/          # FastMCP 서버 예제
│       ├── server.py               # 메인 서버 파일
│       ├── config.json             # 서버 설정
│       ├── requirements.txt        # Python 의존성
│       ├── 📁 tools/              # 도구 구현
│       │   ├── calculator.py       # 계산기 도구
│       │   ├── weather.py          # 날씨 도구
│       │   ├── file_reader.py      # 파일 읽기 도구
│       │   └── text_processor.py   # 텍스트 처리 도구
│       ├── 📁 resources/          # 리소스 구현
│       │   ├── config.py           # 설정 리소스
│       │   ├── help.py             # 도움말 리소스
│       │   └── logs.py             # 로그 리소스
│       └── README.md               # 상세 사용 가이드
├── main.py                         # 기본 Python 파일
├── pyproject.toml                  # 프로젝트 설정 및 의존성
├── .gitignore                      # Git 무시 파일
└── README.md                       # 이 파일
```

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 1. 리포지토리 클론
git clone https://github.com/corazzon/letslearnmcppy.git
cd letslearnmcppy

# 2. uv 설치 (없는 경우)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. 가상환경 생성 및 활성화
uv venv
source .venv/bin/activate  # macOS/Linux
# Windows: .venv\Scripts\activate

# 4. 의존성 설치
uv pip install -e .
```

### 2. FastMCP 서버 실행

```bash
# FastMCP 서버 디렉토리로 이동
cd examples/fastmcp_basic

# 서버 실행
python server.py
```

### 3. VS Code에서 사용

1. **VS Code 열기**: 프로젝트 루트에서 `code .`
2. **MCP 서버 확인**: `Ctrl+Shift+P` → `MCP: Show Installed Servers`
3. **Chat 열기**: `Ctrl+Cmd+I` (Mac) / `Ctrl+Alt+I` (Windows)
4. **Agent Mode 선택**: Chat 창에서 Agent mode 활성화
5. **도구 사용**: 자연어로 도구 사용 가능

## 💬 사용 예제

VS Code Chat에서 다음과 같이 사용할 수 있습니다:

```
# 계산하기
10과 5를 더해주세요

# 날씨 조회
서울의 날씨를 알려주세요

# 파일 읽기
README.md 파일을 읽어주세요

# 텍스트 처리
"안녕하세요"를 대문자로 변환해주세요

# 도움말 보기
사용 가능한 도구들을 보여주세요
```

## 🛠️ 개발 환경 설정

### 개발 의존성 설치

```bash
uv pip install -e ".[dev]"
```

### 포함된 개발 도구
- **pytest**: 테스트 프레임워크
- **black**: 코드 포매터
- **flake8**: 린터
- **mypy**: 타입 체커

## 🔧 MCP 서버 구성

현재 프로젝트에 설정된 MCP 서버들:

### 🔵 활성화된 서버
- **fastmcp_basic**: 자체 제작 FastMCP 예제 서버
- **github**: GitHub API 접근
- **fileSystem**: 파일 시스템 접근

### 🟡 추가 설정 가능한 서버
- **perplexity**: AI 검색 (API 키 필요)
- **fetch**: HTTP 요청
- **brave**: Brave 검색 (API 키 필요)
- **memory**: 메모리 관리

## 📚 학습 리소스

### 🎓 단계별 학습
1. **MCP 기본 개념**: [MCP 공식 문서](https://modelcontextprotocol.io/) 읽기
2. **FastMCP 실습**: `examples/fastmcp_basic/` 폴더의 코드 분석
3. **VS Code 연동**: Agent Mode에서 도구 사용해보기
4. **커스텀 도구 개발**: 새로운 도구 추가해보기

### 📖 참고 자료
- [MCP 사양 문서](https://modelcontextprotocol.io/)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)
- [VS Code MCP 가이드](https://code.visualstudio.com/docs/copilot/mcp-servers)

## 🔒 보안 기능

- **파일 접근 제한**: 허용된 디렉토리로만 접근 가능
- **입력 검증**: 모든 사용자 입력에 대한 검증
- **에러 처리**: 안전한 에러 처리 및 로깅
- **로깅**: 모든 활동 상세 기록

## 🐛 문제 해결

### 자주 발생하는 문제

1. **서버가 시작되지 않음**
   ```bash
   # Python 버전 확인 (3.8+ 필요)
   python --version
   
   # FastMCP 설치 확인
   pip list | grep fastmcp
   ```

2. **VS Code에서 도구가 보이지 않음**
   - MCP extension 활성화 확인
   - `.vscode/mcp.json` 파일 확인
   - VS Code 재시작

3. **파일 읽기 권한 오류**
   - 파일 경로가 허용된 디렉토리 내에 있는지 확인
   - 파일 권한 확인

### 로그 확인

```bash
# 서버 로그 실시간 확인
tail -f examples/fastmcp_basic/server.log

# 에러 로그만 확인
grep ERROR examples/fastmcp_basic/server.log
```

## 🤝 기여하기

1. **Fork** 이 리포지토리
2. **Feature branch** 생성: `git checkout -b feature/새기능`
3. **커밋**: `git commit -am '새 기능 추가'`
4. **Push**: `git push origin feature/새기능`
5. **Pull Request** 생성

## 📄 라이선스

이 프로젝트는 학습 목적으로 제공됩니다.

## 📞 지원

- **GitHub Issues**: 버그 리포트 및 기능 요청
- **GitHub Discussions**: 질문 및 토론

---

**Happy Learning MCP! 🎉**