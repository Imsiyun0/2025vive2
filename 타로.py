import streamlit as st

# 카드 정보 (이름, 이미지, 해석)
tarot_cards = [
    {
        "name": "The Fool",
        "image": "https://upload.wikimedia.org/wikipedia/en/9/90/RWS_Tarot_00_Fool.jpg",
        "meanings": {
            "연애운": "새로운 인연의 시작 또는 자유로움이 필요합니다.",
            "금전운": "충동적 지출에 주의하세요.",
            "직업운": "새로운 일에 대한 도전이 유리할 수 있어요."
        }
    },
    {
        "name": "The Magician",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg",
        "meanings": {
            "연애운": "자신 있게 다가가면 좋은 기회가 생깁니다.",
            "금전운": "능동적으로 움직이면 수익을 낼 수 있어요.",
            "직업운": "스스로 기회를 만들어낼 수 있는 시기입니다."
        }
    },
    {
        "name": "The Lovers",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/db/RWS_Tarot_06_Lovers.jpg",
        "meanings": {
            "연애운": "중요한 선택의 시기입니다. 진심을 따르세요.",
            "금전운": "파트너와의 재정 조율이 필요해요.",
            "직업운": "협력과 파트너십이 중요해지는 시기입니다."
        }
    },
    {
        "name": "The Star",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/db/RWS_Tarot_17_Star.jpg",
        "meanings": {
            "연애운": "희망적인 전개가 예상됩니다.",
            "금전운": "천천히 회복되는 운입니다.",
            "직업운": "지금까지의 노력이 빛을 보게 됩니다."
        }
    },
    {
        "name": "The Tower",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/53/RWS_Tarot_16_Tower.jpg",
        "meanings": {
            "연애운": "예기치 못한 변화가 있을 수 있어요.",
            "금전운": "큰 지출 또는 손실을 조심하세요.",
            "직업운": "예상 밖의 변화에 대비해야 합니다."
        }
    },
    {
        "name": "The World",
        "image": "https://upload.wikimedia.org/wikipedia/en/f/ff/RWS_Tarot_21_World.jpg",
        "meanings": {
            "연애운": "관계가 안정적으로 마무리되거나 완성됩니다.",
            "금전운": "목표한 재정적 성공에 도달할 수 있어요.",
            "직업운": "긴 여정의 마무리, 프로젝트 완수의 시기입니다."
        }
    }
]

back_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Rider-Back.jpg/440px-Rider-Back.jpg"

# 상태 초기화
if "selected_indices" not in st.session_state:
    st.session_state.selected_indices = []
if "flipped" not in st.session_state:
    st.session_state.flipped = [False] * len(tarot_cards)
if "fortune_type" not in st.session_state:
    st.session_state.fortune_type = "연애운"

# 제목
st.title("🔮 타로 카드 직접 뽑기")
st.markdown("카드를 3장 선택해보세요. 클릭하면 카드가 열립니다!")

# 운세 선택
st.session_state.fortune_type = st.selectbox("운세를 선택하세요", ["연애운", "금전운", "직업운"])

# 카드 UI (뒷면 → 클릭하면 앞면)
cols = st.columns(3)

for i in range(len(tarot_cards)):
    col = cols[i % 3]

    with col:
        if st.session_state.flipped[i]:
            st.image(tarot_cards[i]["image"], width=180)
            st.caption(tarot_cards[i]["name"])
        else:
            if len(st.session_state.selected_indices) < 3:
                if st.button(f"카드 {i+1}", key=f"card_btn_{i}"):
                    st.session_state.flipped[i] = True
                    st.session_state.selected_indices.append(i)
            st.image(back_image, width=180)

# 결과 출력
if len(st.session_state.selected_indices) == 3:
    st.subheader("🃏 타로 리딩 결과")
    for idx in st.session_state.selected_indices:
        card = tarot_cards[idx]
        st.markdown(f"### {card['name']}")
        st.image(card["image"], width=200)
        st.markdown(f"**해석:** *{card['meanings'][st.session_state.fortune_type]}*")
        st.markdown("---")

    # 종합 해석
    st.subheader("🔎 종합 해석")
    meanings = [tarot_cards[i]["meanings"][st.session_state.fortune_type] for i in st.session_state.selected_indices]
    summary = f"🧿 **{st.session_state.fortune_type} 총평**\n\n"
    for i, meaning in enumerate(meanings, 1):
        summary += f"- 카드 {i}: {meaning}\n"
    summary += "\n💡 전체적으로, 변화와 기회가 혼재된 흐름입니다. 스스로를 믿고 움직인다면 좋은 방향으로 나아갈 수 있습니다."
    st.markdown(summary)

# 초기화 버튼
if st.button("🔄 다시 뽑기"):
    st.session_state.selected_indices = []
    st.session_state.flipped = [False] * len(tarot_cards)
