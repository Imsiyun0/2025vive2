import streamlit as st
import random

# 초기화 (앱 처음 실행할 때)
if "win" not in st.session_state:
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0

# 제목
st.title("✊✌️🖐️ 가위바위보 게임")
st.write("당신은 컴퓨터와 가위바위보 대결을 하게 됩니다!")

# 선택지
choices = ["가위", "바위", "보"]
user_choice = st.selectbox("당신의 선택은?", choices)

# 버튼 누르면 게임 실행
if st.button("대결!"):
    computer_choice = random.choice(choices)

    # 결과 계산
    if user_choice == computer_choice:
        result = "비겼어요! 😐"
        st.session_state.draw += 1
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        result = "이겼어요! 🎉"
        st.session_state.win += 1
        st.balloons()  # 승리 시 폭죽 효과
    else:
        result = "졌어요... 😢"
        st.session_state.lose += 1

    # 결과 출력
    st.markdown(f"### 당신: {user_choice}")
    st.markdown(f"### 컴퓨터: {computer_choice}")
    st.markdown(f"## 결과: {result}")

    # 통계 출력
    st.markdown("---")
    st.subheader("📊 전적")
    st.markdown(f"- 🏆 승: {st.session_state.win}")
    st.markdown(f"- 💥 패: {st.session_state.lose}")
    st.markdown(f"- 🤝 무승부: {st.session_state.draw}")

# 리셋 버튼
if st.button("전적 초기화"):
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0
    st.success("전적이 초기화되었습니다!")
