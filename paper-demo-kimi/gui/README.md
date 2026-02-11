# GUI Orchestrator (Demo)

이 GUI는 대형 워크플로우를 수동 실행/점검하기 위한 최소 오케스트레이터입니다.

## Run
```bash
cd paper-demo-kimi
python3 -m pip install streamlit
streamlit run gui/app.py
```

## What it does
1. RAG 인덱스 빌드
2. Pre-results hypothesis 단계 생성
3. RAG 검색 결과 점검
4. 산출물 미리보기

## Next
- Stage B/C 버튼 추가 (Kimi 호출)
- Figure OCR/Equation parser 상태 패널
- 실행 로그 + 실패 재시도 큐
