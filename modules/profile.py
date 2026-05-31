import streamlit as st


def profile_page():

    st.title("👤 Profile")

    st.write(
        "Name:",
        st.session_state.user["name"]
    )

    st.write(
        "Email:",
        st.session_state.user["email"]
    )