import os
import sys
import json
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import random

# Load CLIP model and processor
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")



app = Flask(__name__)

# List of example prompts
example_prompts = [
    "Upside Down dinosaur",
    "Rabbit are cooking carrets",
    "flaying pandas",
    "monkey man",
    "elephants with wings"

]

# Function to generate a random prompt
def generate_random_prompt():
    return random.choice(example_prompts)


def preprocess_image(image_path):
    image = Image.open(image_path)
    # Resize image to match CLIP model input size
    resized_image = image.resize((224, 224))
    return resized_image

def compute_similarity(drawing_image, prompt):
    # Preprocess the drawing image
    processed_drawing = clip_processor(text=prompt, images=drawing_image, return_tensors="pt", padding=True)

    # Forward pass through CLIP model
    with torch.no_grad():
        outputs = clip_model(**processed_drawing)
    
    # Retrieve embeddings
    drawing_embedding = outputs.last_hidden_state[:, 0, :]

    # Compute similarity score with prompt
    # You need to encode the prompt using the CLIP processor as well
    prompt_encoding = clip_processor.encode_text(prompt)
    similarity_score = torch.nn.functional.cosine_similarity(drawing_embedding, prompt_encoding).item()

    return similarity_score

@app.route('/', methods=['GET', 'POST'])
def paintapp():
    if request.method == 'GET':
        # Generate a random prompt
        prompt = generate_random_prompt()
        return render_template("paint.html", prompt=prompt)
    if request.method == 'POST':
        filename = request.form['save_fname']
        data = request.form['save_cdata']
        canvas_image = request.form['save_image']
        conn = psycopg2.connect(database="paintmyown", user = "ritchiepulkottil")
        cur = conn.cursor()
        cur.execute("INSERT INTO files (name, data, canvas_image) VALUES (%s, %s, %s)", [filename, data, canvas_image])
        conn.commit()
        conn.close()
        return redirect(url_for('save'))        


@app.route('/save', methods=['GET', 'POST'])
def save():
    conn = psycopg2.connect(database="paintmyown", user="ritchiepulikottil")
    cur = conn.cursor()
    cur.execute("SELECT id, name, data, canvas_image from files")
    files = cur.fetchall()
    conn.close()
    return render_template("save.html", files = files )

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template("search.html")
    if request.method == 'POST':
        filename = request.form['fname']
        conn = psycopg2.connect(database="paintmyown", user="ritchiepulikottil")
        cur = conn.cursor()
        cur.execute("select id, name, data, canvas_image from files")
        files = cur.fetchall()
        conn.close()
        return render_template("search.html", files=files, filename=filename)


@app.route('/compute_similarity', methods=['POST'])
def compute_and_display_similarity():
    drawing_image = request.files['drawing']
    prompt = request.form['prompt']

    # Preprocess image
    processed_image = preprocess_image(drawing_image)
    
    # Compute similarity score
    similarity_score = compute_similarity(processed_image, prompt)

    return render_template("similarity.html", similarity_score=similarity_score)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
