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
    if model:
        # Replace with actual metrics if you have them
        st.write("Accuracy: 95%")  # Example metric
        st.write("Precision: 94%")  # Example metric
        st.write("Recall: 96%")  # Example metric
        st.write("F1 Score: 95%")  # Example metric

    # Feature Importance
    st.subheader("🔍 Feature Importance")
    st.write("Understand the importance of each feature in model predictions.")
    if model:
        # Example feature importance
        # Replace with actual feature importances if available
        feature_names = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z', 'redshift']
        importances = np.random.rand(len(feature_names))  # Example data
        feature_importance_fig = px.bar(
            x=feature_names,
            y=importances,
            title="Feature Importance",
            labels={"x": "Feature", "y": "Importance"}
        )
        st.plotly_chart(feature_importance_fig)

    # Interactive Feature Exploration
    st.subheader("🔍 Interactive Feature Exploration")
    st.write("Explore the relationship between selected features.")
    x_feature = st.selectbox("Choose feature for X axis:", data.columns.tolist())
    y_feature = st.selectbox("Choose feature for Y axis:", data.columns.tolist())
    if x_feature and y_feature:
        scatter_fig = px.scatter(data, x=x_feature, y=y_feature, color="class", title=f"Scatter Plot of {x_feature} vs {y_feature}")
        st.plotly_chart(scatter_fig)

    # Model Predictions Analysis
    st.subheader("🔮 Model Predictions Analysis")
    st.write("Analyze the distribution of model predictions.")
    st.write("Select features for prediction:")
    features = st.multiselect("Choose features for prediction:", data.columns.tolist(), default=['alpha', 'delta', 'u'])
    if len(features) > 0:
        # Dummy example of generating predictions
        # Replace with actual prediction code
        predictions = model.predict(data[features])
        data['predictions'] = predictions
        prediction_dist_fig = px.histogram(data, x='predictions', title="Distribution of Model Predictions")
        st.plotly_chart(prediction_dist_fig)

    # Confusion Matrix
    st.subheader("🔍 Confusion Matrix")
    st.write("Visualize the confusion matrix of model predictions.")
    if model:
        # Dummy confusion matrix example
        # Replace with actual confusion matrix if available
        confusion_matrix = np.array([[50, 10], [5, 100]])  # Example data
        confusion_matrix_fig = px.imshow(confusion_matrix, color_continuous_scale='Blues', title="Confusion Matrix")
        st.plotly_chart(confusion_matrix_fig)

    # ROC Curve
    st.subheader("📈 ROC Curve")
    st.write("Plot the ROC curve for model performance.")
    if model:
        # Dummy ROC curve example
        # Replace with actual ROC curve data if available
        fpr = np.linspace(0, 1, 100)
        tpr = np.linspace(0, 1, 100)
        roc_curve_fig = px.line(
            x=fpr,
            y=tpr,
            title="ROC Curve",
            labels={"x": "False Positive Rate", "y": "True Positive Rate"}
        )
        st.plotly_chart(roc_curve_fig)

    # Precision-Recall Curve
    st.subheader("📉 Precision-Recall Curve")
    st.write("Plot the Precision-Recall curve for model performance.")
    if model:
        # Dummy Precision-Recall curve example
        # Replace with actual Precision-Recall data if available
        precision = np.linspace(0, 1, 100)
        recall = np.linspace(0, 1, 100)
        pr_curve_fig = px.line(
            x=recall,
            y=precision,
            title="Precision-Recall Curve",
            labels={"x": "Recall", "y": "Precision"}
        )
        st.plotly_chart(pr_curve_fig)

    # Feature Distribution
    st.subheader("📈 Feature Distribution")
    st.write("Visualize the distribution of selected features.")
    feature_dist = st.selectbox("Choose feature to visualize:", data.columns.tolist())
    if feature_dist:
        feature_dist_fig = px.histogram(data, x=feature_dist, title=f"Distribution of {feature_dist}")
        st.plotly_chart(feature_dist_fig)

    # Pairwise Relationships
    st.subheader("🔍 Pairwise Relationships")
    st.write("Visualize pairwise relationships between selected features.")
    pair_features = st.multiselect("Choose features for pairwise relationships:", data.columns.tolist(), default=["alpha", "delta", "u"])
    if len(pair_features) > 1:
        pairwise_fig = sns.pairplot(data[pair_features])
        st.pyplot(pairwise_fig.figure)
        plt.close()

    # Violin Plot
    st.subheader("🎻 Violin Plot")
    st.write("Visualize the distribution of a feature using a violin plot.")
    violin_feature = st.selectbox("Choose feature for violin plot:", data.columns.tolist())
    if violin_feature:
        violin_plot = sns.violinplot(data[violin_feature])
        st.pyplot(violin_plot.figure)
        plt.close()

    # Box Plot for Multiple Features
    st.subheader("📦 Box Plot for Multiple Features")
    st.write("Visualize distributions of selected features using box plots.")
    box_features = st.multiselect("Choose features for box plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(box_features) > 0:
        box_plot_fig = px.box(data, y=box_features, title="Box Plot of Selected Features")
        st.plotly_chart(box_plot_fig)

    # Density Plot
    st.subheader("🔍 Density Plot")
    st.write("Visualize the density distribution of selected features.")
    density_features = st.multiselect("Choose features for density plot:", data.columns.tolist(), default=["alpha", "delta"])
    if len(density_features) > 0:
        density_plot = sns.kdeplot(data[density_features])
        st.pyplot(density_plot.figure)
        plt.close()

    # KDE Plot
    st.subheader("🌈 KDE Plot")
    st.write("Visualize Kernel Density Estimate of a selected feature.")
    kde_feature = st.selectbox("Choose feature for KDE plot:", data.columns.tolist())
    if kde_feature:
        kde_plot = sns.kdeplot(data[kde_feature], fill=True)
        st.pyplot(kde_plot.figure)
        plt.close()

if __name__ == "__main__":
    main()
