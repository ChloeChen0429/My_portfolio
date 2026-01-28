import streamlit as st
import cv2
import torch
import numpy as np
from PIL import Image, ImageDraw
from torchvision import transforms, models
from diffusers import StableDiffusionPipeline
import tempfile

st.set_page_config(page_title="Mashao Mask Real-time Emotion Detection", layout="wide")

st.title("🎭 Mashao Mask Real-time Emotion Detection")
st.sidebar.write("📷 Please turn on the camera. The system will automatically detect your emotions and generate a Mashao mask.")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@st.cache_resource
def load_sd_pipeline():
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32
        ).to(device)
        return pipe
    except:
        return StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
        ).to(device)

pipe = load_sd_pipeline()

emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
emotion_model = models.resnet18(weights=None)
emotion_model.fc = torch.nn.Linear(emotion_model.fc.in_features, len(emotion_labels))
emotion_model.load_state_dict(
    torch.load(r"C:\Users\24012749\Desktop\AI-4-Media-Project-Yuxin_Chen-24012749-main\emotion_model.pth", 
               map_location=device, 
               weights_only=True)
)

emotion_model.to(device)
emotion_model.eval()

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def predict_emotion(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = emotion_model(image)
        _, predicted = torch.max(outputs, 1)
        return emotion_labels[predicted.item()]

def generate_face_mask(emotion):
    prompts = {
        'Happiness': 'A traditional Chinese Mashao mask with joyful and vibrant colors, highly detailed, no background.',
        'Surprise': 'A Mashao mask expressing surprise, bright colors, exaggerated facial expressions, no background.',
        'Fear': 'A Mashao mask depicting fear, dark tones with sharp and intense strokes, no background.',
        'Disgust': 'A Mashao mask showing disgust, contrasting colors with distorted facial expressions, no background.',
        'Neutral': 'A balanced and traditional Mashao mask with neutral emotions, subtle yet powerful, no background.',
        'Anger': 'A Mashao mask representing anger, strong red and black tones with bold strokes, no background.',
        'Sadness': 'A Mashao mask expressing sadness, soft blue tones and gentle curves, no background.'
    }

    prompt = prompts.get(emotion, "A traditional Chinese Mashao mask with intricate design, no background.")
    generated_image = pipe(prompt).images[0]

    generated_image = generated_image.convert("RGBA")
    width, height = generated_image.size


    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((10, 10, width - 10, height - 10), fill=255)


    result = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    result.paste(generated_image, (0, 0), mask)

    return result


cap = cv2.VideoCapture(0)

frame_placeholder = st.empty()
emotion_placeholder = st.sidebar.empty()
last_emotion = None
face_mask = None

st.sidebar.write("🔴 Press `q` to exit")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    emotion = predict_emotion(frame)
    if emotion != last_emotion:
        face_mask = generate_face_mask(emotion)
        last_emotion = emotion
        emotion_placeholder.write(f"**Detected Emotion: {emotion}**")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if face_mask is not None:
        for (x, y, w, h) in faces:
            face_mask_resized = face_mask.resize((w, h), Image.LANCZOS)
            face_mask_resized = np.array(face_mask_resized)

        
            overlay = frame.copy()
            alpha_mask = face_mask_resized[:, :, 3] / 255.0
            for c in range(3):
                overlay[y:y+h, x:x+w, c] = (1 - alpha_mask) * frame[y:y+h, x:x+w, c] + alpha_mask * face_mask_resized[:, :, c]
            frame = overlay


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels="RGB", use_column_width=True)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
