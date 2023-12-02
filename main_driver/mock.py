# Mock Functions - for testing driver code
import random
import time

# Misty Robot
class misty_robot:
    def text_to_speech(text):
        return 

# Predefined Functions 
def get_sentiment(user_input):
    return random.choice(["positive", "negative", "neutral"])

def prompt_openAI(*args, **kwargs): 
    time.sleep(0.75)
    if kwargs["response_type"] == "follow_up":
        return ("<dummy open ai response>. Tell me more about this.", None)
    else: 
        return ("<dummy open ai response>. Well thanks for talking to me today - it was nice to meet you! goodbye :)", None)

def emote_behavior(sentiment): 
    return 