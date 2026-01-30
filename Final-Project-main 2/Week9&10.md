# Building the Berlin Underground Dataset & First Attempt at Music Generation

During Weeks 9 and 10, I shifted my focus from emotion modelling to the sound generation component of the project. I began by building my own loop dataset, named Berlin Underground, which contains twelve categories commonly used in techno production: bass loops, drum loops, kicks, pad loops, synth loops, claps, hats, percussion, rides, SFX, snares, and toms. This structure reflects the essential modular components of a typical techno track and allows flexible recombination during generation.

After organising the dataset, I conducted my first attempt at system-based music generation. At this stage, I did not introduce any emotion interaction; the goal was simply to test whether meaningful musical structure could emerge from loops alone. I analysed several basic audio descriptors—such as RMS, spectral centroid, and density—to help determine how loops could be layered or sequenced. I then experimented with arranging the loops into fixed short sections and stitching them together into a complete piece.

![image](https://git.arts.ac.uk/user-attachments/assets/ce616f82-5a30-4747-86bf-c3bd48af880a)

The result was a standalone techno track generated entirely from loop combinations. Although the structure was simple and transitions were not yet smooth, this experiment helped me understand how loop-based generation behaves and provided a foundation for later integrating emotional control into the music pipeline.



https://git.arts.ac.uk/user-attachments/assets/bc708c6e-2721-40b1-87c4-65adb7f594cf

