import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

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

    # 2D Visualizations

    # Interactive Histogram
    st.subheader("🖼️ Interactive Histogram")
    st.write("Select a column to visualize its distribution.")
    column = st.selectbox("Choose column for histogram:", data.columns.tolist())
    if column:
        histogram_fig = px.histogram(data, x=column, nbins=20, title=f"Histogram of {column}")
        st.plotly_chart(histogram_fig)

    # Box Plot of Selected Column
    st.subheader("📊 Box Plot of Selected Column")
    st.write("Select a column to show the distribution.")
    column_box = st.selectbox("Choose column for box plot:", data.columns.tolist())
    if column_box:
        box_plot = px.box(data, y=column_box, title=f"Box Plot of {column_box}")
        st.plotly_chart(box_plot)

    # Violin Plot of Selected Column
    st.subheader("🎻 Violin Plot of Selected Column")
    st.write("Select a column to visualize its distribution using a violin plot.")
    column_violin = st.selectbox("Choose column for violin plot:", data.columns.tolist())
    if column_violin:
        violin_plot = sns.violinplot(data[column_violin])
        st.pyplot(violin_plot.figure)
        plt.close()  # Close the figure to avoid display issues

    # Correlation Heatmap
    st.subheader("🌡️ Feature Correlation Heatmap")
    st.write("Select columns to show correlations.")
    columns_heatmap = st.multiselect("Choose columns for correlation heatmap:", data.columns.tolist(), default=["alpha", "delta", "u", "g", "r", "i", "z", "redshift"])
    if len(columns_heatmap) > 1:
        correlation_matrix = data[columns_heatmap].corr()
        heatmap_fig = px.imshow(correlation_matrix, text_auto=True, title="Feature Correlation Heatmap")
        st.plotly_chart(heatmap_fig)
    else:
        st.warning("Select at least two columns for correlation heatmap.")

    # Pie Chart of Star Types
    st.subheader("🥧 Star Type Distribution")
    st.write("Pie chart showing the distribution of star types.")
    star_type_dist = data["class"].value_counts()
    pie_chart_fig = px.pie(values=star_type_dist.values, names=star_type_dist.index, title="Star Type Distribution")
    st.plotly_chart(pie_chart_fig)

    # Line Chart of Average `alpha` by Star Type
 

    # Area Chart of Star Counts by `redshift`



    # Additional 2D and 3D Plots

    # Line Plot of Selected Columns
    st.subheader("📈 Line Plot of Selected Columns")
    st.write("Select columns to visualize their trends over the index.")
    columns_line = st.multiselect("Choose columns for line plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_line) > 0:
        line_plot_fig = px.line(data, y=columns_line, title="Line Plot of Selected Columns")
        st.plotly_chart(line_plot_fig)

    # Histogram of Selected Columns


    # Box Plot of Multiple Columns
    st.subheader("📊 Box Plot of Multiple Columns")
    st.write("Select columns to show their distributions using box plots.")
    columns_box = st.multiselect("Choose columns for box plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_box) > 0:
        box_plot_fig = px.box(data, y=columns_box, title="Box Plot of Selected Columns")
        st.plotly_chart(box_plot_fig)

# Scatter Plot with Regression Line
    st.subheader("📉 Scatter Plot with Regression Line")
    st.write("Select two columns to visualize their relationship along with a regression line.")
    x_column = st.selectbox("Choose X-axis column for scatter plot:", data.columns.tolist(), key="x_scatter")
    y_column = st.selectbox("Choose Y-axis column for scatter plot:", data.columns.tolist(), key="y_scatter")
    if x_column and y_column:
       scatter_reg_fig = px.scatter(data, x=x_column, y=y_column, trendline="ols", title=f"Scatter Plot of {x_column} vs {y_column} with Regression Line")
       st.plotly_chart(scatter_reg_fig)


     # Heatmap of Selected Features


if __name__ == "__main__":
    main()
