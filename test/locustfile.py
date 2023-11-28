import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def example_all(self):
        self.client.get("/example")
        self.client.post("/example")
        self.client.put("/example")

    @task(3)
    def example_get(self):
        self.client.get("/example")

    @task
    def example_post(self):
        self.client.post("/example")

    @task
    def example_put(self):
        self.client.put("/example")

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})