"""연구실 홈페이지 생성기.

공통 머리글·바닥글과 데이터(연구 분야, 논문)를 한곳에 두고 페이지별 HTML을 만든다.
수정 후 저장소 루트에서 `python3 _src/build.py` 를 실행하면 *.html 이 다시 만들어진다.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://daeil-noh.github.io"
LAB_KO = "양자컴퓨팅·AI 융합연구실"
LAB_EN = "Quantum Computing·AI Convergence Lab"
EMAIL = "daeil.noh@deu.ac.kr"
SCHOLAR = "https://scholar.google.com/citations?user=Ttsq5WkAAAAJ&hl=ko"
ORCID = "https://orcid.org/0000-0002-6586-5780"

PAGES = [  # (파일, 메뉴 이름)
    ("index.html", "Home"),
    ("research.html", "Research"),
    ("people.html", "People"),
    ("publications.html", "Publications"),
    ("contact.html", "Contact"),
]

ICONS = {
    "qc": '<circle cx="12" cy="12" r="2"/><ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"/>',
    "qml": '<circle cx="5" cy="6" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="19" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><path d="M7 6l3 5M7 18l3-5M14 12h3"/>',
    "cv": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "wc": '<path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/><path d="M1.5 9a15 15 0 0 1 21 0"/>',
    "sf": '<path d="M2 20V9l6 4V9l6 4V5h8v15z"/><path d="M6 17h2M11 17h2M16 17h2"/>',
}

def icon(key, size=22):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" aria-hidden="true">{ICONS[key]}</svg>')

AREAS = [
    dict(id="quantum-computing", icon="qc", ko="양자 컴퓨팅", en="Quantum Computing",
         short="양자 회로와 양자 어닐링으로 기존 컴퓨터가 풀기 어려운 최적화 문제를 효율적으로 해결합니다.",
         body="양자 컴퓨터는 중첩과 얽힘을 이용해 고전 컴퓨터와 다른 방식으로 계산합니다. 연구실은 이 특성을 실제 공학 문제의 최적화에 활용하는 방법을 연구합니다.",
         topics=["양자 어닐링 기반 조합 최적화", "무선 네트워크 자원 할당 문제의 양자 최적화 모델링", "양자 회로 설계와 시뮬레이션"],
         tag="Quantum Computing"),
    dict(id="quantum-ml", icon="qml", ko="양자 머신러닝", en="Quantum Machine Learning",
         short="변분 양자 회로(VQC)와 신경망을 결합한 하이브리드 양자-고전 모델을 설계합니다.",
         body="양자 회로를 학습 가능한 모델로 사용하는 양자 머신러닝은 적은 파라미터로 복잡한 표현을 학습할 가능성이 있습니다. 연구실은 고전 딥러닝 구조와 양자 회로를 결합한 하이브리드 모델을 연구합니다.",
         topics=["변분 양자 회로(VQC) 기반 분류 모델", "하이브리드 양자-고전 신경망 구조 설계", "시계열·이미지 데이터 분류 응용"],
         tag="Quantum ML"),
    dict(id="computer-vision", icon="cv", ko="컴퓨터 비전", en="Computer Vision",
         short="Transformer 기반 비전 모델로 의료 영상 분석, 객체 검출·분할 문제를 연구합니다.",
         body="영상에서 의미 있는 정보를 찾아내는 컴퓨터 비전 기술을 의료와 산업 현장에 적용합니다.",
         topics=["Transformer 기반 영상 분류·분할", "의료 영상 질환 검출", "객체 검출과 영상 분할"],
         tag="Computer Vision"),
    dict(id="wireless", icon="wc", ko="무선 통신", en="Wireless Communication",
         short="자동 변조 분류, RF 기반 UAV 탐지 등 AI for Wireless 연구를 수행합니다.",
         body="무선 신호와 네트워크 문제에 딥러닝을 적용해 기존 신호처리 방법의 한계를 넘는 것을 목표로 합니다.",
         topics=["딥러닝 기반 자동 변조 분류(AMC)", "RF 신호 기반 UAV 탐지·분류", "다중 UAV 무선 네트워크 최적화"],
         tag="Wireless"),
    dict(id="smart-factory", icon="sf", ko="스마트 팩토리", en="Smart Factory",
         short="제조 현장의 센서·영상 데이터를 AI로 분석해 품질 검사와 이상 탐지에 활용합니다.",
         body="제조 데이터와 AI를 결합해 생산 현장의 품질과 효율을 높이는 응용 연구를 진행합니다.",
         topics=["영상 기반 제품 품질 검사", "센서 데이터 이상 탐지", "공정 데이터 분석과 최적화"],
         tag=None),
]

PUBS = [
    dict(year=2026, title="Embedding-aware noise modeling of quantum annealing",
         authors="Seon-Geun Jeong, Dinh Cong Mai, <b>Dae-Il Noh</b>, Quoc-Viet Pham, Won-Joo Hwang",
         venue="Quantum Information Processing", doi="10.1007/s11128-026-05293-z", tag="Quantum Computing"),
    dict(year=2026, title="Improving performance of asynchronous pulse code multiple access by machine learning-based pulse detection",
         authors="Mayu Horiuchi, Takuya Fujiwara, Ferdinand Peper, Kenji Leibnitz, Naoki Wakamiya, Maki Arai, <b>Dae-Il Noh</b>, Won-Joo Hwang, Jin Nakazato, Mikio Hasegawa",
         venue="Nonlinear Theory and Its Applications, IEICE (NOLTA)", doi="10.1587/nolta.17.1241", tag="Wireless"),
    dict(year=2026, title="GlaucoFormer: A transformer-based model for glaucoma detection and segmentation",
         authors="<b>Dae-Il Noh</b>, Thien-Thanh Dao, Kyeong-Min Park, Seon-Geun Jeong, Won-Joo Hwang",
         venue="Applied Soft Computing", doi="10.1016/j.asoc.2026.115158", tag="Computer Vision"),
    dict(year=2025, title="Hybrid Quantum ResNet for Time Series Classification",
         authors="<b>Dae-Il Noh</b>, Seon-Geun Jeong, Won-Joo Hwang",
         venue="IEEE Transactions on Emerging Topics in Computing", doi="10.1109/TETC.2025.3563944", tag="Quantum ML"),
    dict(year=2025, title="Quantum-Annealing-Based Sum Rate Maximization for Multi-UAV-Aided Wireless Networks",
         authors="Seon-Geun Jeong, Pham Dang Anh Duc, Quang Vinh Do, <b>Dae-Il Noh</b>, Nguyen Xuan Tung, Trinh Van Chien, Quoc-Viet Pham, Mikio Hasegawa, Hiroo Sekiya, Won-Joo Hwang",
         venue="IEEE Internet of Things Journal", doi="10.1109/JIOT.2025.3546645", tag="Quantum Computing"),
    dict(year=2024, title="VT-MCNet: High-Accuracy Automatic Modulation Classification Model Based on Vision Transformer",
         authors="Thien-Thanh Dao, <b>Dae-Il Noh</b>, Quoc-Viet Pham, Mikio Hasegawa, Hiroo Sekiya, Won-Joo Hwang",
         venue="IEEE Communications Letters", doi="10.1109/LCOMM.2023.3336985", tag="Wireless"),
    dict(year=2024, title="O2O 서비스를 통한 고혈압, 당뇨 관리 모델 개발",
         authors="이상민, 천동훈, <b>노대일</b>, 박진우, 김윤지, 김영기, 황원주, 강동묵",
         venue="멀티미디어학회논문지, 27권 1호, pp. 80–90", doi=None, tag=None),
    dict(year=2022, title="Signal Preprocessing Technique With Noise-Tolerant for RF-Based UAV Signal Classification",
         authors="<b>Dae-Il Noh</b>, Seon-Geun Jeong, Huu-Trung Hoang, Quoc-Viet Pham, Thien Huynh-The, Mikio Hasegawa, Hiroo Sekiya, Sunyoung Kwon, Sang-Hwa Chung, Won-Joo Hwang",
         venue="IEEE Access", doi="10.1109/ACCESS.2022.3232036", tag="Wireless"),
]

STUDENTS = [  # 학생 연구원: 사진은 images/people/ 에 3:4 비율로 저장
    dict(ko="조희준", en="Hee-Jun Cho", role="학부연구생", dept="인공지능학과 4학년",
         email="jhg811515@gmail.com", photo="images/people/hee-jun-cho.jpg"),
    dict(ko="류의상", en="Ui-Sang Ryu", role="학부연구생", dept="인공지능학과 4학년",
         email="20182366@g.deu.ac.kr", photo="images/people/ui-sang-ryu.jpg"),
    dict(ko="박세준", en="Se-Jun Park", role="학부연구생", dept="인공지능학과 3학년",
         email="20221948@g.deu.ac.kr", photo="images/people/se-jun-park.jpg"),
    dict(ko="정재원", en="Jaewon Chung", role="학부연구생", dept="인공지능학과 3학년",
         email="20243242@office.deu.ac.kr", photo=None),  # 사진 받으면 images/people/jaewon-chung.jpg
]

# 학회 발표 논문: PUBS와 같은 형식 (venue에 학회명, 필요하면 location 추가, doi는 없으면 None)
CONFS = [
    dict(year=2025, title="Robust Machine Learning-Based Chirp Signal Detection for Asynchronous Pulse Code Multiple Access in Low-SNR Massive IoT Environments",
         authors="Mayu Horiuchi, Ferdinand Peper, Kenji Leibnitz, Naoki Wakamiya, Jin Nakazato, Maki Arai, <b>Dae-Il Noh</b>, Won-Joo Hwang, Mikio Hasegawa",
         venue="IEICE Technical Report, vol. 125, no. 190, pp. 24–29", doi=None, tag="Wireless"),
    dict(year=2024, title="Quantum-based UWB signal classification",
         authors="<b>Dae-Il Noh</b>, Seon-Geun Jeong, Mikio Hasegawa, Hiroo Sekiya, Won-Joo Hwang",
         venue="10th Anniversary Korea-Japan Joint Workshop on Complex Communication Sciences (KJCCS 2024)",
         location="Beppu, Japan", note="Oral", doi=None, tag="Quantum ML"),
    dict(year=2023, title="UWB LoS, NLoS 신호 탐지",
         authors="<b>노대일</b>, 정선근, 황원주",
         venue="2023 한국소프트웨어종합학술대회 (KSC 2023)", location="부산", note="Poster", doi=None, tag="Wireless"),
    dict(year=2022, title="Noise-Tolerant Signal Preprocessing Technique for Unmanned Aerial Vehicle Classification",
         authors="<b>Dae-Il Noh</b>, Won-Joo Hwang",
         venue="The 18th International Conference on Multimedia Information Technology and Applications (MITA 2022)",
         location="Jeju, Korea", doi=None, tag="Wireless"),
    dict(year=2021, title="주파수 기반 블루투스 신호 분류 CNN 모델",
         authors="<b>노대일</b>, Huu-Trung Hoang, 안수범, 황원주",
         venue="2021년도 한국멀티미디어학회 춘계학술발표대회", location="대구", note="Oral",
         award="우수논문상 (한국지능정보사회진흥원장상)",
         news="https://www.pusan.ac.kr/kor/CMS/Board/Board.do?mCode=MN109&mode=view&mgr_seq=12&board_seq=1464034",
         doi=None, tag="Wireless"),
    dict(year=2021, title="Radio Frequency-Based Classification of Unmanned Aerial Vehicle Using Convolution Neural Network",
         authors="<b>Dae-Il Noh</b>, Huu-Trung Hoang, Won-Joo Hwang",
         venue="The 17th International Conference on Multimedia Information Technology and Applications (MITA 2021)",
         location="Seogwipo, Korea", note="Oral", doi=None, tag="Wireless"),
]

# 특허 (대한민국 등록특허). 주민번호·주소 등 개인정보는 넣지 않는다.
PATENTS = [
    dict(title="시각 이상 여부 진단을 위해 시신경 구조를 세그멘팅하는 AI 기반 영상처리 장치",
         inventors="박경민, <b>노대일</b>, 김동현", reg_no="10-2789575", reg_date="2025.03.27",
         app_no="10-2024-0201821", app_date="2024.12.31", patentee="(주)씨앤피", tag="Computer Vision"),
    dict(title="노이즈 내성을 갖는 신호 분류 방법 및 장치, 이를 이용한 무인항공기 신호 분류 시스템",
         inventors="황원주, <b>노대일</b>", reg_no="10-2591634", reg_date="2023.10.16",
         app_no="10-2021-0175065", app_date="2021.12.08", patentee="부산대학교 산학협력단", tag="Wireless"),
    dict(title="스마트 맥주 디스펜서",
         inventors="<b>노대일</b>, 조성호, 주환이", reg_no="10-2381940", reg_date="2022.03.29",
         app_no="10-2020-0023987", app_date="2020.02.27", patentee="노대일", tag=None),
]

LOGO = ('<svg width="34" height="34" viewBox="0 0 100 100" aria-hidden="true">'
        '<ellipse cx="50" cy="50" rx="40" ry="14" fill="none" stroke="#3a4fd8" stroke-width="5" opacity=".4"/>'
        '<circle cx="50" cy="50" r="40" fill="none" stroke="#3a4fd8" stroke-width="8"/>'
        '<line x1="50" y1="50" x2="74" y2="26" stroke="#3a4fd8" stroke-width="8" stroke-linecap="round"/>'
        '<circle cx="78" cy="22" r="11" fill="#7b5cf0"/></svg>')


def pub_item(p, compact=False):
    tag = f'<span class="badge">{p["tag"]}</span>' if p.get("tag") else ""
    award = f'<span class="badge award">{p["award"]}</span>' if p.get("award") else ""
    body = (f'<div class="pt">{p["title"]}{award}</div><div class="pa">{p["authors"]}</div>'
            f'<div class="pv"><i>{p["venue"]}</i>{", " + p["location"] if p.get("location") else ""}, {p["year"]}'
            + (f' · <a href="https://doi.org/{p["doi"]}" target="_blank" rel="noopener">DOI</a>' if p.get("doi") else "")
            + (f' · {p["note"]}' if p.get("note") else "")
            + (f' · <a href="{p["news"]}" target="_blank" rel="noopener">관련 기사</a>' if p.get("news") else "")
            + f'{tag}</div>')
    if compact:
        return f'<li><div class="yr">{p["year"]}</div><div>{body}</div></li>'
    return f'<li>{body}</li>'


CSS_VER = int((ROOT / "assets/style.css").stat().st_mtime)


def layout(fname, title, desc, content, scripts=""):
    full = LAB_KO if fname == "index.html" else f"{title} | {LAB_KO}"
    menu = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{n}</a>' for f, n in PAGES)
    url = SITE + "/" + ("" if fname == "index.html" else fname)
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/images/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="assets/style.css?v={CSS_VER}">
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="index.html">{LOGO}<span>QC·AI Lab<small>{LAB_KO}</small></span></a>
    <nav class="menu" aria-label="주요 메뉴">{menu}</nav>
  </div>
</header>
<main>
{content}
</main>
<footer>
  <div class="wrap">
    <span>© 2026 {LAB_EN}, Dong-eui University</span>
    <span>산학협력관 804호 · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</footer>
{scripts}</body>
</html>
"""


