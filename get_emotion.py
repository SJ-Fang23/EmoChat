from transformers import pipeline
import sys

input = sys.argv[1]

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

sentences = [input] if input is not None else ["I'm having a great day!"]

model_outputs = classifier(sentences)

print(model_outputs[0][0]["label"])
