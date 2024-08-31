import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

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
        .stMarkdown {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Star Recommendation System")
    st.write("Use this tool to find stars similar to your selected star type based on various parameters.")

    # Load dataset
    @st.cache_data
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
            
            # Display data in a table
            st.dataframe(recommendations[["obj_ID", "alpha", "delta", "u", "g", "r", "i", "z", "redshift", "distance"]])
            
            # Distance Distribution
            st.write("Distance distribution of recommended stars:")
            distance_fig = px.histogram(recommendations, x="distance", nbins=20, title="Distance Distribution of Recommended Stars")
            st.plotly_chart(distance_fig)

            # Interactive 2D Scatter Plots (replacing 3D plots)
            st.write("Interactive scatter plots of selected features:")
            
            # Plot 1: alpha vs delta
            scatter_alpha_delta = px.scatter(
                recommendations,
                x="alpha",
                y="delta",
                color="distance",
                title="Scatter Plot: Alpha vs Delta",
                labels={"alpha": "Alpha", "delta": "Delta", "distance": "Distance"}
            )
            st.plotly_chart(scatter_alpha_delta)
            
            # Plot 2: u vs g
            scatter_u_g = px.scatter(
                recommendations,
                x="u",
                y="g",
                color="distance",
                title="Scatter Plot: u vs g",
                labels={"u": "u", "g": "g", "distance": "Distance"}
            )
            st.plotly_chart(scatter_u_g)
            
            # Pair Plot of Features
            st.write("Pair plot of the features of recommended stars:")
            pair_plot_fig = sns.pairplot(recommendations[["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]])
            st.pyplot(pair_plot_fig)
            
            # Feature Correlation Heatmap
            st.write("Feature correlation heatmap of recommended stars:")
            correlation_matrix = recommendations[["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]].corr()
            heatmap_fig = px.imshow(correlation_matrix, text_auto=True, title="Feature Correlation Heatmap")
            st.plotly_chart(heatmap_fig)
            
            # Star Type Distribution
            st.write("Distribution of Star Types in the Dataset:")
            star_type_dist = data["class"].value_counts()
            pie_chart_fig = px.pie(values=star_type_dist.values, names=star_type_dist.index, title="Distribution of Star Types")
            st.plotly_chart(pie_chart_fig)
            

if __name__ == "__main__":
    main()
