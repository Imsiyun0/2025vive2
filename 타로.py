import streamlit as st
import random

# 운세 종류
fortune_types = ["연애운", "금전운", "직업운"]

# 타로 카드 데이터
tarot_cards = [
    {
        "name": "The Fool",
        "image": "https://upload.wikimedia.org/wikipedia/en/9/90/RWS_Tarot_00_Fool.jpg",
        "meanings": {
            "연애운": "새로운 인연이 다가오거나, 지금 관계에서 자유로움이 필요할 수 있어요.",
            "금전운": "충동적인 소비에 주의가 필요합니다. 무계획한 투자는 피하세요.",
            "직업운": "새로운 기회가 올 수 있지만, 준비가 안 되면 도전이 위험할 수 있어요."
        }
    },
    {
        "name": "The Magician",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg",
        "meanings": {
            "연애운": "당신의 매력이 빛나는 시기입니다. 표현하면 좋은 결과가 있을 거예요.",
            "금전운": "능력을 잘 활용하면 좋은 수익 기회가 있어요.",
            "직업운": "능력을 인정받고 성과를 낼 수 있는 시기입니다."
        }
    },
    {
        "name": "The Lovers",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/db/RWS_Tarot_06_Lovers.jpg",
        "meanings": {
            "연애운": "중요한 선택의 기로에 서 있습니다. 마음의 소리에 귀 기울이세요.",
            "금전운": "지출에 있어 가족이나 연인과의 조율이 필요할 수 있어요.",
            "직업운": "동료 또는 파트너와의 협력이 중요합니다."
        }
    },
    {
        "name": "The Tower",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/53/RWS_Tarot_16_Tower.jpg",
        "meanings": {
            "연애운": "예상치 못한 갈등이나 이별의 가능성이 있습니다. 신중하게 대처하세요.",
            "금전운": "예기치 못한 지출에 대비하세요. 큰 투자에는 위험이 따릅니다.",
            "직업운": "변화가 강제될 수 있는 시기입니다. 마음의 준비를 하세요."
        }
    },
    {
        "name": "The Star",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/db/RWS_Tarot_17_Star.jpg",
        "meanings": {
            "연애운": "희망적인 변화가 기대됩니다. 긍정적인 자세를 유지하세요.",
            "금전운": "서서히 재정이 회복되며 빛을 보기 시작할 수 있어요.",
            "직업운": "긴 시간 노력해온 결과가 곧 보일 수 있어요."
        }
    },
]

# 종합 해석 템플릿
def generate_summary(fortune_type, selected_cards):
    keywords = [card["name"] for card in selected_cards]
    meanings = [card["meanings"][fortune_type] for card in selected_cards]

    summary = ""

    if fortune_type == "연애운":
        summary += "💖 **연애운 종합 해석**\n\n"
        summary += "이번 리딩은 다음과 같은 흐름을 보여줍니다:\n\n"
        summary += f"- 감정의 흐름: {meanings[0]}\n"
        summary += f"- 관계의 전환점: {meanings[1]}\n"
        summary += f"- 조언 또는 결과: {meanings[2]}\n\n"
        summary += "총평: 감정에 솔직하되 섣부른 판단은 피하세요. 마음을 천천히 표현하면 좋은 흐름으로 이어질 수 있습니다."

    elif fortune_type == "금전운":
        summary += "💰 **금전운 종합 해석**\n\n"
        summary += "당신의 금전 흐름은 다음과 같은 방향을 보여줍니다:\n\n"
        summary += f"- 현재 재정 상태: {meanings[0]}\n"
        summary += f"- 위험 요소 또는 기회: {meanings[1]}\n"
        summary += f"- 향후 조언: {meanings[2]}\n\n"
        summary += "총평: 감에 의존하기보단 구체적인 계획과 현실적인 판단이 필요한 시기입니다."

    elif fortune_type == "직업운":
        summary += "💼 **직업운 종합 해석**\n\n"
        summary += "직업과 관련된 흐름은 다음과 같습니다:\n\n"
        summary += f"- 현재 직장 상황 또는 태도: {meanings[0]}\n"
        summary += f"- 도전 혹은 변화 요인: {meanings[1]}\n"
        summary += f"- 결과 또는 조언: {meanings[2]}\n\n"
        summary += "총평: 변화의 흐름 속에서도 중심을 잡는 것이 중요합니다. 내면의 직감을 믿으세요."

    return summary

# UI 시작
st.title("🔮 타로 카드 운세 리딩")
st.write("운세 종류를 선택하고 타로 카드 3장을 뽑아보세요!")

# 운세 선택
selected_fortune = st.selectbox("📌 운세 종류를 선택하세요", fortune_types)

if st.button("🃏 타로 카드 뽑기"):
    selected_cards = random.sample(tarot_cards, 3)

    st.subheader(f"✨ {selected_fortune} 리딩 결과")

    for i, card in enumerate(selected_cards, 1):
        st.markdown(f"### {i}. {card['name']}")
        st.image(card["image"], width=200)
        st.markdown(f"**의미:** *{card['meanings'][selected_fortune]}*")
        st.markdown("---")

    # 종합 해석 출력
    st.subheader("🔎 종합 해석")
    st.markdown(generate_summary(selected_fortune, selected_cards))

# 설명
with st.expander("📘 타로 리딩이란?"):
    st.markdown("""
    타로 카드는 당신의 무의식과 흐름을 반영하는 도구입니다.  
    선택한 주제(운세)에 따라 카드의 해석은 달라질 수 있어요.  
    종합 해석은 세 장의 의미를 하나로 엮어 조언의 흐름을 제시합니다.  
    재미와 참고용으로 활용해보세요 🙏
    """)
