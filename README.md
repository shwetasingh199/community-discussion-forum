# 💬 Community Discussion Forum with Real-Time Chat 

A full-stack community platform built using **Streamlit, Python, and MongoDB**, featuring discussion forums, comments, likes, and real-time chat rooms.

This project simulates a modern community platform like Reddit + Discord (simplified version), ideal for showcasing full-stack development skills.

---

## 🎯 Features

### 👤 Authentication
- User registration
- Secure login system
- Session-based authentication

### 📚 Discussion Forum
- Create discussions
- Browse posts
- Search discussions
- Like system

### 💬 Comments System
- Add comments
- Real-time updates (via refresh)
- User-based commenting

### 🗨️ Chat System
- Multiple chat rooms
- Real-time messaging (auto refresh)
- User identity display
- Room-based messaging

### 📊 Dashboard
- Total users
- Total discussions
- Total comments
- Total messages

### 🔔 Notifications
- Comment notifications
- User interaction alerts

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** MongoDB Atlas
- **Authentication:** bcrypt + session state
- **Messaging:** MongoDB (real-time simulation)
- **Other Libraries:**
  - pymongo
  - streamlit-autorefresh
  - bcrypt
  - pyjwt
  - python-dotenv

---

## 📸 Screenshots

### Register Page
<img width="1842" height="811" alt="P5 O s1" src="https://github.com/user-attachments/assets/4f04e8ed-3df0-47fd-a795-0f7ce16a4e97" />

### 🔐 Login Page
<img width="1894" height="725" alt="P5 O s2" src="https://github.com/user-attachments/assets/a52d81ef-d53e-4e01-a8db-4800e546bcc2" />


### 🏠 Dashboard
<img width="1876" height="826" alt="P5 O s3" src="https://github.com/user-attachments/assets/eeb8bfb1-0a6b-4b08-affa-82897dd4f358" />

<img width="1739" height="844" alt="P5 O s4" src="https://github.com/user-attachments/assets/2b46a5b1-da33-482d-8d07-aa638f2f3a6a" />

<img width="1549" height="685" alt="P5 O s5" src="https://github.com/user-attachments/assets/d58a70c8-7ec5-4240-8236-a89e7cbe145b" />

<img width="1503" height="702" alt="P5 O s6" src="https://github.com/user-attachments/assets/2a682f0a-7c97-48aa-a59e-923f88e3b148" />

<img width="1538" height="788" alt="P5 O s7" src="https://github.com/user-attachments/assets/3348ef99-5bf0-4df1-923f-06bd99047ef2" />

<img width="1881" height="774" alt="P5 O s8" src="https://github.com/user-attachments/assets/9b8a9450-38f6-4813-b14b-ab10afc23065" />

### 📚 Discussions Page
<img width="1849" height="890" alt="P5 O s9" src="https://github.com/user-attachments/assets/d4d2b72f-ad31-469c-b85e-4ca82cf37b16" />

<img width="1829" height="870" alt="P5 O s10" src="https://github.com/user-attachments/assets/339e877a-2ce2-46a1-9389-5a3028083df8" />

### 📝 Create Discussion
<img width="1829" height="900" alt="P5 O s11" src="https://github.com/user-attachments/assets/91c7738c-e2cb-4705-a83b-045c7f874c60" />

<img width="1881" height="754" alt="P5 O s12" src="https://github.com/user-attachments/assets/a767c54d-1a38-4ef7-8ff9-6c16d72ea7ae" />

### 🗨️ Chat Room
<img width="1859" height="874" alt="P5 O s13" src="https://github.com/user-attachments/assets/e0bfb7e0-800b-4e32-b18b-4ae4b45d66c4" />

<img width="1881" height="872" alt="P5 O s14" src="https://github.com/user-attachments/assets/af9d564c-346d-4766-94c2-2e61702fcf44" />

---


## 📁 Project Structure

```
Community-Discussion-Forum/
│
├── app.py
│
├── auth/
│   ├── login.py
│   ├── register.py
│   └── auth_utils.py
│
├── pages/
│   ├── dashboard.py
│   ├── discussions.py
│   ├── discussion_detail.py
│   ├── create_discussion.py
│   ├── chat.py
│   └── profile.py
│
├── database/
│   └── mongodb.py
│
├── screenshots/
│   ├── login.png
│   ├── dashboard.png
│   ├── discussions.png
│   ├── create_discussion.png
│   ├── comments.png
│   └── chat.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/community-discussion-forum.git
cd community-discussion-forum
```

---

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables
Create `.env` file:

```
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
```

---

### 5️⃣ Run Application
```bash
streamlit run app.py
```

---

## 🧠 How It Works

```
User Registration → Login → Dashboard → Create Discussion → 
View Discussion → Add Comments → Chat Rooms → Notifications
```

---

## 💡 Key Highlights

- Clean modular code structure
- MongoDB integration
- Real-time chat simulation
- Authentication system
- Interactive UI with Streamlit
- Beginner-friendly full-stack project

---

## 📊 Database Collections

```
users
discussions
comments
messages
notifications
```

---

## 📸 Screenshot Guide

Save screenshots inside `/screenshots` folder:

| File Name | Page |
|----------|------|
| login.png | Login Page |
| dashboard.png | Dashboard |
| discussions.png | Discussion List |
| create_discussion.png | Create Discussion |
| comments.png | Discussion Detail |
| chat.png | Chat Room |

---

## 🔥 Future Improvements

- Real-time Socket.IO chat
- Post upvotes/downvotes
- User profiles with avatars
- Admin moderation panel
- Email notifications
- Search with filters

---

## 👨‍💻 Author

**SHWETA**  
Full Stack Developer (Student Project)

---

## ⭐ Show Your Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork it
- 📢 Share with others

---

## 📜 License

This project is for educational purposes.
```
