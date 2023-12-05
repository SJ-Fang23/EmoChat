import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from transformers import pipeline

def get_emotion(input_text):

    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

    sentences = [input_text] if input_text is not None else ["I'm having a great day!"]

    model_outputs = classifier(sentences)

    return model_outputs[0][0]["label"]
