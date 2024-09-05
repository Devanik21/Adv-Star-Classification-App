import streamlit as st
import os

# Custom CSS for adding background color and styling
def add_custom_css():
    st.markdown(
        """
        <style>
        .stSubheader {
            color: white;
            background-color: #6c63ff;
            padding: 0.5rem;
            border-radius: 5px;
            font-weight: bold;
        }
        .stWarning {
            background-color: #f39c12;
            color: black;
            padding: 1rem;
            border-radius: 5px;
        }
        .stMarkdown {
            font-size: 1.1rem;
            color: #3498db;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_images(category, image_list):
    """Display images in a grid format with custom design."""
    st.subheader(f"✨ {category}")
    if image_list:
        cols = st.columns(5)  # Display 5 images per row
        for idx, image in enumerate(image_list):
            with cols[idx % 5]:  # Display in a grid format
                st.image(image, use_column_width=True, caption=f"📸 {os.path.basename(image).split('.')[0]}")
    else:
        st.warning(f"No images found for {category}. Ensure the image files are in the correct folder.")

def load_images_from_folder(folder_path, image_extensions=[".jpg", ".png"]):
    """Load image file paths from a specified folder."""
    try:
        return [
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
            if os.path.splitext(file)[1].lower() in image_extensions and os.path.exists(os.path.join(folder_path, file))
        ]
    except FileNotFoundError:
        st.error(f"Directory {folder_path} not found.")
        return []

def main():
    add_custom_css()
    
    st.title("🌠 Astronomy Image Gallery")
    st.markdown("### Explore breathtaking images from across the universe:")
    st.markdown("Galaxies 🌌, Quasars (QSO) 💫, and Stars ⭐!")

    # Define the base directory and categories
    base_dir = "Gallery"
    categories = {
        "Galaxy": os.path.join(base_dir, "Galaxy"),
        "QSO": os.path.join(base_dir, "QSO"),
        "Star": os.path.join(base_dir, "STAR")
    }

    # Allow users to select categories interactively with colorful emojis
    selected_categories = st.multiselect(
        "🌈 Select Categories to Display", options=categories.keys(), default=list(categories.keys())
    )

    # Display images based on selected categories
    for category in selected_categories:
        path = categories[category]
        if os.path.exists(path):
            image_list = load_images_from_folder(path)
            display_images(category, image_list)
        else:
            st.error(f"⚠️ Directory {path} not found. Please check the folder structure.")

    # Add a colorful footer with spacing
    st.markdown("---")
    st.markdown("📸 *Images courtesy of astronomy enthusiasts around the globe.*", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
