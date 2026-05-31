import streamlit as st

from database.mongodb import users
from auth.auth_utils import verify_password


def login_page():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if not email or not password:

            st.error(
                "Please fill all fields."
            )
            return

        user = users.find_one({
            "email": email
        })

        if user is None:

            st.error(
                "User not found. Please register first."
            )
            return

        if verify_password(
            password,
            user["password"]
        ):

            st.session_state.authenticated = True

            st.session_state.user = {
                "name": user["name"],
                "email": user["email"]
            }

            st.success(
                "Login Successful"
            )

            st.rerun()

        else:

            st.error(
                "Incorrect Password"
            )