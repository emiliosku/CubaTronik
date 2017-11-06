"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import os
import logging
import re
import time

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
                           "=====================\n\n<SIGNIN>%d\n" %(user, password, picture, time.time()))


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
            return int("0")

    def loadDiyDrinks(self):
        try:
            booze = []
            soda = []
            extraTouch = []
            dir = os.path.join(os.getcwd(), "drinks\\diy_drinks_list.txt")
            with open(dir, "r") as data:
                self.drinks = data.readlines()
            boozeString = re.compile(r'<BOOZE>(\w+)\n')
            boozeStringWS = re.compile(r'<BOOZE>(\w+\s\w+)\n')
            sodaString = re.compile(r'<SODA>(\w+)\n')
            sodaStringWS = re.compile(r'<SODA>(\w+\s\w+)\n')
            extraString = re.compile(r'<EXTRA>(\w+)\n')
            extraStringWS = re.compile(r'<EXTRA>(\w+\s\w+)\n')
            for line in self.drinks:
                if boozeString.search(line):
                    booze.append(boozeString.findall(line)[0])
                elif boozeStringWS.search(line):
                    booze.append(boozeStringWS.findall(line)[0])
                elif sodaString.search(line):
                    soda.append(sodaString.findall(line)[0])
                elif sodaStringWS.search(line):
                    soda.append(sodaStringWS.findall(line)[0])
                elif extraString.search(line):
                    extraTouch.append(extraString.findall(line)[0])
                elif extraStringWS.search(line):
                    extraTouch.append(extraStringWS.findall(line)[0])
            availableDrinks = [booze, soda, extraTouch]
            return availableDrinks
        except:
            logging.warning("Problem while loading the available drinks. Feature disabled")

# TODO: function that reads a file (or creates it if it does not exist), where each bottle's position is stored.
    def loadMenu(self):
        # try:
        chart = {}
        dir = os.path.join(os.getcwd(), "drinks\\menu.txt")
        with open(dir, "r") as data:
            menuMixes = data.read()
            mixes = menuMixes.split("**")
            for mix in mixes:
                if mix != "":
                    actualMixes = mix.split(";")
                    drinks = actualMixes[0].replace("\n", "")
                    description = actualMixes[1]

                    chart[str(drinks)] = str(description)
        # chart.keys() in order to know the drinks.
        # for loop in order to know all the descriptions like chart[i] = description string.
        return chart


