# utils.py
import os
from openai import OpenAI

def generate_answer(question, image_path=None):
    answer = (
        "This is a mock answer because the OpenAI API quota is exhausted. "
        "Please replace this logic with real OpenAI API calls when your quota is restored."
    )

    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
            "text": "Use the model that’s mentioned in the question."
        },
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
            "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
        }
    ]

    return answer, links
