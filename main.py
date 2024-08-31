import streamlit as st
from streamlit.components.v1 import html

# Set page configuration once at the start
st.set_page_config(page_title="Star Classification App", page_icon="🌟", layout="wide")

# Sidebar image
st.sidebar.image("Universe_2.jpg", use_column_width=True)

# Custom CSS for colorful and interactive styling
st.markdown("""
    <style>
        body {
            background-color: #e6f7ff;
            font-family: 'Arial', sans-serif;
            margin: 0;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
            padding: 20px;
        }
        .stSidebar .stSelectbox div {
            color: #cc2b0e;
            font-weight: bold;
        }
        .stButton button {
            background-color: #705a5a;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #ff4500;
        }
        .page-content {
            color: #333;
            font-size: 18px;
            line-height: 1.6;
            margin: 20px;
        }
        .emoji {
            font-size: 30px;
            vertical-align: middle;
        }
        .footer {
            text-align: center;
            padding: 15px;
            background-color: #333;
            color: #ff6347;
            border-radius: 8px;
            margin-top: 40px;
            font-size: 14px;
        }
        .footer p {
            margin: 0;
            font-size: 16px;
        }
        .footer a {
            color: #1e90ff;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .theme-toggle {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            cursor: pointer;
            border-radius: 8px;
            background-color: #ff6347;
            color: white;
            font-weight: bold;
            text-align: center;
        }
        .theme-toggle:hover {
            background-color: #ff4500;
        }
    </style>
""", unsafe_allow_html=True)

# Theme Toggle


# Page selection with emojis
page = st.sidebar.selectbox("Select a page", [
    "🚀 Predict",
    "✨ Recommend",
    "📊 Visualize",
    "🔍 Analyze",
    "🔭 Insights",
    "🖼️ Gallery",
    "📝 Feedback",
    "📚 About"
])

# User Interaction: Ask for user's name and display a greeting
user_name = st.text_input("Please enter your name:", placeholder=" Your name ")
if user_name:
    st.markdown(f"### Welcome to the Star Classification App, {user_name}! 🌟")

# Load the appropriate page based on the selection
if page == "🚀 Predict":
    import predict
    predict.main()
elif page == "✨ Recommend":
    import recommend
    recommend.main()
elif page == "📊 Visualize":
    import visualize
    visualize.main()
elif page == "🔍 Analyze":
    import analyze
    analyze.main()
elif page == "🔭 Insights":
    import insights
    insights.main()
elif page == "🖼️ Gallery":
    import gallery
    gallery.main()
elif page == "📝 Feedback":
    import feedback
    feedback.main()
elif page == "📚 About":
    import about
    about.main()

# Display the main image below the title
st.image("Galaxy.jpg", caption="A glimpse of the galaxy", use_column_width=True)

# Adding a footer with colorful styling
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by Devanik + Niki</p>
        <p>
            <a href="https://github.com/Devanik21" target="_blank">GitHub</a>
        </p>
    </div>
""", unsafe_allow_html=True)
