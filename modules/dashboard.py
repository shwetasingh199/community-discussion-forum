import streamlit as st
import pandas as pd
import plotly.express as px

from database.mongodb import (
    users,
    discussions,
    comments,
    messages,
    notifications
)


def dashboard_page():

    # ==============================
    # AUTH CHECK
    # ==============================

    if not st.session_state.get("authenticated", False):
        st.warning("Please login first.")
        st.stop()

    # ==============================
    # PAGE HEADER
    # ==============================

    st.title("📊 Community Dashboard")
    st.caption(
        "Monitor community growth, discussions, engagement, and activity."
    )

    st.divider()

    # ==============================
    # DATABASE COUNTS
    # ==============================

    total_users = users.count_documents({})

    total_discussions = discussions.count_documents({})

    total_comments = comments.count_documents({})

    total_messages = messages.count_documents({})

    # ==============================
    # KPI CARDS
    # ==============================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="👥 Users",
            value=total_users
        )

    with col2:
        st.metric(
            label="📝 Discussions",
            value=total_discussions
        )

    with col3:
        st.metric(
            label="💬 Comments",
            value=total_comments
        )

    with col4:
        st.metric(
            label="📨 Messages",
            value=total_messages
        )

    st.divider()

    # ==============================
    # RECENT DISCUSSIONS
    # ==============================

    st.subheader("🔥 Recent Discussions")

    recent_discussions = list(
        discussions.find()
        .sort("_id", -1)
        .limit(5)
    )

    if recent_discussions:

        for discussion in recent_discussions:

            title = discussion.get(
                "title",
                "Untitled Discussion"
            )

            content = discussion.get(
                "content",
                ""
            )

            author = discussion.get(
                "author",
                "Unknown User"
            )

            with st.container():

                st.markdown(f"### {title}")

                st.write(content[:250])

                st.caption(
                    f"Posted by: {author}"
                )

                st.divider()

    else:

        st.info(
            "No discussions available yet."
        )

    # ==============================
    # COMMUNITY ANALYTICS
    # ==============================

    st.subheader("📈 Community Analytics")

    analytics_df = pd.DataFrame({

        "Metric": [
            "Users",
            "Discussions",
            "Comments",
            "Messages"
        ],

        "Count": [
            total_users,
            total_discussions,
            total_comments,
            total_messages
        ]

    })

    chart = px.bar(
        analytics_df,
        x="Metric",
        y="Count",
        title="Community Overview"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    st.divider()

    # ==============================
    # TRENDING DISCUSSIONS
    # ==============================

    st.subheader("🚀 Trending Discussions")

    trending_posts = list(
        discussions.find()
        .limit(5)
    )

    if trending_posts:

        for post in trending_posts:

            st.success(
                f"🔥 {post.get('title', 'Untitled Discussion')}"
            )

    else:

        st.info(
            "No trending discussions available."
        )

    st.divider()

    # ==============================
    # NEW MEMBERS
    # ==============================

    st.subheader("👤 New Community Members")

    latest_users = list(
        users.find()
        .sort("_id", -1)
        .limit(5)
    )

    if latest_users:

        for user in latest_users:

            st.write(
                f"✅ {user.get('name', 'Unnamed User')}"
            )

    else:

        st.info(
            "No members found."
        )

    st.divider()

    # ==============================
    # NOTIFICATIONS
    # ==============================

    st.subheader("🔔 Notifications")

    current_user_email = (
        st.session_state["user"]["email"]
    )

    user_notifications = list(

        notifications.find({

            "user":
            current_user_email

        })

        .sort("_id", -1)

        .limit(5)

    )

    if user_notifications:

        for note in user_notifications:

            st.warning(
                note.get(
                    "message",
                    "New notification"
                )
            )

    else:

        st.info(
            "No notifications available."
        )

    st.divider()

    # ==============================
    # COMMUNITY HEALTH
    # ==============================

    st.subheader("🏆 Community Health")

    engagement_score = (
        total_comments +
        total_messages
    )

    progress_value = min(
        engagement_score,
        100
    )

    st.progress(progress_value)

    st.write(
        f"Current Engagement Score: {engagement_score}"
    )

    st.divider()

    # ==============================
    # USER ACTIVITY
    # ==============================

    st.subheader("📌 My Activity")

    my_email = (
        st.session_state["user"]["email"]
    )

    my_discussions = discussions.count_documents({

        "author":
        my_email

    })

    my_comments = comments.count_documents({

        "user":
        my_email

    })

    activity_col1, activity_col2 = st.columns(2)

    with activity_col1:

        st.metric(
            "My Discussions",
            my_discussions
        )

    with activity_col2:

        st.metric(
            "My Comments",
            my_comments
        )

    st.divider()

    # ==============================
    # FOOTER
    # ==============================

    st.caption(
        "Community Discussion Forum Dashboard • Streamlit + MongoDB Atlas"
    )