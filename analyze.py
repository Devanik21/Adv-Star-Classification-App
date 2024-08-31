import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("🔍 Analyze")
    st.write("Explore data analysis and statistical summaries here.")

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

    # Data Analysis & Statistics

    # Descriptive Statistics
    st.subheader("📊 Descriptive Statistics")
    st.write("Basic statistical summary of the dataset.")
    if not data.empty:
        st.write(data.describe())

    # Correlation Matrix
    st.subheader("🌡️ Correlation Matrix")
    st.write("Correlation matrix of selected columns.")
    columns_corr = st.multiselect("Choose columns for correlation matrix:", data.columns.tolist(), default=["alpha", "delta", "u", "g", "r", "i", "z", "redshift"])
    if len(columns_corr) > 1:
        correlation_matrix = data[columns_corr].corr()
        st.write(correlation_matrix)
        heatmap_fig = px.imshow(correlation_matrix, text_auto=True, title="Correlation Matrix")
        st.plotly_chart(heatmap_fig)
    else:
        st.warning("Select at least two columns for correlation matrix.")

    # Skewness and Kurtosis
    st.subheader("📉 Skewness and Kurtosis")
    st.write("Skewness and kurtosis for selected columns.")
    columns_skew_kurt = st.multiselect("Choose columns for skewness and kurtosis:", data.columns.tolist(), default=["alpha", "delta", "u"])
    if len(columns_skew_kurt) > 0:
        skewness = data[columns_skew_kurt].skew()
        kurtosis = data[columns_skew_kurt].kurtosis()
        st.write("Skewness:")
        st.write(skewness)
        st.write("Kurtosis:")
        st.write(kurtosis)

    # Histograms
    st.subheader("🖼️ Histograms")
    st.write("Select a column to visualize its distribution.")
    column_histogram = st.selectbox("Choose column for histogram:", data.columns.tolist())
    if column_histogram:
        histogram_fig = px.histogram(data, x=column_histogram, nbins=20, title=f"Histogram of {column_histogram}")
        st.plotly_chart(histogram_fig)

    # Box Plot
    st.subheader("📊 Box Plot")
    st.write("Select a column to show the distribution.")
    column_box = st.selectbox("Choose column for box plot:", data.columns.tolist())
    if column_box:
        box_plot = px.box(data, y=column_box, title=f"Box Plot of {column_box}")
        st.plotly_chart(box_plot)

    # Violin Plot
    st.subheader("🎻 Violin Plot")
    st.write("Select a column to visualize its distribution using a violin plot.")
    column_violin = st.selectbox("Choose column for violin plot:", data.columns.tolist())
    if column_violin:
        violin_plot = sns.violinplot(data[column_violin])
        st.pyplot(violin_plot.figure)
        plt.close()

    # Correlation Heatmap
    st.subheader("🌡️ Correlation Heatmap")
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

    # Line Chart
    st.subheader("📈 Line Chart")
    st.write("Select columns to visualize their trends over the index.")
    columns_line = st.multiselect("Choose columns for line plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_line) > 0:
        line_chart_fig = px.line(data, y=columns_line, title="Line Plot of Selected Columns")
        st.plotly_chart(line_chart_fig)

    # Area Chart of Star Counts by `redshift`
    st.subheader("📊 Area Chart of Star Counts by Redshift")
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

    # Scatter Plot
    st.subheader("🔍 Scatter Plot")
    st.write("Select columns to visualize the relationship between them.")
    x_axis = st.selectbox("Choose column for X axis:", data.columns.tolist())
    y_axis = st.selectbox("Choose column for Y axis:", data.columns.tolist())
    if x_axis and y_axis:
        scatter_fig = px.scatter(data, x=x_axis, y=y_axis, title=f"Scatter Plot of {x_axis} vs {y_axis}")
        st.plotly_chart(scatter_fig)

    # Heatmap
    st.subheader("🌡️ Heatmap of Values")
    st.write("Select columns to create a heatmap.")
    columns_heatmap_values = st.multiselect("Choose columns for heatmap:", data.columns.tolist(), default=["alpha", "delta", "u"])
    if len(columns_heatmap_values) > 1:
        heatmap_matrix = data[columns_heatmap_values].corr()
        heatmap_fig = px.imshow(heatmap_matrix, text_auto=True, title="Heatmap of Values")
        st.plotly_chart(heatmap_fig)
    else:
        st.warning("Select at least two columns for heatmap.")

    # KDE Plot
    st.subheader("🌈 KDE Plot")
    st.write("Select a column to show its Kernel Density Estimate.")
    column_kde = st.selectbox("Choose column for KDE plot:", data.columns.tolist())
    if column_kde:
        kde_plot = sns.kdeplot(data[column_kde], fill=True)
        st.pyplot(kde_plot.figure)
        plt.close()

    # Density Plot
    st.subheader("🔍 Density Plot")
    st.write("Select columns to visualize their density distribution.")
    columns_density = st.multiselect("Choose columns for density plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_density) > 0:
        density_plot = sns.kdeplot(data[columns_density])
        st.pyplot(density_plot.figure)
        plt.close()

    # Box Plot for Multiple Columns
    st.subheader("📦 Box Plot for Multiple Columns")
    st.write("Select columns to visualize their distributions using box plots.")
    columns_box_multiple = st.multiselect("Choose columns for box plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_box_multiple) > 0:
        box_plot_multiple_fig = px.box(data, y=columns_box_multiple, title="Box Plot of Selected Columns")
        st.plotly_chart(box_plot_multiple_fig)

    # Histogram for Multiple Columns
    st.subheader("📊 Histogram for Multiple Columns")
    st.write("Select columns to visualize their distribution in histograms.")
    columns_histogram_multiple = st.multiselect("Choose columns for histogram:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_histogram_multiple) > 0:
        histogram_multiple_fig = px.histogram(data, y=columns_histogram_multiple, nbins=20, title="Histogram of Selected Columns")
        st.plotly_chart(histogram_multiple_fig)

    # Violin Plot for Multiple Columns
    st.subheader("🎻 Violin Plot for Multiple Columns")
    st.write("Select columns to visualize their distributions using violin plots.")
    columns_violin_multiple = st.multiselect("Choose columns for violin plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(columns_violin_multiple) > 0:
        for col in columns_violin_multiple:
            violin_plot = sns.violinplot(data[col])
            st.pyplot(violin_plot.figure)
            plt.close()

if __name__ == "__main__":
    main()
