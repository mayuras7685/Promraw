import cv2
import inference
from inference.models import Clip # add
from inference.core.utils.postprocess import cosine_similarity

clip = Clip()
prompt = "Smiling Sun"
text_embedding = clip.embed_text(prompt)

def render(result, image):
    # get the cosine similarity between the prompt & the image
    similarity = cosine_similarity(result["embeddings"][0], text_embedding[0])

    # scale the result to 0-100 based on heuristic (~the best & worst values I've observed)
    range = (0.15, 0.40)
    similarity = (similarity-range[0])/(range[1]-range[0])
    similarity = max(min(similarity, 1), 0)*100

    # print the similarity
    text = f"{similarity:.1f}%"
  
    cv2.putText(image, text, (10, 310),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (206, 6, 103), 5)

    # print the prompt

    cv2.putText(image, prompt, (10, 330),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (206, 6, 103), 5)

    # display the image
    cv2.imshow("CLIP", image)
    cv2.waitKey(1)
    

inference.Stream(
    source = 0,
    model = clip,

    use_main_thread = True,
    output_channel_order = "BGR",

    on_prediction = render
)