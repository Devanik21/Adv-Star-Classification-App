import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Custom CSS for advanced styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .main .block-container {
            padding: 2rem;
        }
        .stButton>button {
            background-color: #6200ea;
            color: #ffffff; /* Button text color */
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #3700b3;
        }
        .stSubheader {
            color: #ffffff;
        }
        .stMarkdown {
            color: #ffffff;
        }
        .st-expanderHeader {
            font-size: 20px;
            font-weight: bold;
        }
        .st-expanderContent {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Star Recommendation System")
    st.write("Explore stars similar to your selected type using advanced algorithms and interactive visualizations.")

    # Load dataset
    @st.cache
    def load_data():
        try:
            return pd.read_csv("star_classification.csv")
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return pd.DataFrame()

    data = load_data()

    if data.empty:
        st.stop()

    # Sidebar: Recommendation Inputs
    st.sidebar.header("Recommendation Inputs")

    star_type = st.sidebar.selectbox("Select a Star Type", ["Galaxy", "QSO", "Star"])
    find_similar_stars = st.sidebar.button("Find Similar Stars")

    alpha = st.sidebar.slider("Alpha", 0.0, 360.0, 180.0)
    delta = st.sidebar.slider("Delta", -90.0, 90.0, 0.0)
    u = st.sidebar.slider("u", 0.0, 30.0, 15.0)
    g = st.sidebar.slider("g", 0.0, 30.0, 15.0)
    r = st.sidebar.slider("r", 0.0, 30.0, 15.0)
    i = st.sidebar.slider("i", 0.0, 30.0, 15.0)
    z = st.sidebar.slider("z", 0.0, 30.0, 15.0)
    redshift = st.sidebar.slider("Redshift", 0.0, 10.0, 0.5)

    if find_similar_stars:
        filtered_data = data[data["class"] == star_type]
        
        if filtered_data.empty:
            st.error("No data available for the selected star type.")
        else:
            # Enhanced distance calculation with normalized features
            def calculate_distance(row):
                return np.sqrt(
                    (row["alpha"] - alpha)**2 +
                    (row["delta"] - delta)**2 +
                    (row["u"] - u)**2 +
                    (row["g"] - g)**2 +
                    (row["r"] - r)**2 +
                    (row["i"] - i)**2 +
                    (row["z"] - z)**2 +
                    (row["redshift"] - redshift)**2
                )

            filtered_data["distance"] = filtered_data.apply(calculate_distance, axis=1)
            recommendations = filtered_data.sort_values(by="distance").head(10)

            # Display recommendations
            st.subheader("Recommended Similar Stars")
            st.write("Here are the top 10 stars similar to your input:")

            # Display data in a table with conditional formatting
            st.dataframe(recommendations[["obj_ID", "alpha", "delta", "u", "g", "r", "i", "z", "redshift", "distance"]])

            # Interactive chart for distance distribution
            st.write("Distance distribution of recommended stars:")
            fig = px.bar(recommendations, x="obj_ID", y="distance", title="Distance of Recommended Stars")
            st.plotly_chart(fig)

            # Interactive scatter plot for features
            st.write("Feature distribution of recommended stars:")
            fig = go.Figure()
            for feature in ["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]:
                fig.add_trace(go.Scatter(
                    x=recommendations[feature],
                    y=recommendations["distance"],
                    mode='markers',
                    name=feature
                ))
            fig.update_layout(title="Feature vs Distance", xaxis_title="Feature Value", yaxis_title="Distance")
            st.plotly_chart(fig)

            # User feedback form
            with st.expander("Provide Feedback", expanded=True):
                feedback = st.text_area("Your feedback or comments:")
                if st.button("Submit Feedback"):
                    if feedback:
                        st.success("Thank you for your feedback!")
                    else:
                        st.warning("Please enter your feedback before submitting.")
                    
            # Additional insights or statistics
            st.subheader("Additional Insights")
            st.write(f"Average Distance: {recommendations['distance'].mean():.2f}")
            st.write(f"Maximum Distance: {recommendations['distance'].max():.2f}")
            st.write(f"Minimum Distance: {recommendations['distance'].min():.2f}")

if __name__ == "__main__":
    main()
