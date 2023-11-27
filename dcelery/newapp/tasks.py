from celery import shared_task
import time

@shared_task
def sharedtask():
    return


class PeriodicTaskController:
    def __init__(self):
        self.running = False
        self.task_instance = None

    def start_task(self):
        if not self.running:
            self.running = True
            self.task_instance = periodic_task.apply_async()
            return "Periodic task started."
        return "Periodic task is already running."

    def stop_task(self):
        if self.running:
            self.running = False
            if self.task_instance:
                self.task_instance.revoke()
                self.task_instance = None
            return "Periodic task stopped."
        return "No periodic task is running."

controller = PeriodicTaskController()

@shared_task
def periodic_task():
    while controller.running:
        print("Working")
        time.sleep(20)

@shared_task
def start_periodic_task():
    return controller.start_task()

@shared_task
def stop_periodic_task():
    return controller.stop_task()