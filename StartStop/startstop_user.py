from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    def on_start(self):
        print("Starting")

    @task
    def task_1(self):
        print("My tasks")

    def on_stop(self):
        print("Stopping")

# CommandLine :  locust -f StartStop/startstop_user.py -r 1 -u 1 -t 10s --headless --only-summary
