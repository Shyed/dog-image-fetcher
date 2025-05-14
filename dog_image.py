import requests
import webbrowser

API_URL = "https://dog.ceo/api/breeds/image/random"

def fetch_dog_image():
    try:
        print("🐾 Fetching a random dog image...")  # debug
        response = requests.get(API_URL)
        data = response.json()
        print("✅ API response received.")  # debug

        if data.get("status") == "success":
            return data["message"]
        else:
            return "❌ Error: No image URL returned."
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    print("=== Dog Image Fetcher ===")
    image_url = fetch_dog_image()

    if image_url.startswith("http"):
        print("\nHere’s a random dog image URL:")
        print(image_url)

        open_now = input("\nOpen this image in your browser? (y/n): ").strip().lower()
        if open_now == 'y':
            webbrowser.open(image_url)
    else:
        print(image_url)
