import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Community Discussion Forum",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# IMPORT AUTH PAGES
# =====================================

from auth.login import login_page
from auth.register import register_page

# =====================================
# IMPORT APP PAGES
# =====================================

from modules.dashboard import dashboard_page
from modules.discussions import discussions_page
from modules.discussion_detail import discussion_detail_page
from modules.create_discussion import create_discussion_page
from modules.chat import chat_page
from modules.profile import profile_page

# =====================================
# SESSION STATE INITIALIZATION
# =====================================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# =====================================
# APP HEADER
# =====================================

st.title("💬 Community Discussion Forum")

st.caption(
    "A Community Platform with Discussions, Comments, Chat and Notifications"
)

st.divider()

# =====================================
# USER NOT LOGGED IN
# =====================================

if not st.session_state.authenticated:

    st.sidebar.title("Authentication")

    auth_option = st.sidebar.radio(
        "Choose Option",
        [
            "Login",
            "Register"
        ]
    )

    if auth_option == "Login":

        login_page()

    else:

        register_page()

# =====================================
# USER LOGGED IN
# =====================================

else:

    # =================================
    # SIDEBAR USER INFO
    # =================================

    st.sidebar.success("Logged In")

    st.sidebar.write(
        f"👤 {st.session_state.user['name']}"
    )

    st.sidebar.write(
        f"📧 {st.session_state.user['email']}"
    )

    st.sidebar.divider()

    # =================================
    # NAVIGATION MENU
    # =================================

    menu = st.sidebar.selectbox(

        "Navigation",

        [
            "Dashboard",
            "Discussions",
            "Create Discussion",
            "Chat",
            "Profile"
        ]

    )

    st.sidebar.divider()

    # =================================
    # LOGOUT BUTTON
    # =================================

    if st.sidebar.button("🚪 Logout"):

        st.session_state.authenticated = False
        st.session_state.user = None

        if "selected_post" in st.session_state:
            del st.session_state["selected_post"]

        st.session_state.page = "dashboard"

        st.success("Logged Out Successfully")

        st.rerun()

    # =================================
    # DISCUSSION DETAIL PAGE PRIORITY
    # =================================

    if st.session_state.get("page") == "discussion_detail":

        discussion_detail_page()

    else:

        # =============================
        # DASHBOARD
        # =============================

        if menu == "Dashboard":

            dashboard_page()

        # =============================
        # DISCUSSIONS
        # =============================

        elif menu == "Discussions":

            st.session_state.page = "discussions"

            discussions_page()

        # =============================
        # CREATE DISCUSSION
        # =============================

        elif menu == "Create Discussion":

            create_discussion_page()

        # =============================
        # CHAT
        # =============================

        elif menu == "Chat":

            chat_page()

        # =============================
        # PROFILE
        # =============================

        elif menu == "Profile":

            profile_page()

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Built with ❤️ using Streamlit + MongoDB Atlas"
)