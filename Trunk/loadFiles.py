"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import os

class loadData():
    def loadProfilePictures(self):
        files = []
        for file in os.listdir("./profiles"):
            if file.endswith(".png"):
                files.append(os.path.join(os.getcwd(), "profiles\\" + file))
        return files