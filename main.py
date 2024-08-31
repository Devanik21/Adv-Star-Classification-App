import streamlit as st
from streamlit.components.v1 import html

# Set page configuration once at the start
st.set_page_config(page_title="Star Classification App", page_icon="🌟", layout="wide")

# Custom CSS for advanced styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Arial', sans-serif;
            margin: 0;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
            padding: 20px;
        }
        .stSidebar .stSelectbox div {
            color: #007bff;
            font-weight: bold;
        }
        .stButton button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .page-title {
            color: #007bff;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .page-content {
            color: #333;
            font-size: 18px;
            line-height: 1.6;
        }
        .emoji {
            font-size: 30px;
            vertical-align: middle;
        }
        .footer {
            text-align: center;
            padding: 15px;
            background-color: #333;
            color: #97c769;
            border-radius: 8px;
            margin-top: 40px;
        }
        .footer p {
            margin: 0;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

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

# Adding a footer with professional styling
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by Devanik + Niki</p>
        <p>
            <a href="https://github.com/Devanik21" target="_blank" style="color: #58a6ff; text-decoration: none;">GitHub</a>
        </p>
    </div>
""", unsafe_allow_html=True)
