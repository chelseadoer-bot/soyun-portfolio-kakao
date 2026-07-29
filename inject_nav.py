import re, os

# 공통 상단 네비게이션 바 (사이트 통일감)
NAV = '''<body>
<div class="site-topbar">
  <a href="index.html" class="stb-home">← 심소연 포트폴리오</a>
  <span class="stb-title">Service Planning · Case Study</span>
  <a href="index.html" class="stb-all">전체 케이스 보기</a>
</div>
<style>
  .site-topbar{position:sticky;top:0;z-index:999;display:flex;align-items:center;gap:16px;
    background:#141419;color:#fff;padding:12px 26px;font-family:'Pretendard','Apple SD Gothic Neo',sans-serif;
    border-bottom:1px solid rgba(255,255,255,.12)}
  .site-topbar .stb-home{color:#fff;text-decoration:none;font-size:14px;font-weight:700;letter-spacing:-.01em}
  .site-topbar .stb-home:hover{color:#F5A623}
  .site-topbar .stb-title{font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#8A8792}
  .site-topbar .stb-all{margin-left:auto;font-size:12.5px;font-weight:700;color:#141419;background:#fff;
    text-decoration:none;padding:7px 15px;border-radius:7px;transition:opacity .15s}
  .site-topbar .stb-all:hover{opacity:.85}
  @media (max-width:600px){.site-topbar .stb-title{display:none}}
</style>'''

files = ["spao.html","pavilion.html","scoring.html","fastar_girog.html","coupon.html","taxonomy.html"]
for f in files:
    html = open(f, encoding="utf-8").read()
    if "site-topbar" in html:
        print(f"{f}: 이미 네비 있음, 스킵")
        continue
    # 첫 <body> 를 NAV로 교체 (한 번만)
    html = html.replace("<body>", NAV, 1)
    open(f,"w",encoding="utf-8").write(html)
    print(f"{f}: 네비 주입 완료")
