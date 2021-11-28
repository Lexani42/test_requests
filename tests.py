from app import Totango
from datetime import date

totango = Totango('testing.user+230_usage@totango.com', 'TestingUser1234')


def test_touchpoint_1():
    assert totango.create_touchpoint('test_1', 'test_1', 'test_1')


def test_touchpoint_2():
    assert totango.create_touchpoint('test_2', 'test_2', 'test_2')


def test_touchpoint_3():
    assert totango.create_touchpoint('test_3', 'test_3', 'test_3')


def test_touchpoint_4():
    assert totango.create_touchpoint('test_4', 'test_4', 'test_4')


def test_touchpoint_5():
    assert totango.create_touchpoint('test_5', 'test_5', 'test_5')


def test_task_1():
    assert totango.create_task('test_task_1', 'testing.user+230_usage@totango.com', 2, 'test_task_1', 'test_1', date(2022, 1, 1))


def test_task_2():
    assert totango.create_task('test_task_2', 'testing.user+230_usage@totango.com', 2, 'test_task_2', 'test_2', date(2022, 2, 2))


def test_task_3():
    assert totango.create_task('test_task_3', 'testing.user+230_usage@totango.com', 2, 'test_task_3', 'test_3', date(2022, 3, 3))


def test_task_4():
    assert totango.create_task('test_task_4', 'testing.user+230_usage@totango.com', 2, 'test_task_4', 'test_4', date(2022, 4, 4))


def test_task_5():
    assert totango.create_task('test_task_5', 'testing.user+230_usage@totango.com', 2, 'test_task_5', 'test_5', date(2022, 5, 5))

