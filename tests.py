from app import Totango
from datetime import date


def test_touchpoint():
    api = Totango('testing.user+230_usage@totango.com', 'TestingUser1234')
    data = {'account': 'test_1', 'subject': 'test_1', 'description': 'test_1'}
    touchpoint = api.create_touchpoint(**data)
    assert touchpoint, 'TP not created'
    assert touchpoint["properties"]["subject"] == data['subject'], 'subject is wrong'
    assert touchpoint["note_content"]["text"] == data['description'], 'description is wrong'


def test_task():
    api = Totango('testing.user+230_usage@totango.com', 'TestingUser1234')
    data = {
        'description': 'test_task_1',
        'assignee': 'testing.user+230_usage@totango.com',
        'priority': 2,
        'title': 'test_task_1',
        'account': 'test_1',
        'to_date': date(2022, 1, 1)
    }
    task = api.create_task(**data)
    assert task, 'task not created'
    assert task['title'] == data['title'], 'title is wrong'
    assert task['description'] == data['description'], 'description is wrong'
