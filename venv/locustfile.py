# -*- coding: utf-8 -*-

from cases.base import *
from locust import Locust, TaskSet, task
from cases.TaskPageApi import *
from cases.PlanPageApi import *


# task page API
class TaskPageTest(TaskSet):

    def on_start(self):
        self.base = Base(self.client)
        self.task_page_api = TaskPageApi(self.client)

    @task(10)
    def createTask(self):
        self.task_page_api.create_task()

    @task
    def taskCreatorAll(self):
        self.task_page_api.task_creator_all()

    @task
    def taskReceiverAll(self):
        self.task_page_api.task_receiver_all()

    @task
    def taskCreatorRejected(self):
        self.base.get('/rest/task/creator/rejected/1/createdDate/desc')

    @task
    def taskCreatorUnAccepted(self):
        self.base.get('/rest/task/creator/unaccepted/1/createdDate/desc')


    @task
    def stop(self):
        self.interrupt()

# plan page API
class PlanPageTest(TaskSet):

    def on_start(self):
        self.base = Base(self.client)
        self.plan_page_api = PlanPageApi(self.client)

    @task
    def createPlan(self):
        self.plan_page_api.create_plan()

    @task
    def stop(self):
        self.interrupt()


class SFExpressTest(TaskSet):
    tasks = {TaskPageTest:5, PlanPageTest:1}

class WebsiteUser(Locust):
    task_set = SFExpressTest
    min_wait = 200
    max_wait = 500
    host = "http://localhost:8080/pmp"
    stop_timeout = 5*60*1000