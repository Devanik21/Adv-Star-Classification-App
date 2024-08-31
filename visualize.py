import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np

def main():
    st.title("📊 Visualize")
    st.write("Explore various visualizations of star data to gain insights.")

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

    # Display column names to debug
    st.write("Columns in dataset:", data.columns.tolist())

    # Visualization 1: Histogram of Distances
    st.warning("Column 'distance' not found in the dataset, skipping Distance Distribution visualization.")

    # Visualization 2: Box Plot of `alpha` Values
    st.subheader("2. Box Plot of Alpha Values")
    st.write("Box plot to show the distribution of `alpha` values.")
    alpha_box_plot = px.box(data, y="alpha", title="Box Plot of Alpha Values")
    st.plotly_chart(alpha_box_plot)

    # Visualization 3: Pair Plot
    st.subheader("3. Pair Plot of Features")
    st.write("Pair plot to show relationships between various features.")
    pair_plot_fig = sns.pairplot(data[["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]])
    st.pyplot(pair_plot_fig)

    # Visualization 4: Correlation Heatmap
    st.subheader("4. Feature Correlation Heatmap")
    st.write("Heatmap showing correlations between features.")
    correlation_matrix = data[["alpha", "delta", "u", "g", "r", "i", "z", "redshift"]].corr()
    heatmap_fig = px.imshow(correlation_matrix, text_auto=True, title="Feature Correlation Heatmap")
    st.plotly_chart(heatmap_fig)

    # Visualization 5: Pie Chart of Star Types
    st.subheader("5. Star Type Distribution")
    st.write("Pie chart showing the distribution of star types.")
    star_type_dist = data["class"].value_counts()
    pie_chart_fig = px.pie(values=star_type_dist.values, names=star_type_dist.index, title="Star Type Distribution")
    st.plotly_chart(pie_chart_fig)

    # Visualization 6: 3D Scatter Plot of `alpha`, `delta`, and `u`
    st.subheader("6. 3D Scatter Plot: Alpha vs Delta vs u")
    st.write("3D scatter plot of `alpha`, `delta`, and `u`.")
    scatter_3d_alpha_delta_u = px.scatter_3d(
        data,
        x="alpha",
        y="delta",
        z="u",
        title="3D Scatter Plot: Alpha vs Delta vs u"
    )
    st.plotly_chart(scatter_3d_alpha_delta_u)

    # Visualization 7: 3D Scatter Plot of `g`, `r`, and `i`
    st.subheader("7. 3D Scatter Plot: g vs r vs i")
    st.write("3D scatter plot of `g`, `r`, and `i`.")
    scatter_3d_gri = px.scatter_3d(
        data,
        x="g",
        y="r",
        z="i",
        title="3D Scatter Plot: g vs r vs i"
    )
    st.plotly_chart(scatter_3d_gri)

    # Visualization 8: 3D Scatter Plot of `z`, `redshift`, and `alpha`
    st.subheader("8. 3D Scatter Plot: z vs Redshift vs Alpha")
    st.write("3D scatter plot of `z`, `redshift`, and `alpha`.")
    scatter_3d_z_redshift_alpha = px.scatter_3d(
        data,
        x="z",
        y="redshift",
        z="alpha",
        title="3D Scatter Plot: z vs Redshift vs Alpha"
    )
    st.plotly_chart(scatter_3d_z_redshift_alpha)

    # Visualization 9: Line Chart of Average `alpha` by Star Type
    st.subheader("9. Average Alpha by Star Type")
    st.write("Line chart showing trends in `alpha` values by star type.")
    avg_alpha_by_type = data.groupby("class")["alpha"].mean().reset_index()
    line_chart_fig = px.line(avg_alpha_by_type, x="class", y="alpha", title="Average Alpha by Star Type")
    st.plotly_chart(line_chart_fig)

    # Visualization 10: Area Chart of Star Counts by `redshift`
    st.subheader("10. Star Counts by Redshift")
    st.write("Area chart showing counts of stars grouped by `redshift` values.")
    redshift_counts = data["redshift"].value_counts().reset_index()
    redshift_counts.columns = ["redshift", "count"]  # Rename columns to match what Plotly expects
    area_chart_fig = px.area(
        redshift_counts,
        x="redshift",
        y="count",
        title="Star Counts by Redshift",
        labels={"redshift": "Redshift", "count": "Star Counts"}
    )
    st.plotly_chart(area_chart_fig)

if __name__ == "__main__":
    main()
