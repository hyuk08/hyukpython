# hyukpython 프로젝트

Python을 활용한 웹 크롤링, 데이터 분석, 머신러닝 프로젝트 모음입니다.

## 🚀 시작하기

### 필수 요구사항
- Python 3.8 이상
- pip 또는 conda

### 설치 방법

#### 1. 저장소 클론
```bash
git clone https://github.com/your-username/hyukpython.git
cd hyukpython
```

#### 2. 가상환경 생성 및 패키지 설치

**방법 A: pipenv 사용 (권장)**
```bash
# pipenv 설치 (없는 경우)
pip install pipenv

# 가상환경 생성 및 패키지 설치
pipenv install

# 가상환경 활성화
pipenv shell
```

**방법 B: venv 사용**
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt
```

**방법 C: conda 사용**
```bash
conda create -n hyukpython python=3.8
conda activate hyukpython
pip install -r requirements.txt
```

## 📦 주요 라이브러리

- **requests**: HTTP 요청 및 웹 크롤링
- **beautifulsoup4**: HTML/XML 파싱
- **pandas**: 데이터 분석 및 CSV 처리
- **lxml**: XML/HTML 파서

전체 목록은 `requirements.txt`를 참고하세요.

## 🖥️ 운영체제별 주의사항

### Windows 사용자

1. **파일 인코딩**
   - 일부 파일에서 `encoding='cp949'`를 사용하는 경우가 있습니다
   - UTF-8로 변경하려면 코드를 수정하세요

2. **경로 구분자**
   - 코드는 상대 경로를 사용하므로 대부분 문제없습니다
   - 절대 경로를 사용하는 경우 `os.path.join()`을 사용하세요

3. **Python 인터프리터 선택**
   - Cursor/VS Code에서 Python 인터프리터를 선택할 때
   - Windows에서는 `C:\Users\사용자명\Anaconda3\python.exe` 같은 경로가 표시됩니다

### macOS/Linux 사용자

- 대부분의 코드가 바로 작동합니다
- conda 환경을 사용하는 경우 경로가 자동으로 감지됩니다

## 📁 프로젝트 구조

```
hyukpython/
├── item/              # 웹 크롤링 관련 스크립트
├── backup/            # 백업 파일들
├── creative_computing/ # p5.js 관련 프로젝트
├── vibe_coding/       # Python 데모 코드
├── requirements.txt   # Python 패키지 목록
└── Pipfile           # pipenv 설정 파일
```

## 🔧 문제 해결

### 패키지 설치 오류
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 인코딩 오류 (Windows)
- 파일을 열 때 `encoding='utf-8'` 또는 `encoding='cp949'`를 명시하세요
- 한글 파일명이 있는 경우 주의하세요

### 가상환경 활성화 안 됨
```bash
# pipenv
pipenv --rm
pipenv install

# venv
rm -rf venv  # 또는 Windows: rmdir /s venv
python -m venv venv
```

## 📝 라이선스

이 프로젝트는 개인 학습용으로 제작되었습니다.

