# Imports 
from ai_engine import prompt_openAI
from mock import misty_robot, get_sentiment, emote_behavior
import os 
import time

### EXPERIMENTAL RUN --------------------------------------------- 
def experimental_run():
    # Robot Intro 
    robot_intro = "Hi, I am Misty. I’m an experimental robot trying to learn more about humans and their daily activities. Tell me about something that’s been bothering you lately."
    print("\nMisty:", robot_intro)
    misty_robot.text_to_speech(robot_intro)

    # Set up Chat History 
    chat_history = [{"role": "system", f"content": {robot_intro}}]

    # Start Convo
    for i in range(4):
        # Get User Input
        user_input = input("\nParticipant: ")
                        
        # Get User Sentiment
        sentiment = get_sentiment(user_input)

        # Get OpenAI Response
        response_type = "end" if i==3 else "follow_up"
        openai_response, chat_history = prompt_openAI(user_input,
                                            response_type=response_type,
                                            sentiment=sentiment,
                                            chat_history=chat_history
                                        )

        # Robot Response
        emote_behavior(sentiment)
        print("\nMisty:", openai_response)
        misty_robot.text_to_speech(openai_response)

### CONTROL RUN --------------------------------------------- 
def control_run():
    # Robot Intro 
    robot_intro = "Hi, I am Misty. I’m an experimental robot trying to learn more about humans and their daily activities. Tell me about something that’s been bothering you lately."
    print("\nMisty:", robot_intro)
    misty_robot.text_to_speech(robot_intro)

    # Set up Chat History 
    chat_history = [{"role": "system", f"content": {robot_intro}}]

    # Start Convo
    for i in range(4):
        # Get User Input
        user_input = input("\nParticipant: ")

        # Get OpenAI Response
        response_type = "end" if i==3 else "follow_up"
        openai_response, chat_history = prompt_openAI(user_input,
                                            response_type=response_type,
                                            sentiment=None,
                                            chat_history=chat_history
                                        )

        # Robot Response
        emote_behavior(None)
        print("\nMisty:", openai_response)
        misty_robot.text_to_speech(openai_response)

### DRIVER --------------------------------------------- 
if __name__ == "__main__":
    # Clear Console 
    os.system("clear")
    time.sleep(1)

    # Experimental Run 
    experimental_run() 

    # Intermission 
    time.sleep(1)
    print("\n \n \n")
    print("-------------------------\n")
    input("Press Enter to proceed to the next portion of this interaction.")  
    os.system("clear")

    # Control Run 
    control_run() 

    # End Interaction 
    time.sleep(1)
    print("\n \n \n")
    print("-------------------------\n")
    input("Press Enter to end this interaction.")
    os.system("clear")

    print(" \n \n \n")
    print("-------------------------\n")
    print("The interaction is now over.")
    print("Thanks for taking the time - please fill out the survey before leaving :)")
    
      

