import logging

logger = logging.getLogger(__name__)

def calculate_score(responses, correct_answers):
    correct = 0
    for response, correct_answer in zip(responses, correct_answers):
        logger.debug({'response': response, 'correct_answer': correct_answer})
        if response == correct_answer:
            correct += 1
    return correct / len(responses)
