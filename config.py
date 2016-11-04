##configuration editor

import configparser, os

class Configuration():
    def __init__(self,filename = "./config.ini"):
        if os.path.isfile(filename):
            config = configparser.ConfigParser()
            config.read(filename)
            self.clientid=config["spotify"]["client-id"]
            self.clientsecret = config["spotify"]["client-secret"]
            self.user = config["spotify"]["user"]
            self.redirect = config["spotify"]["redirect"]
