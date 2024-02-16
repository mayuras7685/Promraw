from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from io import BytesIO
import base64
import torch
from transformers import CLIPProcessor, CLIPModel
import torchvision.transforms as transforms

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Dummy prompts for demonstration
prompts = [
    "Draw a smiling sun.",
    "Sketch a tree with a swing.",
    "Create a picture of a house with a red door.",
    "Draw a cat chasing a mouse.",
    "Sketch a cup of coffee on a saucer.",
]

def generate_prompt():
    return np.random.choice(prompts)

@app.route('/')
def index():
    prompt = generate_prompt()
    return render_template('index.html', prompt=prompt)

@app.route('/compare', methods=['POST'])
def compare():
    # Get user's drawing and prompt
    user_image = request.form['userImage']
    prompt = request.form['prompt']

    # Decode base64 image
    user_image = base64.b64decode(user_image.split(',')[1])

    # Convert base64 image to PIL image
    user_image = Image.open(BytesIO(user_image))

    # Ensure image is in RGB format
    if user_image.mode != 'RGB':
        user_image = user_image.convert('RGB')

    # Resize image to match CLIP's requirements
    preprocess = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    user_image = preprocess(user_image)

    # Normalize image manually
    user_image = user_image * 255.0  # Scale up to the range [0, 255]
    user_image = user_image.byte()    # Convert to byte tensor
    user_image = user_image.float()   # Convert to float tensor for further processing

    # Preprocess prompt
    inputs = processor(
        text=prompt,
        images=user_image.unsqueeze(0),  # Add batch dimension
        return_tensors="pt",
        padding=True,
    )

    # Forward pass through CLIP
    with torch.no_grad():
        inputs = {key: val.to(device) for key, val in inputs.items()}
        outputs = model(**inputs)
        user_embedding = outputs.logits_per_image

    print("User Embedding Shape:", user_embedding.shape)
    print("User Embedding:", user_embedding)

    # Dummy prompt embedding (you may want to encode the prompt text to get its embedding)
    prompt_embedding = torch.randn(user_embedding.shape, device=device)

    print("Prompt Embedding Shape:", prompt_embedding.shape)
    print("Prompt Embedding:", prompt_embedding)

    # Calculate cosine similarity between user's drawing and prompt
    similarity = torch.nn.functional.cosine_similarity(user_embedding, prompt_embedding, dim=1).item()

    print("Cosine Similarity:", similarity)

    # Calculate percentage (for demonstration purposes)
    percentage = int((similarity + 1) / 2 * 100)  # Convert similarity to percentage

    return render_template('result.html', prompt=prompt, similarity=percentage)

if __name__ == '__main__':
    app.run(debug=True)
