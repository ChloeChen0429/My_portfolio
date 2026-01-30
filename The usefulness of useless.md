# The Usefulness of the Useless

A Study of Incomplete or Abandoned Property Developments in London


<img width="1160" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/598e5e69-4e1c-4280-bc26-ca36fd230197">


By reimagining and virtually activating the incomplete buildings on the outskirts of London, we explore how these contemporary ruins, after the collapse of utopian ideals, carry the spiritual value of Zhuangzi's "the usefulness of the useless" and humanity's renewed perception of space, time, and memory.

---

|Team member|Discussion & Research|Concept|Field research|Shooting|3D Model & Printing|TD Interaction & Vision|Video Editing|TD technical support|GitHub Writing|
| :---          | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| Manyi Lin     |✅|🩷|✅|✅|🩷|🩷|✅|🩷|🩷| 
| Yuxin Chen    |✅|✅|✅|🩷|🩷|✅|🩷|✅|🩷| 
| Zenghou Luan  |✅|🩷|✅|🩷|✅|🩷|🩷|🩷|✅|

---

TD Files: 

[interaction control](https://drive.google.com/file/d/1diTfe-FsJYwT39xE8YubOE-qgt-sLypP/view?usp=sharing)

[background](https://drive.google.com/file/d/1diTfe-FsJYwT39xE8YubOE-qgt-sLypP/view?usp=sharing)

---

## Overview & Project Description

### Interaction & Rules:

* State 1: When there is no interaction, the projection will grow naturally on the model.

* State 2: When there is interaction, the webcam identifies the height of the hand position, the projection changes to a special state, and it undulates on the fountain according to the height of the gesture.

The system tracks the position of the audience's wrists through MediaPipe: the left hand controls the rotation of the tree, and the right hand controls its growth rate and scale. These real - time inputs are transmitted to the CHOP network (select, math, lag, merge) in TouchDesigner, and further act on the pointTransform SOP and the particle system, generating an evolving tree - like structure in space through instancing. This geometry is stored in the geo COMP, and after being rendered, it is directly projected onto the real - life fountain sculpture in the center of the installation through Kantan Mapper.
    
---

### Concepts and Goals: Contemporary Interpretation of Zhuangzi's Topology

London is a modern and prosperous city. However, on its outskirts, there are some "unfinished buildings" scattered around - these contemporary ruins are embedded in the urban fabric. These abandoned structures are not only the result of unbalanced urban development, but also reflect the projection and remains of past ideals.

We attempt to explore the time imprints and spiritual values carried by these failed ideal spaces, and ponder why these spaces that once promised publicity, futurism, and collective order are now regarded as "useless" physical relics.

![image](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/c3a9965d-719b-4b71-8aa7-1c0de8a8027e)

At the same time, we hope to introduce the Taoist philosophy of "the utility of the useless" by Zhuangzi. A building that is considered useless in terms of utility may have an irreplaceable significance in the spiritual and emotional aspects. It is precisely this kind of "uselessness" that escapes the fate of being "used" and "exploited", and is closer to a state of nature and autonomy.

<img width="1419" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/0ac78d44-8fa8-400a-be01-437c99a22e17">

By re - imagining and reconstructing these abandoned buildings, we aim to understand the spiritual value behind the "unfinished" and the collapse of collective memory and ideals reflected in the failure of utopian visions in architectural practices. Our exploration focuses on how the ideals carried by these ruins affect contemporary people's perception of space, time, and memory - and explores whether we can re - establish an emotional connection with idealism through these places regarded as useless. Based on the concept of "the utility of the useless is the greatest utility", we will activate these structures in a virtual environment to explore the historical and emotional significance they carry. 

---
## Supplies & Materials

### Components Used:  
- **projector**: 3D mapping in real time
- **webcam**: Capture gesture dynamics in real time
- **Blender**: Make ruins model
- **3D printing**: 3D print models
- **Touchdesigner**: Create 3D mapping interaction & visuals
---

## Process

### Field research

We selected the following locations and conducted Case studies

<img width="1066" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/a68529c3-bb07-426d-8d60-f7aaed5b87a6">

At the same time, we conducted on - site research.

<img width="1043" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/704b47d5-10ae-4a02-812e-b41ec2c7a854">

---

### Visual production

When we conducted on - site research, we collected relevant visual elements.

<img width="1029" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/ad8f5a81-f784-4867-9552-ce5f65eae351">

After that, a visual sketch was drawn

<img width="372" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/194ed31c-119a-40c5-baf2-fdff9172557c">

and conduct modeling in Blender

<img width="812" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/1a8d71db-f588-4311-958d-869568cab36a">

After that, we 3D printed the model.

<img width="1016" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/663c569e-ea2e-4270-b6f6-d7610bc7c1cd">

<img width="1395" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/d372407f-8079-414e-b4e4-62bf8c26d5ec">

---

### Touchdesigner & 3D Mapping Interaction

We designed the relevant visuals in TD and projected them for testing.

<img width="951" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/7769494b-924c-41c0-85b3-d0813b8b3659">

<img width="1062" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/e3148e2e-1373-4e38-9fe9-630d367e51b9">

---

### Touchdesigner gesture interaction construction

On a visual level, this tree is composed of glowing and expanding particles, accompanied by a breathing-like rhythm. The movement of the audience prompts its rotation and growth, symbolizing the reactivation of a dormant ideal in the presence of people - poetically presenting that when things break free from the shackles of utility, the so - called "uselessness" instead reveals a deeper value.

At the same time, a parallel image system continuously generates evolving textures resembling moss or mycelium. Starting from seed - like circular patterns and program noise, through repeated calculations in feedback loops (feedback, composite, edge, mirror, ramp), it forms a chaotic yet organic visual form. This image is projected onto the rough wall behind the fountain, as if digital spores are quietly spreading - evoking the biological processes of decay, growth, and ecological memory.

In terms of spatial composition, the tree on the fountain is at the center, symbolizing physical agency and the ideal of structuring; while the moss on the wall, as a non - linear memory structure, is connected to abandonment, deposition, and the silent tenacity of nature. Through Kantan Mapper, the visual effects and physical textures are seamlessly integrated, gradually blurring the boundary between the digital and the physical.


<img width="1885" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/0e73c28b-64c0-49db-966b-e7df70810d6f">

<img width="1571" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/9aa88b2d-0c80-4c2c-9fb5-6c459f764547">


This system is not merely a technological marvel. It reactivates the forgotten architectural remnants through human interaction, transforming the audience from controllers into co - existers and witnesses. It reawakens the "useless" spaces, echoing what Zhuangzi said: true value often reveals itself when divorced from direct utility.

On a philosophical level, this project also corresponds to the "hauntology" theory proposed by Mark Fisher in *The Ghosts of My Life* - forgotten dreams and lost futures haunt the present like ghosts. Here, the projected ruins become the living remnants of a failed utopia - the ghosts of past ideals - inviting the audience to inhabit the liminal zone where memory, failure, and the possibility of re - imagination intersect. 

---

## Video Demonstration

https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/c41a0000-45d8-4c20-a848-7f3e63e154ae

---

## Final Images
<img width="1640" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/4a48fc10-cc28-4ae6-bbfe-a697b72bff12">

<img width="1755" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/950f29ed-4369-4cad-ad3c-2704384c1679">

---

## Design Justification 
<img width="743" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/c449fc1c-0ccc-439e-9369-60a02c916d98">

---

## 🧪 User Testing Summary (5 Participants)

**1. Emily Zhang** 

* Appreciated the philosophical framing of space and ruin.
* Suggested adding more historical background of the chosen buildings.
* Thought explanatory texts or audio narration could help deepen audience engagement.

**2. Lucas Kim** 

* Found the interaction effects visually impressive but experienced some lag.
* Reported instability in gesture recognition under low or flickering lighting.
* Recommended clearer gesture guidance at the installation site.

**3. Sophie Miller

* Was visually attracted to the projection and sculpture.
* Didn’t immediately understand how to interact with the system.
* Suggested adding audio or visual cues to indicate interaction feedback.

**4. Dr. Michael Rhodes

* Praised the philosophical depth and visual language.
* Questioned whether the “usefulness of the useless” idea was clearly communicated to all viewers.
* Recommended providing QR codes or digital links to contextual resources for further reading.

**5. Anna Laurent

* Saw strong exhibition potential in the installation.
* Suggested improving technical reliability for public settings.
* Encouraged exploring multi-user interaction to reflect shared temporal/spatial experience.

---

## 🔧 Revision Plan 

Based on user testing, we identified areas for improvement in interaction stability, audience guidance, and narrative depth. Technically, we plan to enhance the robustness of gesture recognition by integrating dual-camera or depth-sensing systems to better adapt to inconsistent lighting environments. To improve user experience, we will add clear gesture instructions near the installation and incorporate real-time visual and audio feedback to signal successful interactions. Conceptually, we aim to deepen the historical and emotional context by embedding more site-specific narratives — such as archival images or stories — through projected text or accessible QR code links. This will help ground the audience’s experience in the socio-economic reality behind the ruins. Additionally, we will explore the implementation of multi-user input to allow for collaborative interaction, fostering a stronger sense of shared presence and temporal layering. This shift aligns more closely with Zhuangzi’s idea of open-ended perception and collective engagement with space. Through these revisions, we hope to enhance both the technical clarity and philosophical resonance of the project, making the “useless” more visibly meaningful.

