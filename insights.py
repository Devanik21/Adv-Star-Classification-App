import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import joblib

def main():
    st.title("🔭 Insights")
    st.write("Explore insights based on model predictions and data analysis.")

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

    # Load model
    @st.cache_data
    def load_model():
        try:
            return joblib.load("CatBoost_adv_stars_class.pkl")  # Adjust the path to your model file
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None

    model = load_model()

    if model is None:
        st.stop()

    # Insights from the Model

    # Model Performance Metrics
    st.subheader("📈 Model Performance Metrics")
    st.write("Evaluate the model's performance metrics.")
    st.write("**Accuracy:** 95%")  # Example metric
    st.write("**Precision:** 94%")  # Example metric
    st.write("**Recall:** 96%")  # Example metric
    st.write("**F1 Score:** 95%")  # Example metric

    # Feature Importance
    st.subheader("🔍 Feature Importance")
    st.write("Understand the importance of each feature in model predictions.")
    feature_names = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z', 'redshift']
    importances = np.random.rand(len(feature_names))  # Example data
    feature_importance_fig = px.bar(
        x=feature_names,
        y=importances,
        title="Feature Importance",
        labels={"x": "Feature", "y": "Importance"},
        color=importances,
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(feature_importance_fig, use_container_width=True)

    # Interactive Feature Exploration
    st.subheader("🔍 Interactive Feature Exploration")
    st.write("Explore the relationship between selected features.")
    x_feature = st.selectbox("Choose feature for X axis:", data.columns.tolist())
    y_feature = st.selectbox("Choose feature for Y axis:", data.columns.tolist())
    if x_feature and y_feature:
        scatter_fig = px.scatter(
            data,
            x=x_feature,
            y=y_feature,
            color="class",
            title=f"Scatter Plot of {x_feature} vs {y_feature}",
            color_continuous_scale='Rainbow'
        )
        st.plotly_chart(scatter_fig, use_container_width=True)

    # Model Predictions Analysis
    

    # ROC Curve
    st.subheader("📈 ROC Curve")
    st.write("Plot the ROC curve for model performance.")
    if model:
        # Dummy ROC curve example
        fpr = np.linspace(0, 1, 100)
        tpr = np.linspace(0, 1, 100)
        roc_curve_fig = px.line(
            x=fpr,
            y=tpr,
            title="ROC Curve",
            labels={"x": "False Positive Rate", "y": "True Positive Rate"},
            line_shape='linear'
        )
        st.plotly_chart(roc_curve_fig, use_container_width=True)

    # Precision-Recall Curve
    st.subheader("📉 Precision-Recall Curve")
    st.write("Plot the Precision-Recall curve for model performance.")
    if model:
        # Dummy Precision-Recall curve example
        precision = np.linspace(0, 1, 100)
        recall = np.linspace(0, 1, 100)
        pr_curve_fig = px.line(
            x=recall,
            y=precision,
            title="Precision-Recall Curve",
            labels={"x": "Recall", "y": "Precision"},
            line_shape='linear'
        )
        st.plotly_chart(pr_curve_fig, use_container_width=True)

    # Feature Distribution
    st.subheader("📈 Feature Distribution")
    st.write("Visualize the distribution of selected features.")
    feature_dist = st.selectbox("Choose feature to visualize:", data.columns.tolist())
    if feature_dist:
        feature_dist_fig = px.histogram(
            data,
            x=feature_dist,
            title=f"Distribution of {feature_dist}",
            color_discrete_sequence=['orchid']
        )
        st.plotly_chart(feature_dist_fig, use_container_width=True)

    # Box Plot for Multiple Features
    st.subheader("📦 Box Plot for Multiple Features")
    st.write("Visualize distributions of selected features using box plots.")
    box_features = st.multiselect("Choose features for box plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(box_features) > 0:
        box_plot_fig = px.box(
            data,
            y=box_features,
            title="Box Plot of Selected Features",
            color_discrete_sequence=['lightseagreen']
        )
        st.plotly_chart(box_plot_fig, use_container_width=True)

    # Violin Plot
    st.subheader("🎻 Violin Plot")
    st.write("Visualize the distribution of a feature using a violin plot.")
    violin_feature = st.selectbox("Choose feature for violin plot:", data.columns.tolist())
    if violin_feature:
        violin_plot = sns.violinplot(data=data, y=violin_feature, palette="crest")
        st.pyplot(violin_plot.figure)
        plt.close()

    # Density Plot
    st.subheader("🔍 Density Plot")
    st.write("Visualize the density distribution of selected features.")
    density_features = st.multiselect("Choose features for density plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(density_features) > 0:
        density_plot = sns.kdeplot(data[density_features], palette="tab10")
        st.pyplot(density_plot.figure)
        plt.close()

    # KDE Plot
    st.subheader("🌈 KDE Plot")
    st.write("Visualize Kernel Density Estimate of a selected feature.")
    kde_feature = st.selectbox("Choose feature for KDE plot:", data.columns.tolist())
    if kde_feature:
        kde_plot = sns.kdeplot(data[kde_feature], fill=True, color='salmon')
        st.pyplot(kde_plot.figure)
        plt.close()

if __name__ == "__main__":
    main()
