import urllib.request
from bs4 import BeautifulSoup
import re
import os


def get_problem_urls(contest_id):
    contest_url = "https://codeforces.com/contest/" + contest_id

    fp = urllib.request.urlopen(contest_url)
    HTMLdata = fp.read().decode("utf8")
    fp.close()

    soup = BeautifulSoup(HTMLdata, "html.parser")
    problem_urls = []
    problem_base_url = "/contest/" + contest_id + "/problem/"
    for link in soup.find_all("a"):
        href = link.get("href")
        # Check if the link is a problem link and append to problem_urls list
        if re.search("^" + problem_base_url, href) and href not in problem_urls:
            problem_urls.append(href)

    return problem_urls


def make_solution_files(folder_names, template_for_solution_files, contest_id):

    for folder_name in folder_names:
        try:
            # Make problem folders like 1366A, 1366B etc
            folder_path = "./" + contest_id + "/" + folder_name
            os.mkdir(folder_path)

            # Create a file sol.cpp inside 1366A, 1366B etc
            fp = open(folder_path + "/sol.cpp", "w")

            # Insert template inside sol.cpp
            fp.write(template_for_solution_files)

        except OSError:
            print(folder_name, " already exists")

    print("All solution files generated")


def create_io_files(problem_relative_urls, contest_id):

    for relative_url in problem_relative_urls:
        absolute_url = "https://codeforces.com" + relative_url

        # Requesting HTML data of a problem
        fp = urllib.request.urlopen(absolute_url)
        problem_page = fp.read().decode("utf8")
        fp.close()

        problem_soup = BeautifulSoup(problem_page, "html.parser")

        # All input and output lists in HTML are inside <pre>.
        # This will create a list of all input and output files.
        # Like testcase 1 input -> io_list[0]
        #                 ouput -> io_list[1]
        io_list = problem_soup.find_all("pre")

        words = relative_url.split("/")
        problem_code = words[len(words) - 1]

        for i in range(len(io_list)//2):
            input_text = io_list[i].get_text()
            output_text = io_list[i + 1].get_text()
            path_for_io_files = "./" + contest_id + "/" + contest_id + problem_code

            # This creates input and output files like input0.txt, input1.txt, ...., input(len(io_list//2) - 1).txt
            input_file = open(path_for_io_files + "/input" + str(i) + ".txt", "w")
            input_file.write(input_text)
            output_file = open(path_for_io_files + "/output" + str(i) + ".txt", "w")
            output_file.write(output_text)
