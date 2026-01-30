# Training the Facial Emotion Model with Fine-tuned FER2013

During Weeks 7 and 8, I completed the training of my facial-emotion recognition model. After preparing the fine-tuned FER2013 dataset in the previous stage, I converted all images into the YOLO-friendly format and applied several augmentation strategies—including Gaussian blur, brightness reduction, and dark-spot simulation—to imitate the complex and unstable lighting conditions of live performance environments. This significantly improved the model’s robustness.

The final training set contained 114,836 images, and the validation set contained 28,709 images across seven emotion categories. I trained the model using YOLOv8-cls at an input resolution of 224×224, with a batch size of 64 for 120 epochs. The model achieved 98.8% Top-1 accuracy and 100% Top-5 accuracy on the validation set, which confirmed that YOLOv8 was better suited to my project than ResNet-18. In earlier comparisons, I found that YOLOv8 offered stronger generalisation, faster inference speed, and more stable performance under lighting variations—three requirements essential for a real-time audiovisual system.

In practical use, the model continuously monitors the performer’s facial expressions. Instead of taking every single frame independently, it calculates an averaged prediction within a short time window at the end of each musical section. This approach helps reduce recognition noise caused by subtle facial tremors or transient misclassifications, making the emotion output more stable for controlling music and visuals.

<img width="640" alt="image" src="https://git.arts.ac.uk/user-attachments/assets/02ea1321-7410-433e-8692-bc452ff57089" />
