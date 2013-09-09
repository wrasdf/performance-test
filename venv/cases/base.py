
class Base(object):

    def __init__(self, webclient):
        self.client = webclient

    def get(self,url):
        self.client.get(url)

    def post(self,url,data):
        self.client.post(url,data,headers={"Content-type":"application/json"})

    def put(self,url,data):
        self.client.put(url,data,headers={"Content-type":"application/json"})
