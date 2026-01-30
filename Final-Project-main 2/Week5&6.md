During Weeks 5 and 6, I reviewed the results of my previous experiments on upper-limb emotion recognition and realised several fundamental limitations. Although I initially attempted to classify emotions using YOLOv8-Pose on crowd videos, the detection accuracy of upper-limb gestures proved unreliable. Variations in lighting, frequent occlusions, and rapid movements made the extracted keypoints unstable. More importantly, in club environments, most audience members display consistently high-arousal behaviours—raising arms, dancing vigorously—resulting in very low emotional differentiation. This made it extremely difficult to build a meaningful emotion classifier based on upper-limb movement alone.

At the same time, I compared MediaPipe Pose with YOLOv8-Pose. MediaPipe only supports single-person pose estimation and showed unstable behaviour under complex lighting. YOLOv8-Pose, on the other hand, offered stronger robustness, multi-person tracking, and more stable keypoints in noisy scenes, which confirmed that my earlier choice of YOLOv8-Pose was the right direction. However, even with YOLOv8-Pose, upper-limb cues still lacked emotional granularity for club settings.

These findings led me to shift towards single-person facial emotion recognition, for two main reasons:

the performer acts as the emotional source in a live performance;

facial expression provides stronger controllability and clearer emotional distinctions than audience body movements.

To build a reliable facial emotion model, I evaluated different classification architectures. I compared ResNet18 and YOLOv8-Cls, and found that YOLOv8 offered:

faster inference suitable for real-time performance,

better robustness to low-quality or blurred inputs,

an integrated pipeline consistent with my later multi-module setup.

Based on this assessment, I chose YOLOv8-Cls as the final model architecture.

I then prepared the FER2013 dataset for fine-tuning. Since the original dataset contains clean, front-facing faces unsuitable for dynamic lighting environments, I adapted it to the YOLOv8 format and applied augmentation strategies such as Gaussian blur, noise injection, brightness variation, and contrast shifts to simulate club-like conditions. These augmentations aimed to improve robustness and ensure the model could handle real-time webcam inputs during live performance.

<img width="320" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/d241cf6d-79ea-4f72-bda5-65cf96d8bfb0" />

