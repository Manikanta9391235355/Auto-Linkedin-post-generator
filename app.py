import os
import streamlit as st

from text_generator import generate_text
from image_generator import generate_image
from linkedin_post import (
    register_image_upload,
    upload_image,
    create_post
)

IMAGE_PATH = "post_image.png"

# -------------------- Streamlit Config --------------------
st.set_page_config(
    page_title="LinkedIn AI Post Generator",
    page_icon="💼",
    layout="centered"
)

st.title("💼 LinkedIn AI Post Generator & Publisher")
st.write("Generate AI-powered LinkedIn posts with optional images and publish instantly.")

# -------------------- User Input --------------------
topic = st.text_input("Enter topic for LinkedIn post")

post_with_image = st.checkbox("Generate & post with image", value=True)

# -------------------- Action Button --------------------
if st.button("🚀 Generate & Post"):
    if not topic.strip():
        st.error("❌ Topic cannot be empty")

    else:
        # 1️⃣ Generate Text
        with st.spinner("✍️ Generating LinkedIn post text..."):
            post_text = generate_text(topic)

        st.subheader("✅ Generated LinkedIn Post")
        st.text_area("Post Preview", post_text, height=220)

        # 2️⃣ Generate Image (Optional)
        image_created = False

        if post_with_image:
            with st.spinner("🖼️ Generating image..."):
                try:
                    generate_image(topic)
                    image_created = os.path.exists(IMAGE_PATH)

                    if image_created:
                        st.image(
                            IMAGE_PATH,
                            caption="Generated Post Image",
                            width=700
                        )
                    else:
                        st.warning("⚠️ Image was not created. Will post text-only.")

                except Exception as e:
                    st.warning(f"⚠️ Image generation failed: {e}")

        # 3️⃣ Post to LinkedIn
        with st.spinner("📤 Posting to LinkedIn..."):
            try:
                if image_created:
                    upload_url, asset_urn = register_image_upload()
                    upload_image(upload_url)
                    result = create_post(post_text, asset_urn)
                else:
                    result = create_post(post_text, None)

                st.success("🎉 Post published successfully!")

            except Exception as e:
                st.error(f"❌ Failed to post on LinkedIn: {e}")
