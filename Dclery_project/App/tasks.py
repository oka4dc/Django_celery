# app/tasks.py
from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    sleep(5)  # simulate a time-consuming task
    return x + y
