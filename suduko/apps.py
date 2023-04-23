
from django.apps import AppConfig
import numpy as np
import os

boards = []

def setup_ques(name):
    global boards
  
    quizzes = np.zeros((1000000, 81), np.int32)
    
    for i, line in enumerate(open(f'./{name}/../sudoku.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            

    boards = quizzes.reshape((-1, 9, 9))

class SudukoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suduko'

    def ready(self) -> None:
        if os.environ.get('RUN_MAIN'):setup_ques(self.name)
