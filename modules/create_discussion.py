import streamlit as st
from datetime import datetime

from database.mongodb import discussions


def create_discussion_page():

    # ==================================
    # AUTH CHECK
    # ==================================

    if not st.session_state.get(
        "authenticated",
        False
    ):
        st.warning(
            "Please login first."
        )
        st.stop()

    # ==================================
    # PAGE HEADER
    # ==================================

    st.title("📝 Create Discussion")

    st.caption(
        "Start a new discussion and engage the community."
    )

    st.divider()

    # ==================================
    # DISCUSSION TITLE
    # ==================================

    title = st.text_input(
        "Discussion Title"
    )

    # ==================================
    # CATEGORY
    # ==================================

    category = st.selectbox(

        "Category",

        [
            "Programming",
            "Web Development",
            "Data Science",
            "Artificial Intelligence",
            "Machine Learning",
            "Career Guidance",
            "Internships",
            "College",
            "General Discussion"
        ]

    )

    # ==================================
    # TAGS
    # ==================================

    tags_input = st.text_input(

        "Tags (comma separated)",

        placeholder=
        "React, MongoDB, Python"

    )

    # ==================================
    # CONTENT
    # ==================================

    content = st.text_area(

        "Discussion Content",

        height=250,

        placeholder=
        "Write your discussion here..."

    )

    # ==================================
    # PREVIEW
    # ==================================

    st.subheader("📄 Preview")

    st.markdown(
        f"### {title}"
    )

    st.write(content)

    st.divider()

    # ==================================
    # SUBMIT BUTTON
    # ==================================

    if st.button(
        "🚀 Publish Discussion",
        use_container_width=True
    ):

        # ------------------------------
        # VALIDATION
        # ------------------------------

        if not title.strip():

            st.error(
                "Title is required."
            )

            return

        if not content.strip():

            st.error(
                "Content is required."
            )

            return

        # ------------------------------
        # PROCESS TAGS
        # ------------------------------

        tags = []

        if tags_input:

            tags = [

                tag.strip()

                for tag in
                tags_input.split(",")

                if tag.strip()

            ]

        # ------------------------------
        # CREATE DOCUMENT
        # ------------------------------

        discussion_data = {

            "title":
            title,

            "content":
            content,

            "category":
            category,

            "tags":
            tags,

            "author":
            st.session_state["user"]["email"],

            "author_name":
            st.session_state["user"]["name"],

            "views":
            0,

            "likes":
            0,

            "comments_count":
            0,

            "created_at":
            datetime.utcnow()

        }

        # ------------------------------
        # INSERT INTO DATABASE
        # ------------------------------

        discussions.insert_one(
            discussion_data
        )

        st.success(
            "Discussion published successfully!"
        )

        st.balloons()