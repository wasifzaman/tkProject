import pickle

class Settings(object):

    ''' # '''

    def __init__(self):
        self.file = "rybCONFIG.db"
        self.config = {}
        self.defaults = {"requiredFields": ["Age", "First Name"],
                         "dbFile": "tdb2.db",
                         "defPhoto": "monet_sm.jpg"}

        self.loadSettings()

    def pickleData(self):
        pickle.dump(self.config, open(self.file, "wb"))

    def loadSettings(self):
        #if the config file does not exist, create a new config file.
        try:
            self.config = pickle.load(open(self.file, "rb"))
        except:
            self.pickleData()
            self.loadSettings()

        #if the config file does not contain required configurations,
        #fill them with defaults
        for setting, value in self.defaults.items():
            if setting not in self.config:
                self.config[setting] = value

    def saveSettings(self, func=lambda:False):
        self.loadSettings()
        func()
        self.pickleData()
        self.loadSettings()


s = Settings()
s.loadSettings()
