import requests
from PIL import Image
from io import BytesIO
import urllib.parse
import time


def generate_image(prompt, output_path="post_image.png", retries=3) -> bool:
    encoded_prompt = urllib.parse.quote(prompt)

    url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width=1024&height=1024&seed=42"
    )

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=20)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image.save(output_path)
                print(f"✅ Image generated successfully → {output_path}")
                return True
            else:
                print(
                    f"⚠️ Attempt {attempt}: Image API returned "
                    f"{response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Attempt {attempt}: Image API error → {e}")

        time.sleep(2)

    print("❌ Image generation skipped (API unstable)")
    return False
