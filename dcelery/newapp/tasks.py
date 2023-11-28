from celery import shared_task
import time

@shared_task
def sharedtask():
    return


@shared_task
def task_one():
    # Task one logic
    print("Task One executed")


@shared_task
def task_two():
    # Task two logic
    print("Task Two executed")

