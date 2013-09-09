# -*- coding: utf-8 -*-

from cases.base import *
from locust import Locust, TaskSet, task
from cases.TaskPageApi import *
from cases.PlanPageApi import *


class SFExpressTest(TaskSet):

    # task page API
    def on_start(self):
        self.task_page_api = TaskPageApi(self.client)
        self.plan_page_api = PlanPageApi(self.client)

    @task
    def createTask(self):
        self.task_page_api.create_task()

    @task
    def taskCreatorAll(self):
        self.task_page_api.task_creator_all()

    @task
    def taskReceiverAll(self):
        self.task_page_api.task_receiver_all()

    # plan page API
    @task
    def createPlan(self):
        self.plan_page_api.create_plan()





class WebsiteUser(Locust):
    task_set = SFExpressTest
    min_wait = 5000
    max_wait = 15000
    host = "http://localhost:8080/pmp"