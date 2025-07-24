import streamlit as st
from datetime import datetime
import random
import hashlib

st.set_page_config(page_title="오늘의 운세 게임", page_icon="🔮", layout="centered")

st.title("🔮 오늘의 운세를 알아보자!")
st.write("당신의 생일로 오늘의 운세를 점쳐드립니다.")

# 생일 입력
birth_date = st.date_input("🎂 생년월일을 입력하세요", min_value=datetime(1900, 1, 1), max_value=datetime.today())

if st.button("운세 보기"):
    # 오늘 날짜
    today = datetime.today().strftime("%Y-%m-%d")

    # 생일 + 오늘 날짜로 고정된 시드 생성
    combined = str(birth_date) + today
    seed = int(hashlib.sha256(combined.encode()).hexdigest(), 16) % (10 ** 8)
    random.seed(seed)

    # 운세 항목
    fortunes = {
        "💰 금전운": [
            "뜻하지 않은 행운이 생길 수 있어요!",
            "오늘은 지출을 조심하세요.",
            "작은 투자에 행운이 따릅니다.",
            "금전적으로 평온한 하루입니다.",
            "복권을 사면 좋은 결과가 있을지도?"
        ],
        "❤️ 애정운": [
            "사랑이 피어나는 하루가 될 거예요!",
            "썸이 있다면 진전이 있을지도 몰라요.",
            "연인과 다툼에 주의하세요.",
            "솔로에게 좋은 기회가 찾아옵니다.",
            "감정 표현에 솔직해지면 좋아요."
        ],
        "💪 건강운": [
            "건강한 하루! 컨디션 최고!",
            "과로를 조심하세요.",
            "스트레칭을 자주 해주세요.",
            "마음 건강에 집중해보세요.",
            "오늘은 휴식이 필요한 날이에요."
        ],
        "📚 조언": [
            "가까운 사람의 조언에 귀를 기울이세요.",
            "새로운 시도를 두려워하지 마세요.",
            "오늘은 천천히, 여유를 가지세요.",
            "작은 친절이 큰 기쁨이 될 거예요.",
            "웃는 얼굴이 복을 부른답니다 :)"
        ]
    }

    st.subheader("✨ 오늘의 운세 ✨")
    for category, messages in fortunes.items():
        message = random.choice(messages)
        st.markdown(f"**{category}**: {message}")

    st.success("좋은 하루 보내세요! 🌈")
