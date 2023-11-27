# Imports 
from mock import misty_robot, get_sentiment, prompt_openAI, emote_behavior
import os 
import time

# Clear Console 
os.system("clear")
time.sleep(1)

# Robot Intro 
robot_intro = "Hi, I am Misty. I’m an experimental robot trying to learn more about humans and their daily activities. Tell me about something that’s been bothering you lately."
print("\nMisty:", robot_intro)
misty_robot.text_to_speech(robot_intro)

# Start Convo
for i in range(4):
    # Get User Input
    user_input = input("\nParticipant: ")
                       
    # Get User Sentiment
    sentiment = get_sentiment(user_input)

    # Get OpenAI Response
    response_type = "end" if i==3 else "follow_up"

    openai_response = prompt_openAI(user_input,
                        response_type=response_type,
                        sentiment=sentiment
                        )

    # Robot Response
    emote_behavior(sentiment)
    print("\nMisty:", openai_response)
    misty_robot.text_to_speech(openai_response)