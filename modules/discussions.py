import streamlit as st
from database.mongodb import discussions


def discussions_page():

    st.title("📚 Community Discussions")

    # ==========================
    # SEARCH BAR
    # ==========================

    search = st.text_input(
        "🔍 Search Discussions"
    )

    # ==========================
    # FETCH DATA
    # ==========================

    if search:

        posts = discussions.find({

            "title": {

                "$regex": search,

                "$options": "i"

            }

        }).sort("_id", -1)

    else:

        posts = discussions.find().sort(
            "_id",
            -1
        )

    posts = list(posts)

    # ==========================
    # NO POSTS
    # ==========================

    if len(posts) == 0:

        st.info(
            "No discussions available."
        )

        return

    # ==========================
    # DISPLAY POSTS
    # ==========================

    for post in posts:

        title = post.get(
            "title",
            "Untitled"
        )

        content = post.get(
            "content",
            ""
        )

        author = post.get(
            "author_name",
            "Unknown"
        )

        likes = post.get(
            "likes",
            0
        )

        views = post.get(
            "views",
            0
        )

        category = post.get(
            "category",
            "General"
        )

        tags = post.get(
            "tags",
            []
        )

        with st.container():

            st.subheader(title)

            st.write(
                content[:200] + "..."
                if len(content) > 200
                else content
            )

            st.caption(
                f"👤 {author}"
            )

            st.write(
                f"📂 Category: {category}"
            )

            if tags:

                st.write(
                    "🏷️ Tags:",
                    ", ".join(tags)
                )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"👍 {likes}"
                )

            with col2:

                st.write(
                    f"👀 {views}"
                )

            with col3:

                if st.button(
                    "👍 Like",
                    key=f"like_{post['_id']}"
                ):

                    discussions.update_one(

                        {
                            "_id":
                            post["_id"]
                        },

                        {
                            "$inc":
                            {"likes": 1}
                        }

                    )

                    st.rerun()

            if st.button(
                "📖 Open Discussion",
                key=f"open_{post['_id']}"
            ):

                st.session_state.selected_post = str(
                    post["_id"]
                )

                st.session_state.page = (
                    "discussion_detail"
                )

                st.rerun()

            st.divider()