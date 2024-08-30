import streamlit as st

# Set page configuration once at the start
st.set_page_config(page_title="Star Classification App", page_icon="🌟", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
        }
        .stSidebar .stSelectbox div {
            color: #007bff;
        }
        .stButton button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .page-title {
            color: #007bff;
            font-size: 24px;
            font-weight: bold;
        }
        .page-content {
            color: #333;
            font-size: 18px;
        }
        .emoji {
            font-size: 30px;
            vertical-align: middle;
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

# Adding a footer
st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <p class="page-content">Made with ❤️ by [Your Name]</p>
    </div>
""", unsafe_allow_html=True)
