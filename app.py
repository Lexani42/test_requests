import requests
import time
from datetime import date


class Totango:
    def __init__(self, email: str, password: str):
        self.session = requests.Session()
        self.email = email
        self.password = password
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        }
        self.login()

    def login(self):
        data = {
            "j_username": self.email,
            "j_password": self.password,
            "_spring_security_remember_me": "false",
        }
        self.session.post(
            "https://app-test.totango.com/t01/ciklum-automation-demo-230/j_spring_security_check",
            data=data,
        )

    def create_touchpoint(
        self, account: str, subject: str, description: str,
    ):
        payload = {
            "account_id": account,
            "activity_type_id": "key_1526213231499",
            "content": description,
            "create_date": int(time.time()) * 1000,
            "origin": "UI",
            "participantList": [
                {
                    "email": "testing.user+230_usage@totango.com",
                    "label": "Usage Admin",
                    "type": "internal",
                    "userId": "testing.user+230_usage@totango.com",
                }
            ],
            "subject": subject,
            "touchpointType": "08317369-0154-404c-ad12-ca25c627d52e",
        }
        response = self.session.post(
            "https://app-test.totango.com/t01/ciklum-automation-demo-230/api/v3/touchpoints/",
            data=payload,
        )
        touchpoint_id = response.json()["note"]["id"]
        time.sleep(1)
        return self.check_if_touchpoingt_exist(touchpoint_id, account)

    def check_if_touchpoingt_exist(
        self, touchpoint_id: int, account: str,
    ):
        resp = self.session.get(
            f"https://app-test.totango.com/t01/ciklum-automation-demo-230/api/v2/events/?account_id={account}&include_formatting=true",
            headers=self.header,
        )
        try:
            return (
                i for i in resp.json() if i["type"] == "note" and int(i["note_content"]["note_id"]) == int(touchpoint_id)
            ).__next__()
        except StopIteration:
            return None

    def create_task(
        self,
        description: str,
        assignee: str,
        priority: int,
        title: str,
        account: str,
        to_date: date,
    ):
        payload = {
            "description": description,
            "assignee": assignee,
            "priority": priority,
            "activity_type_id": "key_1526213231499",
            "due_date": to_date,
            "title": title,
            "status": "open",
            "account_id": account,
        }
        resp = self.session.post(
            "https://app-test.totango.com/t01/ciklum-automation-demo-230/api/v3/tasks",
            data=payload,
            headers=self.header,
        )
        task_id = resp.json()["id"]
        return self.check_if_task_created(account, task_id)

    def check_if_task_created(self, account: str, task_id: int):
        resp = self.session.get(
            f"https://app-test.totango.com/t01/ciklum-automation-demo-230/api/v3/tasks?account_id={account}",
            headers=self.header,
        )
        try:
            return (i for i in resp.json() if i["id"] == 28374698347563).__next__()
        except StopIteration:
            return None
