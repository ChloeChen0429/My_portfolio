# The Usefulness of the Useless

A Study of Incomplete or Abandoned Property Developments in London


[<img width="1160" alt="image" src="https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/598e5e69-4e1c-4280-bc26-ca36fd230197">
](https://git.arts.ac.uk/24005203/Responsive-Environments-Blog-2024/assets/1175/598e5e69-4e1c-4280-bc26-ca36fd230197)

By reimagining and virtually activating the incomplete buildings on the outskirts of London, we explore how these contemporary ruins, after the collapse of utopian ideals, carry the spiritual value of Zhuangzi's "the usefulness of the useless" and humanity's renewed perception of space, time, and memory.

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

<img width="3300" height="2550" alt="image" src="https://github.com/user-attachments/assets/40cab8f9-d461-4d0c-ba61-1602902193d8" />


At the same time, we hope to introduce the Taoist philosophy of "the utility of the useless" by Zhuangzi. A building that is considered useless in terms of utility may have an irreplaceable significance in the spiritual and emotional aspects. It is precisely this kind of "uselessness" that escapes the fate of being "used" and "exploited", and is closer to a state of nature and autonomy.

<img width="2838" height="1284" alt="image" src="https://github.com/user-attachments/assets/ae592259-9bcf-4540-9569-399835672481" />


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

<img width="2132" height="978" alt="image" src="https://github.com/user-attachments/assets/b76c407c-a6b5-482a-adb8-79946494ab8e" />


At the same time, we conducted on - site research.

<img width="2086" height="1096" alt="image" src="https://github.com/user-attachments/assets/51592a97-4107-485c-8878-08b5c863c6df" />

---

### Visual production

When we conducted on - site research, we collected relevant visual elements.

<img width="2058" height="1128" alt="image" src="https://github.com/user-attachments/assets/1786bcdb-b475-4875-a1b0-bbbeca34ae95" />

After that, a visual sketch was drawn

<img width="744" height="494" alt="image" src="https://github.com/user-attachments/assets/8a280438-888e-4532-aa4d-f8c443c8d6f5" />

and conduct modeling in Blender

<img width="1624" height="848" alt="image" src="https://github.com/user-attachments/assets/41148a37-04e4-447e-9e1c-b351633ac348" />

After that, we 3D printed the model.

<img width="2032" height="882" alt="image" src="https://github.com/user-attachments/assets/400f32ff-9cd8-4a02-8750-8d1d3a013b38" />

<img width="2790" height="1040" alt="image" src="https://github.com/user-attachments/assets/589644dd-25ef-4684-a516-e6a052325d56" />

---

### Touchdesigner & 3D Mapping Interaction

We designed the relevant visuals in TD and projected them for testing.

<img width="1902" height="986" alt="image" src="https://github.com/user-attachments/assets/291784b0-2eb3-4641-9350-636d7b6e3dee" />

<img width="2124" height="878" alt="image" src="https://github.com/user-attachments/assets/5baf56d7-45d4-4160-aead-6d550ff863e0" />


---

### Touchdesigner gesture interaction construction

On a visual level, this tree is composed of glowing and expanding particles, accompanied by a breathing-like rhythm. The movement of the audience prompts its rotation and growth, symbolizing the reactivation of a dormant ideal in the presence of people - poetically presenting that when things break free from the shackles of utility, the so - called "uselessness" instead reveals a deeper value.

At the same time, a parallel image system continuously generates evolving textures resembling moss or mycelium. Starting from seed - like circular patterns and program noise, through repeated calculations in feedback loops (feedback, composite, edge, mirror, ramp), it forms a chaotic yet organic visual form. This image is projected onto the rough wall behind the fountain, as if digital spores are quietly spreading - evoking the biological processes of decay, growth, and ecological memory.

In terms of spatial composition, the tree on the fountain is at the center, symbolizing physical agency and the ideal of structuring; while the moss on the wall, as a non - linear memory structure, is connected to abandonment, deposition, and the silent tenacity of nature. Through Kantan Mapper, the visual effects and physical textures are seamlessly integrated, gradually blurring the boundary between the digital and the physical.


<img width="3770" height="1786" alt="image" src="https://github.com/user-attachments/assets/266e7357-dd5c-442d-aa65-d611c7d47520" />


<img width="3142" height="1776" alt="image" src="https://github.com/user-attachments/assets/ef72452c-948e-4af6-aeb9-b6a9eff93bbe" />



This system is not merely a technological marvel. It reactivates the forgotten architectural remnants through human interaction, transforming the audience from controllers into co - existers and witnesses. It reawakens the "useless" spaces, echoing what Zhuangzi said: true value often reveals itself when divorced from direct utility.

On a philosophical level, this project also corresponds to the "hauntology" theory proposed by Mark Fisher in *The Ghosts of My Life* - forgotten dreams and lost futures haunt the present like ghosts. Here, the projected ruins become the living remnants of a failed utopia - the ghosts of past ideals - inviting the audience to inhabit the liminal zone where memory, failure, and the possibility of re - imagination intersect. 

---

## Video Demonstration

https://github.com/user-attachments/assets/dc374a04-e28b-4cad-83e4-93c4032955f5


---

## Final Images
<img width="3280" height="698" alt="image" src="https://github.com/user-attachments/assets/c2a49303-d8e1-4222-8eee-091c98382b1a" />

<img width="3510" height="730" alt="image" src="https://github.com/user-attachments/assets/607619e8-c11e-4ac2-81b6-920d6249f306" />


---

## Design Justification 
<img width="1486" height="916" alt="image" src="https://github.com/user-attachments/assets/1f19d08b-d458-40fc-8ac2-3a331413e81f" />


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

