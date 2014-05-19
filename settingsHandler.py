import pickle

class Settings(object):

    ''' # '''

    def __init__(self):
        self.file = "rybCONFIG.db"
        self.config = {}
        self.defaults = {"requiredFields": ["Age", "First Name"],
                         "dbFile": "db\\rybDB.db",
                         "defPhoto": "resc\\default.jpg"}

        self.unpickleData()

    def pickleData(self):
        pickle.dump(self.config, open(self.file, "wb"))

    def unpickleData(self):
        #if the config file does not exist, create a new config file.
        try:
            self.config = pickle.load(open(self.file, "rb"))
        except:
            self.pickleData()
            self.unpickleData()

        #if the config file does not contain required configurations,
        #fill them with defaults
        for setting, value in self.defaults.items():
            if setting not in self.config:
                self.config[setting] = value

    def saveSettings(self, func=lambda:False):
        self.unpickleData()
        func()
        self.pickleData()
        self.unpickleData()
