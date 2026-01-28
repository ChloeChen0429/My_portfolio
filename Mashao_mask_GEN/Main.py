import os
import cv2
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
from torchvision import transforms, models
from diffusers import StableDiffusionPipeline
from safetensors.torch import load_file


mashao_model_path = "C:/Users/24012749/Desktop/AI-4-Media-Project-Yuxin_Chen-24012749-main/mashao-lianpu-model"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

try:
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32).to(device)
    print("✅ 成功加载自定义 Stable Diffusion 马勺脸谱模型！")
except:
    print("⚠️ 载入自定义模型失败，使用默认 Stable Diffusion v1.5")
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to(device)


emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
emotion_model = models.resnet18(weights=None)
emotion_model.fc = nn.Linear(emotion_model.fc.in_features, len(emotion_labels))
emotion_model.load_state_dict(torch.load("emotion_model.pth", map_location=device))
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
    datas = generated_image.getdata()
    new_data = []
    for item in datas:
        if item[:3] == (255, 255, 255):  
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    generated_image.putdata(new_data)

    return generated_image


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

frame_count = 0
face_mask = None
last_emotion = None  # 记录

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    if frame_count % 5 == 0: 
        emotion = predict_emotion(frame)

        if emotion != last_emotion:
            print(f"🔍 Detected emotion: {emotion}")
            face_mask = generate_face_mask(emotion)  # 生成新脸谱
            last_emotion = emotion

    if face_mask is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face_mask_resized = face_mask.resize((w, h), Image.LANCZOS)  # 调整大小
            face_mask_resized = np.array(face_mask_resized)

            overlay = np.zeros_like(frame, dtype=np.uint8)
            alpha_mask = face_mask_resized[:, :, 3] / 255.0  
            for c in range(3):
                overlay[y:y+h, x:x+w, c] = (1 - alpha_mask) * frame[y:y+h, x:x+w, c] + alpha_mask * face_mask_resized[:, :, c]

            frame[y:y+h, x:x+w] = overlay[y:y+h, x:x+w]  

    cv2.putText(frame, f"Emotion: {last_emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Mashao Emotion and Face Mask Analysis', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
