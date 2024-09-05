import streamlit as st
import os

def display_images(category, image_list):
    st.subheader(category)
    if image_list:
        cols = st.columns(5)  # Display 5 images per row
        for idx, image in enumerate(image_list):
            with cols[idx % 5]:  # Display in a grid format
                st.image(image, use_column_width=True, caption=os.path.basename(image).split('.')[0])
    else:
        st.write(f"⚠️ No images found for {category}. Please ensure the image files are in the correct folder.")

def load_images_from_folder(folder_path, image_extensions=[".jpg", ".png"]):
    """Load image file paths from a specified folder."""
    return [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.splitext(file)[1].lower() in image_extensions and os.path.exists(os.path.join(folder_path, file))
    ]

def main():
    st.title("🌌 Astronomy Image Gallery")
    st.write("Explore stunning images from different astronomical categories including Galaxies, Quasars (QSO), and Stars.")

    # Define the directories for each category
    base_dir = "Gallery"
    categories = {
        "Galaxy": os.path.join(base_dir, "Galaxy"),
        "QSO": os.path.join(base_dir, "QSO"),
        "Star": os.path.join(base_dir, "STAR")
    }

    # Load images dynamically from each folder
    for category, path in categories.items():
        if os.path.exists(path):
            image_list = load_images_from_folder(path)
            display_images(category, image_list)
        else:
            st.write(f"⚠️ Directory {path} not found. Please check the folder structure.")

if __name__ == "__main__":
    main()
