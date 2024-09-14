import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pytesseract
import openai

# Configure your API keys and paths
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
CHROMEDRIVER_PATH = 'path/to/chromedriver'  # Path to your ChromeDriver executable

# Configure Tesseract path if necessary
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust this for your OS

def capture_screenshot(url, file_name):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run headlessly
    chrome_options.add_argument('--window-size=1920x1080')

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Wait for page to load completely
        driver.save_screenshot(file_name)
    finally:
        driver.quit()

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def analyze_with_ai(text):
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Review the following LinkedIn profile text and suggest improvements:\n\n{text}",
        max_tokens=150
    )

    return response.choices[0].text.strip()

def main():
    profile_url = 'https://www.linkedin.com/in/some-profile/'  # Replace with actual profile URL
    screenshot_path = 'profile_screenshot.png'

    try:
        # Step 1: Capture screenshot
        capture_screenshot(profile_url, screenshot_path)

        # Step 2: Extract text from screenshot
        profile_text = extract_text_from_image(screenshot_path)

        # Step 3: Analyze text using AI
        suggestions = analyze_with_ai(profile_text)

        # Step 4: Print suggestions
        print("Profile Review Suggestions:")
        print(suggestions)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
