import streamlit as st

from bson import ObjectId

from database.mongodb import (
    discussions,
    comments,
    notifications
)


def discussion_detail_page():

    # ==========================
    # CHECK SELECTED POST
    # ==========================

    if "selected_post" not in st.session_state:

        st.warning(
            "Please select a discussion."
        )

        return

    # ==========================
    # GET DISCUSSION
    # ==========================

    post = discussions.find_one({

        "_id": ObjectId(
            st.session_state.selected_post
        )

    })

    if not post:

        st.error(
            "Discussion not found."
        )

        return

    # ==========================
    # INCREASE VIEW COUNT
    # ==========================

    discussions.update_one(

        {
            "_id": post["_id"]
        },

        {
            "$inc":
            {"views": 1}
        }

    )

    # ==========================
    # HEADER
    # ==========================

    st.title(post["title"])

    st.caption(
        f"👤 {post['author_name']}"
    )

    st.write(
        f"📂 Category: "
        f"{post['category']}"
    )

    st.write(
        f"👍 {post.get('likes',0)}"
    )

    st.write(
        f"👀 {post.get('views',0)+1}"
    )

    st.divider()

    # ==========================
    # CONTENT
    # ==========================

    st.markdown(
        post["content"]
    )

    st.divider()

    # ==========================
    # COMMENTS SECTION
    # ==========================

    st.subheader("💬 Comments")

    all_comments = comments.find({

        "discussion_id":
        str(post["_id"])

    })

    all_comments = list(all_comments)

    if len(all_comments) == 0:

        st.info(
            "No comments yet."
        )

    else:

        for comment in all_comments:

            st.markdown(
                f"**{comment['user']}**"
            )

            st.write(
                comment["comment"]
            )

            st.divider()

    # ==========================
    # ADD COMMENT
    # ==========================

    st.subheader(
        "✍️ Add Comment"
    )

    new_comment = st.text_area(
        "Write your comment"
    )

    if st.button(
        "Post Comment"
    ):

        if not new_comment.strip():

            st.error(
                "Comment cannot be empty."
            )

        else:

            comments.insert_one({

                "discussion_id":
                str(post["_id"]),

                "user":
                st.session_state
                ["user"]["email"],

                "comment":
                new_comment

            })

            # ======================
            # NOTIFICATION
            # ======================

            if (
                post["author"]
                !=
                st.session_state
                ["user"]["email"]
            ):

                notifications.insert_one({

                    "user":
                    post["author"],

                    "message":
                    f"{st.session_state['user']['name']} commented on your discussion."

                })

            st.success(
                "Comment added."
            )

            st.rerun()

    st.divider()

    # ==========================
    # BACK BUTTON
    # ==========================

    if st.button(
        "⬅ Back to Discussions"
    ):

        if "selected_post" in st.session_state:

            del st.session_state[
                "selected_post"
            ]

        st.session_state.page = (
            "discussions"
        )

        st.rerun()