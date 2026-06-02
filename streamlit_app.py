import streamlit as st

st.title("📋 전체 세트 메뉴 판")

popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 기존의 print 대신 st.write나 st.text를 사용합니다.
st.subheader("주문 가능한 조합 목록")

for popcorn in popcorn_options:
    for drink in drink_options:
        st.write(f"• 세트 메뉴: **{popcorn}** 팝콘, **{drink}**")