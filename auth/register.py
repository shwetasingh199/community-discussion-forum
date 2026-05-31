import streamlit as st

from database.mongodb import users
from auth.auth_utils import hash_password


def register_page():

    st.title("📝 Register")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        # Validation
        if not name or not email or not password:

            st.error(
                "Please fill all fields."
            )

            return

        # Check if user already exists
        existing_user = users.find_one({

            "email": email

        })

        if existing_user:

            st.error(
                "Email already registered."
            )

            return

        # Save user
        users.insert_one({

            "name": name,

            "email": email,

            "password": hash_password(
                password
            )

        })

        st.success(
            "Registration Successful! Please login."
        )