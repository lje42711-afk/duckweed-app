import streamlit as st
import numpy as np
import pandas as pd

# 제목
st.title("아세트아미노펜 생태 영향 시뮬레이션")

st.write("농도를 선택하면 개구리밥의 생장 반응을 예측합니다.")

# 실험 데이터
x_data = np.array([0, 0.1, 0.5, 1, 5, 10, 20, 50])
y_data = np.array([3.48, 3.34, 3.10, 3.79, 3.35, 3.39, 3.30, 3.13])

# 입력 (슬라이더)
conc = st.slider("아세트아미노펜 농도 (mg/L)", 0.0, 50.0, 5.0)

# 보간 (예측값 계산)
growth = np.interp(conc, x_data, y_data)

# 결과 출력
st.subheader("예측 결과")
st.write(f"🌱 예상 생장 배율: {growth:.2f}")

# 위험 수준 표시
if conc < 1:
    st.success("🟢 낮은 영향 가능성")
elif conc < 10:
    st.warning("🟡 생리적 스트레스 가능성")
else:
    st.error("🔴 생장 저해 및 생리적 이상 가능성")

# 데이터프레임 생성
df = pd.DataFrame({
    "농도 (mg/L)": x_data,
    "생장 배율": y_data
})

# 그래프 (한글 문제 없는 Streamlit 그래프)
st.subheader("농도에 따른 개구리밥 생장 변화")
st.line_chart(df.set_index("농도 (mg/L)"))

# 현재 위치 강조 표시
st.write(f"📍 현재 선택 농도: {conc} mg/L → 생장 배율 {growth:.2f}")

# 교육 메시지
st.info("💡 폐의약품은 수생태계에 영향을 줄 수 있으므로 올바른 분리배출이 필요합니다.")
