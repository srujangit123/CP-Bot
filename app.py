import urllib.request
from bs4 import BeautifulSoup
import re
import os


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
            fp = open(i + ".cpp", "w")
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
        inputText = io[0].get_text()
        outputText = io[1].get_text()
        words = problem.split("/")
        Ifile = open(words[len(words) - 1] + "input.txt", "w")
        Ifile.write(inputText)
        Ofile = open(words[len(words) - 1] + "output.txt", "w")
        Ofile.write(outputText)



contestName = input("contest number: ")

problemListsURL = problemsURLs(contestName) 
template= open("./template.cpp", "r").read()

fileNames = []
for problem in problemListsURL:
    a = problem.split("/")
    fileNames.append(contestName + a[len(a) - 1])
    
makeSolutionFiles(fileNames, template)


createIOfiles(problemListsURL)