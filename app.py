import os
from bot import get_problem_urls, make_solution_files, create_io_files

# ContestName is the number in the Codeforces contest URL
# For example if the contest URL is https://codeforces.com/contest/1366, then contestName is 1366


def main():
    contest_id = input("contest ID/number in the contest URL: ")

    try:
        os.mkdir("./" + contest_id)
    except OSError:
        print("Folder already exists")

    problem_urls = get_problem_urls(contest_id)
    template = open("./template.cpp", "r").read()

    problem_folder_names = []

    # problem_urls -> /contest/contest_id/problem/letter(A-Z)
    # Create problem names as contest_id + problem_code. Like 1336A
    for url in problem_urls:
        url_split = url.split("/")
        problem_folder_names.append(contest_id + url_split[len(url_split) - 1])

    # Create problem folders and make solution files for all problems with template
    make_solution_files(problem_folder_names, template, contest_id)

    # Create testcases files inside problem folders
    create_io_files(problem_urls, contest_id)


if __name__ == "__main__":
    main()
