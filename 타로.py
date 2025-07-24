import streamlit as st

# -----------------------------
# 카드 데이터 (10장)
# -----------------------------
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
        "name": "The High Priestess",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/88/RWS_Tarot_02_High_Priestess.jpg",
        "meanings": {
            "연애운": "당장의 말보다는 직관을 믿으세요.",
            "금전운": "겉으로 드러나지 않은 정보가 중요합니다.",
            "직업운": "지금은 조용히 준비하고 기다리는 시기입니다."
        }
    },
    {
        "name": "The Empress",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/d2/RWS_Tarot_03_Empress.jpg",
        "meanings": {
            "연애운": "풍요롭고 따뜻한 관계가 이어집니다.",
            "금전운": "수확의 시기입니다. 풍요가 따릅니다.",
            "직업운": "창조적 에너지가 충만한 시기입니다."
        }
    },
    {
        "name": "The Emperor",
        "image": "https://upload.wikimedia.org/wikipedia/en/c/c3/RWS_Tarot_04_Emperor.jpg",
        "meanings": {
            "연애운": "책임감 있는 태도가 관계를 이끌 수 있어요.",
            "금전운": "안정적인 수입과 체계적 계획이 중요합니다.",
            "직업운": "지금은 리더십과 권위를 발휘해야 할 시기입니다."
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
        "name": "The Chariot",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/3a/The_Chariot.jpg",
        "meanings": {
            "연애운": "관계를 주도해 나가면 좋은 결과가 있을 수 있어요.",
            "금전운": "목표를 향해 집중하면 성과가 따릅니다.",
            "직업운": "전진하는 힘이 강합니다. 추진력을 믿으세요."
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
            "연애운": "관계가 완성되거나 큰 성장을 이룹니다.",
            "금전운": "목표한 재정적 성공에 도달할 수 있어요.",
            "직업운": "프로젝트가 성공적으로 마무리됩니다."
        }
    },
]

# 카드 뒷면 이미지
back_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Rider-Back.jpg/440px-Rider-Back.jpg"

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "selected_indices" not in st.session_state:
    st.session_state.selected_indices = []
if "flipped" not in st.session_state:
    st.session_state.flipped = [False] * len(tarot_cards)
if "fortune_type" not in st.session_state:
    st.session_state.fortune_type = "연애운"

# -----------------------------
# UI 시작
# -----------------------------
st.title("🔮 직접 뽑는 3장 타로 리딩")
st.markdown("아래에서 카드를 클릭해 3장을 선택하세요. 클릭하면 앞면이 드러납니다.")

# 운세 종류 선택
st.session_state.fortune_type = st.selectbox("🔍 궁금한 운세를 선택하세요", ["연애운", "금전운", "직업운"])

# 카드 뽑기 UI
cols = st.columns(5)
for i in range(len(tarot_cards)):
    col = cols[i % 5]
    with col:
        if st.session_state.flipped[i]:
            st.image(tarot_cards[i]["image"], use_column_width=True)
            st.caption(tarot_cards[i]["name"])
        else:
            if len(st.session_state.selected_indices) < 3:
                if st.button(f"카드 {i+1}", key=f"card_{i}"):
                    st.session_state.flipped[i] = True
                    st.session_state.selected_indices.append(i)
            st.image(back_image, use_column_width=True)

# -----------------------------
# 리딩 결과 출력
# -----------------------------
if len(st.session_state.selected_indices) == 3:
    st.subheader("🃏 선택한 카드 해석")
    selected = st.session_state.selected_indices
    for idx in selected:
        card = tarot_cards[idx]
        st.markdown(f"### {card['name']}")
        st.image(card["image"], width=200)
        st.markdown(f"**의미:** *{card['meanings'][st.session_state.fortune_type]}*")
        st.markdown("---")

    # 종합 해석
    st.subheader("🔎 종합 해석")
    all_meanings = [tarot_cards[i]["meanings"][st.session_state.fortune_type] for i in selected]
    st.markdown(f"""
    ### 🧿 {st.session_state.fortune_type} 요약
    - 카드 1: {all_meanings[0]}
    - 카드 2: {all_meanings[1]}
    - 카드 3: {all_meanings[2]}

    💡 전반적으로 이 흐름은 **긍정적인 변화와 조화**, 또는 **주의가 필요한 전환기**를 의미할 수 있습니다.  
    조언을 마음에 새기고 오늘 하루를 준비해보세요.
    """)

# -----------------------------
# 리셋 버튼
# -----------------------------
if st.button("🔄 다시 뽑기"):
    st.session_state.selected_indices = []
    st.session_state.flipped = [False] * len(tarot_cards)
