from locust import HttpLocust, TaskSet

def login(self):

    #a=l.client.post("/login", {"username":"static", "password":"static"})
    #response = self.client.get("/login/")
    #csrftoken = response.cookies['csrftoken']
    #print "csrftoken"
    #print csrftoken
    #response = self.client.post("/login/",
    #                                {"username": "static",
    #                                 "password": "static"},
    #                                headers={"X-CSRFToken": csrftoken})
    pass

def index(l):
    l.client.get("/esto-es-guerra-teens/encuesta/418/")

def profile(l):
    #l.client.get("/principal")
    l.client.get("/")
class UserBehavior(TaskSet):
    tasks = {index:2, profile:1}

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    #host = "http://localhost:8000"
    host = "http://www.americatv.com.pe"
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000