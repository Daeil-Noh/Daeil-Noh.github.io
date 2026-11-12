# 양자컴퓨팅·AI 융합연구실 (Quantum Computing·AI Convergence Lab)

https://daeil-noh.github.io

동의대학교 인공지능학과 양자컴퓨팅·AI 융합연구실의 홈페이지 저장소입니다.
양자 컴퓨팅과 인공지능의 접점에서 새로운 학습 모델을 연구하고, 이를 무선 통신과 제조 현장의 실제 문제에 적용합니다.

## 연구 분야

- **양자 컴퓨팅** (Quantum Computing)
- **양자 머신러닝** (Quantum Machine Learning)
- **컴퓨터 비전** (Computer Vision)
- **무선 통신** (Wireless Communication)
- **스마트 팩토리** (Smart Factory)

## 연락처

- 지도교수: 노대일 (Dae-Il Noh), 조교수
- 위치: 부산광역시 부산진구 엄광로 176, 동의대학교 산학협력관 804호
- 이메일: daeil.noh@deu.ac.kr

## 사이트 수정 방법

페이지 내용(구성원, 논문, 특허, 연구 분야)은 `_src/build.py` 한 파일에 모여 있습니다.
내용을 고친 뒤 저장소 루트에서 아래 명령을 실행하면 모든 `*.html` 페이지가 다시 만들어집니다.

```bash
python3 _src/build.py
```

| 폴더·파일 | 내용 |
|---|---|
| `_src/build.py` | 페이지 생성기와 데이터 (STUDENTS, PUBS, CONFS, PATENTS, AREAS) |
| `assets/` | 공통 스타일(`style.css`), 첫 화면 애니메이션, 파비콘 |
| `images/` | 교수·학생 사진, 링크 미리보기 이미지 |
