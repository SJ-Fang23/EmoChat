# Mock Functions - for testing driver code
import random
import openai

# Set up: OpenAI API key
api_key = "DUMMY KEY"  # Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = api_key

def _chatgpt_interface(chat_history):
    response = openai.ChatCompletion.create( 
                        model = "gpt-3.5-turbo",  # or another GPT-3 model you prefer
                        messages = chat_history,
                        temperature = 0.7, 
                        max_tokens = 150
                    )
        
    # Return AI's response
    return response['choices'][0]['message']['content']

def prompt_openAI(user_input, response_type="follow_up", sentiment="N/A", chat_history=[]): 
    # Engineer the Prompt
    message = ""
    if response_type == "follow_up":
        message = {"role": "user", "content": f"[sentiment: {sentiment}, and ask follow up question]: {user_input}"}
    else:
        message = {"role": "user", "content": f"[sentiment: {sentiment}, and end the conversation]: {user_input}"}
    chat_history.append(message)
    
    # Get Chat GPT Response + Update Chat History 
    response = _chatgpt_interface(chat_history)
    chat_history.append({"role": "system", f"content": response})

    return response, chat_history