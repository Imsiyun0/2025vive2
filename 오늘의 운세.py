import streamlit as st
from datetime import datetime
import random
import hashlib

st.set_page_config(page_title="오늘의 운세", page_icon="🔮", layout="centered")

st.title("🔮 오늘의 운세")
st.write("당신의 생일과 오늘의 기운을 조합해 정밀한 운세를 알려드릴게요!")

# 🎂 생일 입력
birth_date = st.date_input("생년월일을 입력하세요", min_value=datetime(1900, 1, 1), max_value=datetime.today())

# 🔍 운세 종류 선택
selected_types = st.multiselect(
    "보고 싶은 운세 종류를 선택하세요:",
    ["💰 금전운", "❤️ 애정운", "💪 건강운", "📚 오늘의 조언"],
    default=["💰 금전운", "❤️ 애정운", "💪 건강운", "📚 오늘의 조언"]
)

# 운세 메시지
fortune_messages = {
    "💰 금전운": [
        "오늘은 재정적인 면에서 안정적인 흐름을 기대해볼 수 있는 날입니다. 특히 오후 시간대에 재정적으로 유리한 기운이 들어오며, 예상치 못한 수입이나 혜택이 생길 가능성도 있습니다. 단, 충동구매에는 주의하세요.",
        "갑작스러운 지출이 생길 수 있으니 여유 자금을 준비해두는 것이 좋습니다. 친구나 가족과의 약속에서 예산을 초과하지 않도록 주의하세요. 소비 습관을 되돌아보는 기회가 될 수 있습니다.",
        "작은 투자나 저축을 시작하기에 좋은 날입니다. 무리한 투자는 피하되, 장기적인 재정 계획을 세우기 시작한다면 매우 유리한 흐름이 따를 것입니다."
    ],
    "❤️ 애정운": [
        "연인과의 관계에서 깊은 대화가 필요한 날입니다. 마음을 솔직하게 나누면 서로에 대한 이해가 깊어질 것입니다. 솔로라면 새로운 만남에 마음을 열어보세요.",
        "감정이 예민해질 수 있으니 말 한마디에 주의가 필요합니다. 다툼보다는 배려와 경청이 중요합니다. 오늘 하루는 관계를 점검하는 데 집중해보세요.",
        "당신의 매력이 빛나는 하루입니다. 자신감을 가지고 행동해보세요. 썸이나 연애 중인 경우, 진전의 기회가 생깁니다."
    ],
    "💪 건강운": [
        "에너지 넘치는 하루입니다! 가벼운 운동이나 산책으로 좋은 기운을 유지할 수 있어요. 평소보다 컨디션이 좋아 새로운 루틴을 시작하기에도 좋습니다.",
        "스트레스가 누적될 수 있는 날입니다. 너무 무리하지 말고 휴식 시간을 충분히 가져야 합니다. 특히 수면과 식사를 규칙적으로 유지하세요.",
        "몸이 보내는 신호에 집중하세요. 피로감을 무시하지 말고 가벼운 스트레칭이나 명상을 통해 컨디션을 회복해보세요."
    ],
    "📚 오늘의 조언": [
        "오늘은 주변 사람들과의 관계에서 좋은 기운이 흐릅니다. 작은 친절이 큰 행운으로 이어질 수 있습니다. 긍정적인 에너지를 나누세요.",
        "혼자 있는 시간을 통해 많은 것을 정리할 수 있는 날입니다. 머릿속 생각들을 정리하고, 새로운 계획을 세우기에 적절한 시간입니다.",
        "정리정돈과 마음의 여유가 중요한 하루입니다. 주변 환경을 정돈하며 마음도 정리해보세요. 오늘의 정리가 내일의 성장을 만듭니다."
    ]
}

# 행운 요소들 (무작위 조합)
colors = ['빨강', '노랑', '파랑', '초록', '보라', '분홍', '주황', '검정', '하늘색']
items = ['책', '커피', '노트', '열쇠고리', '우산', '손목시계', '화장품', '이어폰', '텀블러']
numbers = list(range(1, 100))

# 운세 보기 버튼
if st.button("🔮 운세 보기"):
    if not selected_types:
        st.warning("운세 종류를 하나 이상 선택해주세요!")
    else:
        # 시드 고정 (매일 동일 결과)
        today = datetime.today().strftime("%Y-%m-%d")
        seed_input = str(birth_date) + today
        seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (10 ** 8)
        random.seed(seed)

        st.subheader("✨ 오늘의 운세 결과 ✨")

        for category in selected_types:
            message = random.choice(fortune_messages[category])
            score = random.randint(60, 100)
            lucky_color = random.choice(colors)
            lucky_item = random.choice(items)
            lucky_number = random.choice(numbers)

            st.markdown(f"""
            ### {category}
            **📖 운세 해석:** {message}  
            **⭐ 운세 점수:** {score}점 / 100  
            **🎨 행운의 색상:** {lucky_color}  
            **🎁 행운의 아이템:** {lucky_item}  
            **🔢 행운의 숫자:** {lucky_number}
            ---
            """)

        st.success("🎉 오늘 하루, 행운이 가득하길 바랍니다!")
