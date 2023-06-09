import time
import pytest


@pytest.fixture(scope='class', autouse=True)
def test_class_fixture(request):
    start_time = time.time()
    print('Start time:', time.ctime(start_time))

    def teardown():
        end_time = time.time()
        print('End time:', time.ctime(end_time))
        duration = end_time - start_time
        print('Total duration:', duration)

    request.addfinalizer(teardown)


@pytest.fixture()
def test_fixture(request):
    start_time = time.time()
    print('Test start time:', time.ctime(start_time))

    def teardown():
        end_time = time.time()
        print('Test end time:', time.ctime(end_time))
        duration = end_time - start_time
        print('Test total duration:', duration)

    request.addfinalizer(teardown)
