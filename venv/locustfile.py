# -*- coding: utf-8 -*-

from cases.base import *
from locust import Locust, TaskSet, task
from cases.TaskPageApi import *
from cases.PlanPageApi import *


class SFExpressTest(TaskSet):

    # task page API
    @task
    def createTask(self):
        TaskPageApi(self.client).createTask()

    @task
    def taskCreatorAll(self):
        TaskPageApi(self.client).taskCreatorAll()

    @task
    def taskReceiverAll(self):
        TaskPageApi(self.client).taskReceiverAll()

    # plan page API
    @task
    def createPlan(self):
        PlanPageApi(self.client).createPlan()


class WebsiteUser(Locust):
    task_set = SFExpressTest
    min_wait = 5000
    max_wait = 15000
    host = "http://localhost:8080/pmp"