def page_head(sub, h1, p=""):
    para = f"<p>{p}</p>" if p else ""
    return f'<div class="page-head"><div class="wrap"><div class="sub">{sub}</div><h1>{h1}</h1>{para}</div></div>'


# ---------- Home ----------
def home():
    tags = "".join(f'<a href="research.html#{a["id"]}">{a["en"]}</a>' for a in AREAS)
    cards = "".join(
        f'<a class="card" href="research.html#{a["id"]}"><div class="ic">{icon(a["icon"])}</div>'
        f'<h3>{a["ko"]}<small>{a["en"]}</small></h3><p>{a["short"]}</p></a>' for a in AREAS)
    recent = "".join(pub_item(p, compact=True) for p in PUBS[:3])
    content = f"""<div class="hero">
  <canvas id="qbits" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="eyebrow">Dong-eui University · Dept. of Artificial Intelligence</div>
    <h1>{LAB_KO}</h1>
    <div class="en">{LAB_EN}</div>
    <p class="lead">양자 컴퓨팅과 인공지능의 접점에서 새로운 학습 모델을 연구하고, 이를 무선 통신과 제조 현장의 실제 문제에 적용합니다.</p>
    <div class="tags">{tags}</div>
  </div>
</div>
<section>
  <div class="wrap">
    <div class="head"><div><div class="sub">Research</div><h2>연구 분야</h2></div><a class="more-link" href="research.html">자세히 보기 →</a></div>
    <div class="grid">{cards}</div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head"><div><div class="sub">Publications</div><h2>최근 논문</h2></div><a class="more-link" href="publications.html">전체 논문 →</a></div>
    <ul class="pubs compact">{recent}</ul>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="cta">
      <div><h2>학부연구생 모집 중</h2><p>양자 컴퓨팅과 AI 연구에 관심 있는 학생을 기다립니다.</p></div>
      <a class="btn" href="people.html#join">지원 안내 보기</a>
    </div>
  </div>
</section>"""
    return layout("index.html", "Home",
                  "동의대학교 인공지능학과 양자컴퓨팅·AI 융합연구실 — 양자 컴퓨팅, 양자 머신러닝, 컴퓨터 비전, 무선 통신, 스마트 팩토리",
                  content, '<script src="assets/hero.js"></script>\n')


