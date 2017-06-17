"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import os
import logging

class loadData():
    def loadProfilePictures(self):
        try:
            self.files = []
            for file in os.listdir("./profiles"):
                if file.endswith(".png"):
                    self.files.append(os.path.join(os.getcwd(), "profiles\\" + file))
            logging.debug("Profile pictures loaded successfully.")
            return self.files
        except:
            logging.warning("Problem while loading Profile pictures. Feature disabled.")

    def saveInfo(self, user, password, picture):
        dir = os.getcwd()
        fileName = dir + "\\log\\" + user + ".txt"
        with open(fileName, "w") as textFile:
            textFile.write("<USER>%s\n<PASSWORD>%s\n<PICTURE>%s\n"
                           "=====================\n\n" %(user, password, picture))

    def refreshData(self):
        try:
            users = []
            for user in os.listdir("./log"):
                if user.endswith(".txt"):
                    users.append(os.path.join(os.getcwd(), "log\\" + user))
            logging.debug("Users refreshed successfully,")
            return users
        except:
            logging.warning("Problem while loading users. Feature disabled")


    # def loadInfo