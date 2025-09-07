import requests

# Replace with your actual Stability API key
API_KEY = "sk-P26OoD1hcbLO0bDAeIVIbV1rRFItFxuDAhYXeBbnIJw0r8If"

# Path to your input image
image_path = r"C:\Users\SWAGAT\OneDrive - agilework\Desktop\projects\decorai\input_images\Screenshot 2025-08-31 202233.png"

# API endpoint
url = "https://api.stability.ai/v2beta/3d/stable-fast-3d"

# Prepare headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

# Prepare payload
files = {
    "image": open(image_path, "rb")
}
data = {
    "prompt": "This image is a collage showing five different views of the same motorcycle model — front-left, front-right, rear-left, rear-right, and side profile. The bike is a modern street-style design with a white fuel tank, black frame, alloy wheels, and compact headlight. Please use these visual references to generate a realistic 3D representation of the motorcycle, preserving its proportions, branding, and mechanical details. Focus on accurate geometry, lighting, and texture fidelity to reflect the real-world look of the bike.",  # <-- Add your prompt here
    "texture_resolution": "1024",       # Optional: 512, 1024, 2048
    "foreground_ratio": "0.85"          # Optional: between 0.0 and 1.0
}

# Make the request
response = requests.post(url, headers=headers, files=files, data=data)

# Save the GLB output if successful
if response.status_code == 200:
    with open("output_model.glb", "wb") as f:
        f.write(response.content)
    print("✅ 3D model saved as output_model.glb")
else:
    print("❌ Error:", response.status_code, response.text)
