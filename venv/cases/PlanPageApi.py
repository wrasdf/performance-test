# -*- coding: utf-8 -*-

import json
from locust import Locust, TaskSet, task

class PlanPageApi(TaskSet):

    def on_start(self):
        self.client.get("/pages/plan/index.htm")

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

