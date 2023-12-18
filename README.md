# Emochat
To Run Experiment, go into main_driver folder and run $python main.py 

Within main_driver folder
------------------------

### Primary Code for AI
- main.py contains code for driving experimental runs 
- ai_engine.py contains code for AI prompting, interfacing with Chat GPT for responses, and all related parsing for requests and responses 
- emote_behavior.py contains code for calling Misty's API to perform robotic actions chosen by AI agent 
- get_emotion.py contains RoBERTa based model for classifying emotion of user's input (1 of 28 unique emotions returned)

### Robotic Code
- text_to_speech.py contains code for Misty to verbalize AI agent's responses 
- Misty_actions.py and mistyPy_modified.py contains code to interface with Misty's API for performing robotic actions.


Authors: Jonathan Lai, Shijie Fang, Turner Hayes