# ---------- Research ----------
def research():
    items = []
    for a in AREAS:
        lis = "".join(f"<li>{t}</li>" for t in a["topics"])
        rel = [p for p in PUBS if a["tag"] and p["tag"] == a["tag"]]
        rel_html = ""
        if rel:
            links = " · ".join(f'<a href="https://doi.org/{p["doi"]}" target="_blank" rel="noopener">{p["title"].split(":")[0]}</a>' for p in rel)
            rel_html = f'<div class="rel">관련 논문: {links}</div>'
        items.append(f'<div class="area" id="{a["id"]}"><div class="ic">{icon(a["icon"], 28)}</div><div>'
                     f'<h2>{a["ko"]}<small>{a["en"]}</small></h2><p>{a["body"]}</p><ul>{lis}</ul>{rel_html}</div></div>')
    content = page_head("Research", "연구 분야",
                        "양자 알고리즘과 딥러닝을 결합한 하이브리드 모델을 핵심으로, 통신·비전·제조 분야의 응용 연구를 함께 수행합니다.") + \
        f'<section><div class="wrap">{"".join(items)}</div></section>'
    return layout("research.html", "연구 분야", "양자컴퓨팅·AI 융합연구실의 연구 분야 — 양자 컴퓨팅, 양자 머신러닝, 컴퓨터 비전, 무선 통신, 스마트 팩토리", content)


