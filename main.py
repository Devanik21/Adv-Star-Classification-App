import streamlit as st

# Set page configuration once at the start
st.set_page_config(page_title="Star Classification App", page_icon="🌟🔭", layout="wide")

# Page selection
page = st.sidebar.selectbox("Select a page", [
    "🚀 Predict",
    "✨ Recommend",
    "📊 Visualize",
    "🔍 Analyze",
    "🔭 Insights",
    "Gallery",
    "Feedback",
    "📚 About"
])

# Load the appropriate page based on the selection
if page == "🚀 Predict":
    import predict
    predict.main()  # Ensure that you have a `main()` function in `predict.py`
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
elif page == "Gallery":
    import gallery
    gallery.main()
elif page == "Feedback":
    import feedback
    feedback.main()
elif page == "📚 About":
    import about
    about.main()
