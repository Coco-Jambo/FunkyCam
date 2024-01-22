# FunkyCam
FunkyCam

## Prerequisites 
I need to figure out how to make these libraries independant from the user, they should be installed with the app
<br>
``pip install opencv-python``
## What is this about?
As an artist, I decided to stay anonymous and cover my face like Daft Punk. Editing takes a lot of time, so I got inspired from instagram filters to try and recreate that tracking technology on Python, so that it automatically puts your brand face on yours. In myc ase it is a star, and for Marshmallow for example, well it is a marshmallow. The app will detect the different expressions of your face and put the right image for it. For example, if I smile it will put the image of the star that is smiling. It is early in developement as I am currently learning how to use the OpenCV library, which is pretty dense. 
## Challenges

These are some of the challenges I am facacing right now, I will update this document whenever I digure out a solution to them and mark them as fixed

- I knew nothing about image procesing going in, I am learning how to use the opencv library and documenting what I learn as I am going through it. I am continuously learning about it online and it is very interesting!
- Documentation takes some time but it is worth it so that it is easy to go back to and saves more time since I won't need to relearn the code I wrote
- I'm still looking at how to put an image on the screen using opencv, right now it draws a rectangle, but I want to remove it and have an image instead
- Making the image scale and tilt with head movements
- Detecting my face in low lighting
- Detecting my face when it moves fast
- Making the image not dissapear whenever the program doesn't detect the face for a few frames
- The app doesn't want to close when I press the X button on the top right of the window
## Future steps
- For now I imagine the app to work with images, maybe having a 3D model would be a great idea, sort of like VTubers but with just the head
- Integration with the android camera app
- A website to showcase the app
- Making the UI
- Making it usable by other people too, right now I am using it with the Funky Jambo faces, but I want to make it so that it's easy for other artists to upload their own images for different expressions
