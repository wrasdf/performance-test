# -*- coding: utf-8 -*-

import json
from locust import Locust, TaskSet, task


class TaskPageApi(TaskSet):

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