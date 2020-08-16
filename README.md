# CP-Bot
Tool for competitive programmers to avoid copy pasting things like templates, input, output etc.
Currently works only for codeforces contests.

## How to install 
* See requirements.txt
* Install beautiful soup and urllib if you don't have using pip like `` pip install beautifulsoup4 ``

## How to use
* ``export CONTEST={contestname}`` For example if the contest URL is https://codeforces.com/contest/1370, then contestname = 1370
* Run app.py to download the testcases and expected output of all the problems.
* When you run this, you will be asked to enter the contestname (see the first point).
* Folder is created with name as contestname
* Add your template file to template.cpp.


If the contest name is 1366
```
PWD(Present working directory)
│   app.py
│   check.sh
|   bot.py
│
└───1366(subfolder)
    │
    │
    └───1366A(subfolder)
    |   │--  sol.cpp
    |   │--  input*.cpp
    |   │--  output*.cpp
    |
    └───1366B
    .
    .
    .
    .
```
* If you want to write solution to problem A go to 1366A/sol.cpp and then write.
* To check all testcases for a problem(say A) run ``./check.sh A``. This will show all the inputs, corresponding expected output and your output.
