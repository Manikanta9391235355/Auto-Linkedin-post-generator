import os
from text_generator import generate_text
from image_generator import generate_image
from linkedin_post import (
    register_image_upload,
    upload_image,
    create_post
)

IMAGE_PATH = "post_image.png"

if __name__ == "__main__":
    topic = input("Enter topic for LinkedIn post: ").strip()

    if not topic:
        print("❌ Topic cannot be empty")
        exit()

    # 1️⃣ Generate text
    post_text = generate_text(topic)
    print("\n✅ Generated LinkedIn Post:\n")
    print(post_text)

    # 2️⃣ Try generating image
    image_created = False
    try:
        generate_image(topic)
        image_created = os.path.exists(IMAGE_PATH)
    except Exception as e:
        print("⚠️ Image generation failed:", e)

    # 3️⃣ Post to LinkedIn
    if image_created:
        print("📤 Posting with image...")
        upload_url, asset_urn = register_image_upload()
        upload_image(upload_url)
        result = create_post(post_text, asset_urn)
    else:
        print("📤 Posting text-only (no image)...")
        result = create_post(post_text, None)

    print("\n✅ LinkedIn Post Response:")
    print(result)
