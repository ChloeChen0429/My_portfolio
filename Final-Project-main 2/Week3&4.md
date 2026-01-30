During Weeks 3 and 4, I began building the first version of my upper-limb emotion analysis pipeline. After discussing with my tutor, I re-evaluated the pose-estimation tools I had planned to use. Initially, I considered MediaPipe Pose, but after testing it with crowd-based dance-floor videos, I found several limitations: it only supports single-person tracking, struggles with occlusion and club-like lighting, and is not reliable when multiple upper bodies appear in the frame. These issues made it unsuitable for later emotion aggregation and arousal–valence mapping.

Because of this, I switched to YOLOv8-Pose, which provides reliable multi-person pose estimation, stronger robustness in real-world videos, and stable tracking of upper-limb and head movements. This better aligns with my later goal of mapping gesture dynamics into Russell’s arousal–valence model.

With YOLOv8-Pose identified as the core detector, I started building my own training pipeline. Following the workflow in my slides, I developed a two-stage system:

### Dataset construction

I crawled YouTube videos using keywords such as “people dancing in clubs” and “techno rave.”

I applied quality filtering based on duration, resolution, and metadata.

After cleaning, I obtained a curated dataset of upper-body movement videos (89 valid files out of ~480 downloaded) 

These videos became the foundation for gesture-based emotion modelling.

<img width="1177" alt="截屏2025-11-24 17 46 32" src="https://git.arts.ac.uk/user-attachments/assets/249eb607-5a36-46a6-843f-5ef1eaf816e1" />

### Auto-training pipeline

I extracted pose keypoints for each video window using YOLOv8-Pose.

I aggregated all windows into a structured CSV dataset.

I applied unsupervised clustering to discover latent upper-limb motion patterns.

Each cluster’s mean arousal/valence value was mapped into one of the eight sectors of Russell’s circumplex model (excited, happy, calm, relaxed, bored, sad, angry, tense) 

Finally, I saved the trained pipeline (cluster centers + preprocessing steps) as a reusable model for real-time prediction.

This was my first complete attempt at “emotion from movement” without using FER2013 or facial expression data. Through this process, I learned why I needed a custom upper-limb model, why existing emotion models could not be used directly, and how unsupervised learning can transform raw movement data into continuous emotional states.

<img width="917" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/68e57be2-27d4-4a49-8380-e49fd7c14638" />

<img width="916" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/9ae3bc33-4526-48a1-9450-ba4d790deb87" />

<img width="917" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/ae911206-c691-4ab6-8039-aa54788411e0" />

<img width="918" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/33d33663-3e3d-47e8-9996-fdc62ebceb28" />

<img width="919" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/153130ba-0f49-4211-b3cc-8936c86b3761" />

<img width="919" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/184679fa-cab6-4c3a-a61d-845627831bdf" />








