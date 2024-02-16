# Our MVP

This Flask web application allows users to draw an image based on a given prompt and then compares the similarity between the drawn image and the prompt using the OpenAI CLIP (Contrastive Language-Image Pre-training) model.

## Features

- **Paint Page**: Users can draw an image based on a provided prompt.
- **Prompt Generator**: Users can receive a random prompt to inspire their drawing.
- **Gallery**: Saved image gallery 
- **Similarity Comparison**: The drawn image is compared with the provided prompt using CLIP, and the similarity percentage is displayed.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/mayuras7685/Starknet-submission.git
    ```

2. Navigate to the project directory:

    ```bash
    cd MVP
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python main.py
    ```

5. Access the web application in your browser at `http://localhost:5000`.

## Usage

1. Draw an image based on the provided prompt on the paint page.
2. Click on the "Generate Prompt" button to receive a random prompt if desired.
3. Click on the "Submit" button to compare your drawing with the provided prompt.
4. View the similarity percentage and the original prompt.

## Dependencies

- Flask: Web framework for building the application.
- PyTorch: Deep learning library used for CLIP model integration.
- Transformers: Library for natural language understanding (NLU) and natural language generation (NLG) tasks, including CLIP.
- Pillow: Image processing library used for handling images.

## License

This project is licensed under the [MIT License](LICENSE).
