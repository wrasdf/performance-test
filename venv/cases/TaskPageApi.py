# -*- coding: utf-8 -*-

import json

class TaskPageApi(object):

    def __init__(self, webClient):
        self.client = webClient

    def create_task(self):
        self.client.post("/rest/task/new", json.dumps({
            "fiveElementName": "1.1.1招（含晋升）",
            "name": "smoke test for shunfeng express",
            "description": "smoke test",
            "receivers": ["000002"],
            "startDate": "2013-09-09",
            "reviewDate": "2013-09-12",
            "endDate": "2013-09-19"
        }), headers={"Content-type": "application/json"})

    def task_creator_all(self):
        self.client.get("/rest/task/creator/all/1/createdDate/desc")

    def task_receiver_all(self):
        self.client.get("/rest/task/receiver/all/1/createdDate/desc")
