from locust import Locust, TaskSet, task
from cases.PlanPageApi import *
from cases.TaskPageApi import *

class SFExpressTest(TaskSet):

    def __init__(self):
        self.TaskPageApi = TaskPageApi
        self.PlanPageApi = PlanPageApi

    @task
    def new_task(self):
        self.TaskPageApi.createTask

    @task
    def new_plan(self):
        self.PlanPageApi.createPlan