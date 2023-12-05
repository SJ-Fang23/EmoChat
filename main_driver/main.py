# Imports 
from ai_engine import prompt_openAI
# from mock import prompt_openAI
from mock import misty_robot, emote_behavior
import os 
import time
import sys

# Flushes System Input Buffer 
def flush_input():
    try:
        import msvcrt  # for Windows systems
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import termios  # for Linux/Mac systems
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

### TRIAL RUN CODE --------------------------------------------- 
def trial_run(run_type="experimental"): 
    # Robot Intro 
    robot_intro = "Hi, I am Misty. I’m an experimental robot trying to learn more about humans and their daily activities. Tell me about something that’s been bothering you lately."
    print("\nMisty:", robot_intro)
    misty_robot.text_to_speech(robot_intro)

    # Set up Chat History 
    chat_history = [{"role": "system", f"content": robot_intro}]

    # Start Convo
    for i in range(4):
        # Get User Input
        flush_input()
        user_input = input("\nParticipant: ")
                        
        # Get User Sentiment (unless control run)
        sentiment = "N/A" 
        if run_type == "experimental":
            sentiment = get_sentiment(user_input)

        # Get OpenAI Response
        response_type = "end" if i==3 else "follow_up"
        openai_response, chat_history = prompt_openAI(user_input,
                                            response_type=response_type,
                                            sentiment=sentiment,
                                            chat_history=chat_history
                                        )

        # Robot Response
        emote_behavior(openai_response)
        print("\nMisty:", openai_response)
        misty_robot.text_to_speech(openai_response)

### DRIVER --------------------------------------------- 
if __name__ == "__main__":
    # Clear Console 
    os.system("clear")
    time.sleep(1)

    # Experimental Run 
    trial_run("experimental")

    # Intermission 
    time.sleep(1)
    print("\n \n \n")
    print("The first interaction is done now")
    print("NOTE: Please fill out the survey before moving onto the next section.\n")
    time.sleep(2)
    print("-------------------------\n")
    flush_input()
    input("Press Enter to proceed to the next portion of this interaction once you have finished the survey ... ")  
    os.system("clear")
    time.sleep(1)

    # Control Run 
    trial_run("control") 

    # End Interaction 
    time.sleep(1)
    print("\n \n \n")
    print("-------------------------\n")
    flush_input()
    input("Press Enter to end this interaction ... ")
    os.system("clear")

    print(" \n \n \n")
    print("-------------------------\n")
    print("The interaction is now over.")
    print("Thanks for taking the time - please fill out the final survey before leaving :)\n")
    
      

