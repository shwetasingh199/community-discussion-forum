import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

from database.mongodb import messages


def chat_page():

    # =====================================
    # AUTH CHECK
    # =====================================

    if not st.session_state.get("authenticated", False):
        st.warning("Please login first.")
        st.stop()

    # =====================================
    # PAGE HEADER
    # =====================================

    st.title("💬 Community Chat Rooms")

    st.caption(
        "Join community rooms and chat with other members."
    )

    # =====================================
    # AUTO REFRESH
    # =====================================

    st_autorefresh(
        interval=3000,
        key="chat_refresh"
    )

    # =====================================
    # CHAT ROOMS
    # =====================================

    rooms = [
        "General",
        "Programming",
        "Web Development",
        "AI & ML",
        "Career Guidance"
    ]

    selected_room = st.selectbox(
        "Select Chat Room",
        rooms
    )

    st.divider()

    # =====================================
    # ROOM STATS
    # =====================================

    total_messages = messages.count_documents({
        "room": selected_room
    })

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Room",
            selected_room
        )

    with col2:
        st.metric(
            "Messages",
            total_messages
        )

    st.divider()

    # =====================================
    # CHAT HISTORY
    # =====================================

    st.subheader(
        f"📨 {selected_room} Chat"
    )

    room_messages = list(

        messages.find({
            "room": selected_room
        })

        .sort("_id", -1)

        .limit(50)

    )

    room_messages.reverse()

    chat_container = st.container(
        border=True
    )

    with chat_container:

        if len(room_messages) == 0:

            st.info(
                "No messages yet."
            )

        else:

            for msg in room_messages:

                username = msg.get(
                    "user_name",
                    "Unknown"
                )

                text = msg.get(
                    "message",
                    ""
                )

                timestamp = msg.get(
                    "timestamp",
                    ""
                )

                st.markdown(
                    f"""
                    **👤 {username}**

                    {text}

                    <small>{timestamp}</small>
                    """,
                    unsafe_allow_html=True
                )

                st.divider()

    # =====================================
    # SEND MESSAGE
    # =====================================

    st.subheader("✍️ Send Message")

    message = st.text_input(
        "Type your message",
        key="message_input"
    )

    col1, col2 = st.columns([4, 1])

    with col2:

        send = st.button(
            "Send",
            use_container_width=True
        )

    if send:

        if not message.strip():

            st.error(
                "Message cannot be empty."
            )

        else:

            messages.insert_one({

                "room":
                selected_room,

                "user":
                st.session_state["user"][
                    "email"
                ],

                "user_name":
                st.session_state["user"][
                    "name"
                ],

                "message":
                message,

                "timestamp":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

            })

            st.rerun()

    st.divider()

    # =====================================
    # RECENT ACTIVITY
    # =====================================

    st.subheader("🔥 Recent Activity")

    latest_messages = list(

        messages.find()

        .sort("_id", -1)

        .limit(5)

    )

    if latest_messages:

        for msg in latest_messages:

            st.write(
                f"💬 {msg.get('user_name')} "
                f"in {msg.get('room')}"
            )

    else:

        st.info(
            "No recent activity."
        )