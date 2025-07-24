import streamlit as st
import random

# 초기화 (앱 처음 실행할 때)
if "score" not in st.session_state:
    st.session_state.score = 0

# 제목
st.title("✊✌️🖐️ 가위바위보 점수제 게임")

# 게임 설명
with st.expander("📘 게임 설명 보기"):
    st.markdown("""
    이 게임은 전통적인 **가위바위보**를 기반으로 점수를 획득하는 방식입니다.

    - ✌️ **가위**, ✊ **바위**, 🖐️ **보** 중 하나를 선택하세요.
    - 컴퓨터와 대결하여 결과에 따라 점수를 받습니다:
        - 🎉 **이기면 +2점**
        - 🤝 **비기면 +1점**
        - 😢 **지면 -1점**
    - 누적 점수는 화면 아래에 표시됩니다.

    🔁 `점수 초기화` 버튼을 눌러 언제든 점수를 리셋할 수 있어요.
    """)

# 선택지
choices = ["가위", "바위", "보"]
user_choice = st.selectbox("당신의 선택은?", choices)

# 버튼 누르면 게임 실행
if st.button("대결!"):
    computer_choice = random.choice(choices)

    # 결과 및 점수 계산
    if user_choice == computer_choice:
        result = "비겼어요! 🤝"
        st.session_state.score += 1
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        result = "이겼어요! 🎉"
        st.session_state.score += 2
        st.balloons()
    else:
        result = "졌어요... 😢"
        st.session_state.score -= 1

    # 결과 출력
    st.markdown(f"### 당신: {user_choice}")
    st.markdown(f"### 컴퓨터: {computer_choice}")
    st.markdown(f"## 결과: {result}")

    # 점수 출력
    st.markdown("---")
    st.subheader("🏅 현재 점수")
    st.markdown(f"## **{st.session_state.score}점**")

# 점수 초기화
if st.button("점수 초기화"):
    st.session_state.score = 0
    st.success("점수가 초기화되었습니다!")