# ---------- People ----------
def member_card(m):
    photo = (f'<img src="{m["photo"]}" alt="{m["ko"]}" loading="lazy">' if m["photo"]
             else f'<div class="photo-ph" aria-hidden="true">{m["ko"][0]}</div>')
    return (f'<div class="member">{photo}'
            f'<div class="info"><h3>{m["ko"]}<small>{m["en"]}</small></h3>'
            f'<div class="role">{m["role"]}</div><div class="dept">{m["dept"]}</div>'
            f'<a href="mailto:{m["email"]}">{m["email"]}</a></div></div>')


def people():
    members = "".join(member_card(m) for m in STUDENTS)
    content = page_head("People", "구성원") + f"""<section>
  <div class="wrap">
    <div class="head"><div><div class="sub">Principal Investigator</div><h2>지도교수</h2></div></div>
    <div class="pi">
      <img class="avatar" src="images/profile.jpg" alt="노대일 교수">
      <div>
        <h3>노대일<small>Dae-Il Noh</small></h3>
        <div class="role">조교수 · Assistant Professor</div>
        <ul>
          <li>동의대학교 인공지능학과</li>
          <li>산학협력관 804호</li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <div class="links">
          <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a>
          <a href="{ORCID}" target="_blank" rel="noopener">ORCID</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="alt" id="join">
  <div class="wrap">
    <div class="head"><div><div class="sub">Students</div><h2>학생 연구원</h2></div></div>
    <div class="members">{members}</div>
    <div class="recruit">
      <b>학부연구생 모집 중</b> — 양자 컴퓨팅, 양자 머신러닝, 컴퓨터 비전, 무선 통신, 스마트 팩토리 분야에 관심 있는 학생은
      <a href="mailto:{EMAIL}">이메일</a>로 연락 주세요.
    </div>
  </div>
</section>"""
    return layout("people.html", "구성원", "양자컴퓨팅·AI 융합연구실 구성원 — 지도교수 노대일, 학부연구생 모집", content)


