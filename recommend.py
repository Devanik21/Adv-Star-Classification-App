import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
        .stSubheader, .stMarkdown {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Set Seaborn theme for consistency
sns.set_theme(style="darkgrid", palette="deep")

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
            distance_fig = px.histogram(recommendations, x="distance", nbins=20, title="Distance Distribution of Recommended Stars", color_discrete_sequence=px.colors.sequential.Plasma)
            st.plotly_chart(distance_fig)

            # 2D Scatter Plots
            st.write("2D scatter plots of selected features:")

            # Plot 1: alpha vs delta
            scatter_2d_alpha_delta = sns.scatterplot(x="alpha", y="delta", hue="distance", data=recommendations, palette="viridis")
            plt.title("Scatter Plot: Alpha vs Delta")
            st.pyplot(scatter_2d_alpha_delta.figure)
            
            # Plot 2: u vs g
            scatter_2d_u_g = sns.scatterplot(x="u", y="g", hue="distance", data=recommendations, palette="coolwarm")
            plt.title("Scatter Plot: u vs g")
            st.pyplot(scatter_2d_u_g.figure)
            
            # Plot 3: r vs i
            scatter_2d_r_i = sns.scatterplot(x="r", y="i", hue="distance", data=recommendations, palette="magma")
            plt.title("Scatter Plot: r vs i")
            st.pyplot(scatter_2d_r_i.figure)
            
            # Plot 4: z vs redshift
            scatter_2d_z_redshift = sns.scatterplot(x="z", y="redshift", hue="distance", data=recommendations, palette="Spectral")
            plt.title("Scatter Plot: z vs Redshift")
            st.pyplot(scatter_2d_z_redshift.figure)

            # Pair Plot of Features
            st.write("Pair plot of the features of recommended stars:")
            pair_plot_fig = sns.pairplot(recommendations[["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]], palette="coolwarm")
            st.pyplot(pair_plot_fig)

            # Feature Correlation Heatmap
            st.write("Feature correlation heatmap of recommended stars:")
            correlation_matrix = recommendations[["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]].corr()
            heatmap_fig, ax = plt.subplots()
            sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", ax=ax)
            ax.set_title("Feature Correlation Heatmap")
            st.pyplot(heatmap_fig)
            
            # Star Type Distribution
            st.write("Distribution of Star Types in the Dataset:")
            star_type_dist = data["class"].value_counts()
            pie_chart_fig = px.pie(values=star_type_dist.values, names=star_type_dist.index, title="Distribution of Star Types", color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(pie_chart_fig)

if __name__ == "__main__":
    main()
