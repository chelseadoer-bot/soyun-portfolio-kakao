# 심소연 서비스 기획 포트폴리오 사이트

네이버웹툰 Disney 디지털 코믹스 서비스 기획자(PM) 지원용 포트폴리오.
"하나의 웹사이트"처럼 허브(index.html)에서 카드를 클릭하면 각 상세 케이스로 이동하는 구조.

## 파일 구조

```
site/
├── index.html        ← 허브(갤러리). 여기가 첫 페이지. 6개 케이스 카드 → 상세로 링크
├── ai-agent.html     ← EP.01 AI 대화형 커머스 에이전트 (완성, 그린 다이어그램·대화 목업)
├── spao.html         ← EP.02 자사몰 UX 개편 (완성, 이미지 4)
├── pavilion.html     ← EP.03 브랜드 전용관 설계 (완성, 이미지 3)
├── fastar.html       ← EP.04 글로벌 런칭·현지화 (완성, 코럴~그린 다이어그램)
├── girog.html        ← EP.05 기로그 창업 (완성, 이미지 2)
├── scoring.html      ← EP.06 입점 판별 모델 (완성, 이미지 3)
├── coupon.html       ← (허브 미노출) 쿠폰 COI
└── taxonomy.html     ← (허브 미노출) 메타태그 택소노미
```

## 디자인 시스템 (Webtoon Green)

네이버웹툰 아이덴티티를 반영한 톤. 모든 페이지가 이 토큰을 공유함:

- **시그니처 컬러**: 웹툰 그린 `--accent: #00B551` / soft `--accent-soft: #E6FBF0`
- 밝은 그린(다크 배경용) `#5EE6A0`, 딥 그린(텍스트) `#00753A`
- 잉크 `#17161A`, 배경 크림 `#FCFBF9` / wash `#F4F1EC`
- 폰트: Pretendard (jsdelivr CDN), 헤드라인 900 / 본문 400·500
- 허브(index.html)는 순백 배경 + 큼직한 썸네일 카드 + EP.NN 뱃지 + 웹툰식 지표(별점·조회수 느낌)

## 각 상세 페이지 공통 요소

- 상단에 `.site-topbar` (검정 배경, "← 심소연 포트폴리오" 홈 링크 + "전체 케이스 보기")
- 본문 구조: `.mast`(제목·요약·메타) → Problem → Hypothesis → Solution → Results → Takeaway
- `<body>` 바로 다음에 site-topbar가 주입되어 있음

## ✅ 완료: ai-agent.html, fastar.html (2026-07-29)

두 페이지 모두 기존 상세 페이지(spao.html)와 **동일한 디자인 시스템**(Webtoon Green 토큰·Pretendard·site-topbar·Problem→Hypothesis→Solution→Results 구조)으로 완성.
이미지 없이 **CSS 다이어그램/도식**으로 대체(ai-agent=대화 목업·3단 파이프라인, fastar=고정축/현지화 코럴-그린 시각화·시장 매트릭스·런칭→운영→정책화 라이프사이클).
검증: 로컬 서버(python http.server)로 8개 HTML 200 확인, 카드 링크·홈 복귀 정상, 데스크톱/모바일 무(無) 가로스크롤, 폰트 로드 확인.

### ai-agent.html (EP.01 — AI 대화형 커머스 에이전트)
- 소속: 이랜드 그룹 온라인 · 키디키디 · 2025.08–현재 (진행 중)
- Problem: 검색 품질 저하 → 이탈 증가. 목표=전환율·객단가 동시 상승
- Hypothesis: ①엄마 고객은 상황(TPO)으로 질문 ②키디키디는 기획전 단위 운영 ③추천 정확도는 메타태그 품질이 결정
- Solution: 상황 해석 → 메타태그 매핑 → 기획전 큐레이션 (3단 파이프라인). 상위기획/상세기획(대화 플로우·추천 로직·화면)/협업 실행(외부 개발사·IT플랫폼팀·데이터팀 리딩)
- Results: 전환·객단가↑(예상), 이탈↓. ※진행 중이라 성과는 예상치로 표기
- 이미지 없음 → 그린 계열 다이어그램/도식으로 대체

### fastar.html (EP.04 — 글로벌 서비스 런칭·현지화)
- 소속: 쏘영(SSOYOUNG) · 팀 4인(개발·디자인·운영·기획/마케팅, 본인=기획+마케팅) · 2021–2022
- Problem: 같은 상품도 나라마다 다르게 팔아야 함 (대만·동남아·미국)
- Insight: 공통 축=K-pop 스타일링(고정), 변수=현지 채널·트렌드(현지화)
- Solution: ①스타일링 큐레이션 ②채널별 현지화 콘텐츠(틱톡 등) ③국내 유튜버 협업 룩북 ④채널별 타깃 광고
- Results: 3개국 런칭, 전환율 2%대(업계 평균 1%대 중반 상회)
- 이미지 없음 → 코럴~그린 다이어그램으로 대체
- ※우대사항(Global Service Launch) 직결 케이스라 중요

## 배포

- Vercel/Netlify에 site 폴더 통째로 드래그&드롭 → index.html이 자동 첫 페이지
- 또는 GitHub Pages (chelseadoer-bot.github.io)
- 모든 링크가 상대경로(예: href="spao.html")라 그대로 작동함
- ※주의: Claude 채팅 미리보기에서는 파일 간 이동이 안 됨(격리 때문). 실제 배포하면 정상 작동.