# ---------- Publications ----------
def by_year(items, render):
    years = sorted({p["year"] for p in items}, reverse=True)
    return "".join(f'<div class="year">{y}</div><ul class="pubs">{"".join(render(p) for p in items if p["year"] == y)}</ul>'
                   for y in years)


def patent_item(p):
    tag = f'<span class="badge">{p["tag"]}</span>' if p.get("tag") else ""
    return (f'<li><div class="pt">{p["title"]}<span class="badge ok">등록</span>{tag}</div>'
            f'<div class="pa">발명자: {p["inventors"]}</div>'
            f'<div class="pv">대한민국 특허 제{p["reg_no"]}호 · 등록일 {p["reg_date"]} · '
            f'출원번호 {p["app_no"]} ({p["app_date"]}) · 특허권자 {p["patentee"]}</div></li>')


def pub_section(sid, sub, h2, count, body, empty):
    inner = body if count else f'<div class="empty">{empty}</div>'
    return (f'<section id="{sid}"><div class="wrap"><div class="head"><div><div class="sub">{sub}</div>'
            f'<h2>{h2}</h2></div></div>{inner}</div></section>')


def publications():
    journal = pub_section("journal", "Journal", "저널 논문", len(PUBS), by_year(PUBS, pub_item),
                          "등록된 저널 논문이 없습니다.")
    conf = pub_section("conference", "Conference", "학술대회 논문", len(CONFS), by_year(CONFS, pub_item),
                       "학술대회 발표 논문 목록을 준비 중입니다.")
    pats = sorted(PATENTS, key=lambda p: p["reg_date"], reverse=True)
    patent = pub_section("patent", "Patent", "특허", len(PATENTS),
                         f'<ul class="pubs">{"".join(patent_item(p) for p in pats)}</ul>', "특허 목록을 준비 중입니다.")
    content = page_head("Publications", "연구 성과",
                        f'전체 논문 목록은 <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a>에서도 확인할 수 있습니다.') + journal + conf + patent
    return layout("publications.html", "연구 성과", "양자컴퓨팅·AI 융합연구실 연구 성과 — 저널 논문, 학술대회 논문, 특허", content)


# ---------- Contact ----------
def contact():
    content = page_head("Contact", "연락처") + f"""<section>
  <div class="wrap">
    <div class="contact">
      <div class="card">
        <div class="k">Location</div>
        <p>부산광역시 부산진구 엄광로 176<br>동의대학교 산학협력관 804호</p>
        <div class="links"><a href="https://map.naver.com/p/search/%EB%8F%99%EC%9D%98%EB%8C%80%ED%95%99%EA%B5%90%20%EC%82%B0%ED%95%99%ED%98%91%EB%A0%A5%EA%B4%80" target="_blank" rel="noopener">네이버 지도에서 보기</a></div>
      </div>
      <div class="card">
        <div class="k">Email</div>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <div class="links"><a href="people.html#join">학부연구생 지원 안내</a></div>
      </div>
    </div>
  </div>
</section>"""
    return layout("contact.html", "연락처", "양자컴퓨팅·AI 융합연구실 연락처 — 동의대학교 산학협력관 804호", content)


if __name__ == "__main__":
    for fname, fn in [("index.html", home), ("research.html", research), ("people.html", people),
                      ("publications.html", publications), ("contact.html", contact)]:
        (ROOT / fname).write_text(fn(), encoding="utf-8")
        print("wrote", fname)
