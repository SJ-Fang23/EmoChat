"""
text to speech using huggingface transdormers
"""
from transformers import pipeline
from IPython.display import Audio
# pipe = pipeline("text-to-speech", model="suno/bark-small")
robot_intro = "Hi, I am Misty. I am an experimental robot trying to learn more about humans and their daily activities. Tell me about something that has been bothering you lately."
# output = pipe(robot_intro)
# print(output)
# Audio(output["audio"], rate=output["sampling_rate"])
Audio('Untitled.wav')