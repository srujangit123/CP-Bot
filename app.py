import urllib.request
from bs4 import BeautifulSoup
import re
import os

contestName = input("contest number: ")

def problemsURLs(contestName):
    contestURL = "https://codeforces.com/contest/" + contestName
    fp = urllib.request.urlopen(contestURL)
    mybytes = fp.read()

    HTMLData = mybytes.decode("utf8")
    fp.close()
    soup = BeautifulSoup(HTMLData, "html.parser")
    hrefs = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if(re.search("^/contest/" + contestName + "/problem/", href) and href not in hrefs):
            hrefs.append(href)

    return hrefs


def makeSolutionFiles(fileNames, template):
    for i in fileNames:
        try:
            os.mkdir("./" + contestName + "/" + i)
            fp = open(contestName + "/" + i + "/sol.cpp", "w")
            # fp = open(contestName + "/" + i + ".cpp", "w")
            fp.write(template)
        except:
            print(i, " already exists")

    print("All solution files generated")
    print("Now gathering all solutions file")


def createIOfiles(problemListsURL):
        
    for i in range(len(problemListsURL)):
        problemListsURL[i] = "https://codeforces.com" + problemListsURL[i]

    for problem in problemListsURL:
        fp = urllib.request.urlopen(problem)
        mybytes = fp.read()
        problemPage = mybytes.decode("utf8")
        fp.close()

        IOSoup = BeautifulSoup(problemPage, "html.parser")

        io = IOSoup.find_all("pre")


        numberOfIOs = len(io)

        words = problem.split("/")
        problemCode = words[len(words) - 1]

        for i in range(numberOfIOs//2):
            inputText = io[i].get_text()
            outputText = io[i + 1].get_text()
            Ifile = open(contestName + "/" + contestName + problemCode + "/input" + str(i) + ".txt", "w")
            Ifile.write(inputText)
            Ofile = open(contestName + "/" + contestName + problemCode + "/output" + str(i) + ".txt", "w")
            Ofile.write(outputText)


try:
    os.mkdir("./" + contestName)
except:
    print("Folder already exists")

problemListsURL = problemsURLs(contestName) 
template= open("./template.cpp", "r").read()

fileNames = []
for problem in problemListsURL:
    a = problem.split("/")
    fileNames.append(contestName + a[len(a) - 1])
    
makeSolutionFiles(fileNames, template)


createIOfiles(problemListsURL)