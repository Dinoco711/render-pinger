import requests

# Replace this URL with your actual Render.com server URL
URL = "https://nexobotics-2.onrender.com/"

try:
    response = requests.get(URL)
    print(f"Pinged {URL}, status code: {response.status_code}")
except Exception as e:
    print(f"Failed to ping {URL}: {e}")
