import streamlit as st
import pandas as pd
import numpy as np

# Custom CSS for styling
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
            color: white;
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
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Star Recommendation System")
    st.write("Use this tool to find stars similar to your selected star type based on various parameters.")

    # Load dataset
    @st.cache
    def load_data():
        try:
            return pd.read_csv("star_classification.csv")
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return pd.DataFrame()  # Return empty DataFrame in case of error

    data = load_data()

    if data.empty:
        st.stop()

    # Sidebar: Recommendation Inputs
    st.sidebar.header("Recommendation Inputs")
    
    star_type = st.sidebar.selectbox("Select a Star Type", ["Galaxy", "QSO", "Star"])

    # Place the button at the top of the sidebar
    find_similar_stars = st.sidebar.button("Find Similar Stars")

    # Define sliders
    alpha = st.sidebar.slider("Alpha", 0.0, 360.0, 180.0)
    delta = st.sidebar.slider("Delta", -90.0, 90.0, 0.0)
    u = st.sidebar.slider("u", 0.0, 30.0, 15.0)
    g = st.sidebar.slider("g", 0.0, 30.0, 15.0)
    r = st.sidebar.slider("r", 0.0, 30.0, 15.0)
    i = st.sidebar.slider("i", 0.0, 30.0, 15.0)
    z = st.sidebar.slider("z", 0.0, 30.0, 15.0)
    redshift = st.sidebar.slider("Redshift", 0.0, 10.0, 0.5)

    if find_similar_stars:
        # Filter the dataset based on star type
        filtered_data = data[data["class"] == star_type]
        
        if filtered_data.empty:
            st.error("No data available for the selected star type.")
        else:
            # Find similar stars based on feature proximity
            def calculate_distance(row):
                return abs(row["alpha"] - alpha) + abs(row["delta"] - delta) + \
                       abs(row["u"] - u) + abs(row["g"] - g) + \
                       abs(row["r"] - r) + abs(row["i"] - i) + \
                       abs(row["z"] - z) + abs(row["redshift"] - redshift)

            filtered_data["distance"] = filtered_data.apply(calculate_distance, axis=1)
            recommendations = filtered_data.sort_values(by="distance").head(10)

            st.subheader("Recommended Similar Stars")
            st.write("Here are the top 10 stars similar to your input:")
            st.write(recommendations[["obj_ID", "alpha", "delta", "u", "g", "r", "i", "z", "redshift"]])
            
            # Optional: Display a sample visualization of distances
            st.write("Distance distribution of recommended stars:")
            st.bar_chart(recommendations.set_index('obj_ID')['distance'])

if __name__ == "__main__":
    main()
