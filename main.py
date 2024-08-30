import streamlit as st

# Page selection
page = st.sidebar.selectbox("Select a page", [
    "🚀 Predict",
    "✨ Recommend",
    "📊 Visualize",
    "🔍 Analyze",
    "🔭 Insights",
    "Gallery",
    "Feedback"
])

# Load the appropriate page based on the selection
if page == "🚀 Predict":
    import predict
elif page == "✨ Recommend":
    import recommend
elif page == "📊 Visualize":
    import visualize
elif page == "🔍 Analyze":
    import analyze
elif page == "🔭 Insights":
    import insights
elif page == "Gallery":
    import gallery
elif page == "Feedback":
    import feedback
