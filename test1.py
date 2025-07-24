import streamlit as st

# MBTI별 진로 추천 사전
mbti_careers = {
    "ISTJ": ["회계사", "행정직 공무원", "데이터 분석가", "법률 관련 직업"],
    "ISFJ": ["간호사", "교사", "사회복지사", "도서관 사서"],
    "INFJ": ["심리상담사", "작가", "연구원", "기획자"],
    "INTJ": ["전략 컨설턴트", "연구개발 엔지니어", "정책 분석가"],
    "ISTP": ["엔지니어", "파일럿", "정비사", "경찰"],
    "ISFP": ["디자이너", "요리사", "예술가", "간호사"],
    "INFP": ["작가", "예술가", "상담사", "콘텐츠 기획자"],
    "INTP": ["개발자", "이론물리학자", "데이터 과학자", "교수"],
    "ESTP": ["영업 전문가", "기자", "응급 구조사", "파일럿"],
    "ESFP": ["배우", "이벤트 플래너", "MC/진행자", "간호사"],
    "ENFP": ["광고기획자", "강연자", "마케터", "작가"],
    "ENTP": ["스타트업 창업자", "변호사", "기획자", "프로듀서"],
    "ESTJ": ["관리직 공무원", "프로젝트 매니저", "경영 컨설턴트"],
    "ESFJ": ["교사", "간호사", "HR 전문가", "사회복지사"],
    "ENFJ": ["상담사", "교수", "강사", "HRD 전문가"],
    "ENTJ": ["CEO", "전략기획가", "투자 분석가", "컨설턴트"]
}

# 웹앱 제목
st.title("🔮 MBTI 기반 진로 추천기")
st.write("당신의 MBTI를 선택하면, 성격 유형에 맞는 진로를 추천해드려요!")

# 사용자 입력: MBTI 선택
mbti_types = list(mbti_careers.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 추천 진로 보여주기
if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 유형에게 어울리는 진로:")
    for job in mbti_careers[selected_mbti]:
        st.markdown(f"- {job}")

# 하단 설명
st.markdown("---")
st.markdown("💡 *이 추천은 일반적인 MBTI 성격 특성을 바탕으로 제공됩니다. 본인의 흥미와 적성을 함께 고려해보세요!*")
