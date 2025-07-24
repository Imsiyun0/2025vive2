import streamlit as st
import random

# 초기화: 정답이 없다면 무작위 숫자 선택
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 20)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# 제목
st.title("🔢 숫자 맞추기 게임")
st.write("1부터 20 사이의 숫자 중 하나를 맞춰보세요!")

# 사용자 입력
user_input = st.number_input("숫자를 입력하세요 (1~20)", min_value=1, max_value=20, step=1)

# 게임 진행
if st.button("제출"):
    st.session_state.attempts += 1
    answer = st.session_state.secret_number

    if user_input < answer:
        st.warning("up 📈")
    elif user_input > answer:
        st.warning("down 📉")
    else:
        st.success(f"🎉 정답입니다! 숫자는 {answer}였습니다.")
        st.balloons()
        st.info(f"총 {st.session_state.attempts}번 만에 맞췄어요!")
        # 게임 재시작을 위해 정답 초기화
        st.session_state.secret_number = random.randint(1, 20)
        st.session_state.attempts = 0

# 리셋 버튼
if st.button("게임 리셋하기"):
    st.session_state.secret_number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.info("새 게임이 시작되었습니다!")
