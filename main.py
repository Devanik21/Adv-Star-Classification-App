import streamlit as st
from streamlit.components.v1 import html

# Set page configuration once at the start
st.set_page_config(page_title="Star Classification App", page_icon="🌟", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #0d1117;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #161b22;
        }
        .stSidebar .stSelectbox div {
            color: #78b2f0;
        }
        .stButton button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .page-title {
            color: #58a6ff;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .page-content {
            color: #c9d1d9;
            font-size: 18px;
            line-height: 1.6;
        }
        .emoji {
            font-size: 30px;
            vertical-align: middle;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background-color: #161b22;
            color: #97c769;
            border-radius: 5px;
            margin-top: 20px;
        }
        .footer p {
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Dynamic loading indicator
loading_indicator = st.empty()

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

# Load the appropriate page with a loading indicator
loading_indicator.markdown("⏳ Loading...")
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

loading_indicator.empty()

# Adding a footer with interactive elements
footer_html = """
    <div class="footer">
        <p style="color: #333;">Made with ❤️ by Devanik + Niki</p>
        <p>
            <a href="https://github.com/Devanik21" target="_blank" style="color: #58a6ff;">GitHub</a>
        </p>
    </div>
"""
html(footer_html)


