from locust import HttpLocust, TaskSet

def login(self):

    #a=self.client.post("/login", {"username":"static", "password":"static"})
    response = self.client.get("/login/")
    csrftoken = response.cookies['csrftoken']
    #print "csrftoken"
    #print csrftoken
    print  "csrftoken"
    print csrftoken
    response = self.client.post("/login/",
                                    {"username": "static",
                                     "password": "static"},
                                    headers={"X-CSRFToken": csrftoken})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/principal")
    #l.client.get("/")
class UserBehavior(TaskSet):
    #tasks = {index:2, profile:1}
    tasks = {index:1, profile:1}

    def on_start(self):
        login(self)
    """
    def login(self):
        #a=self.client.post("/login", {"username":"static", "password":"static"})
        response = self.client.get("/login/")
        csrftoken = response.cookies['csrftoken']
        #print "csrftoken"
        #print csrftoken
        response = self.client.post("/login/",
                                    {"username": "static",
                                     "password": "static"},
                                    headers={"X-CSRFToken": csrftoken})
    """

class WebsiteUser(HttpLocust):
    host = "http://localhost:8000"
    #host = "http://www.americatv.com.pe"
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000