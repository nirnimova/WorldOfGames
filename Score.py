from Utils import SCORES_FILE_NAME
import os


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    scores_file = open(SCORES_FILE_NAME, mode='a', encoding='utf-8')

    current_score = 0
    if os.stat(SCORES_FILE_NAME).st_size > 0:
        scores_file = open(SCORES_FILE_NAME, mode='r', encoding='utf-8')
        current_score = int(scores_file.readline())

    scores_file = open(SCORES_FILE_NAME, mode='w', encoding='utf-8')

    current_score = current_score + points_of_winning

    scores_file.write(str(current_score))