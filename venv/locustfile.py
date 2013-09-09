# -*- coding: utf-8 -*-

import json
from locust import Locust, TaskSet, task

class SFExpressTest(TaskSet):

    @task
    class TaskPageApi(TaskSet):

        @task
        def createTask(self):
            self.client.post("/rest/task/new", json.dumps({
                "fiveElementName": "1.1.1招（含晋升）",
                "name": "smoke test for shunfeng express",
                "description": "smoke test",
                "receivers": ["000002"],
                "startDate": "2013-09-09",
                "reviewDate": "2013-09-12",
                "endDate": "2013-09-19"
            }),headers={"Content-type":"application/json"})

    @task
    class PlanPageApi(TaskSet):

        @task
        def createPlan(self):
            self.client.post("/rest/plan/new", json.dumps({
                "comments": "We need make sure this api works fine",
                "description": "We need make sure this api works fine",
                "fiveElement": "1.1.1招（含晋升）",
                "followLevel": "DIVISION",
                "initiator": "000001",
                "name": "smoke test for create plan",
                "owner": "000002",
                "steps":[{
                       "description": "Step 1",
                       "departmentIds": [1],
                       "comments": "This is created by smoke test",
                       "startDate": "2013-09-10",
                       "endDate": "2013-10-30"
                    }
                ]
            }),headers={"Content-type":"application/json"})


class WebsiteUser(Locust):
    task_set = SFExpressTest
    min_wait = 5000
    max_wait = 15000
    host = "http://localhost:8080/pmp"