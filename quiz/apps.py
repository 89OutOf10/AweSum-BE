from django.apps import AppConfig
import html
import pathlib
import os

#from . import QuizGenerator

class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'

#퀴즈 생성 모델에 맞게 path 수정
#class WebappConfig(AppConfig):
#    name = 'quiz'
#    MODEL_PATH = Path("model")
#    BERT_PRETRAINED_PATH = Path("model/uncased_L-12_H-768_A-12/")
#    LABEL_PATH = Path("label/")
#    generator = QuizGenerator(model_path = MODEL_PATH/"multilabel-emotion-fastbert-basic.bin", 
#                                            pretrained_path = BERT_PRETRAINED_PATH, 
#                                            label_path = LABEL_PATH, multi_label=True) 