"""1 Work(Directory)
    2.report.doc (File)
    2.main.py
    2.Project (Directory)
      3.talk.ppt (File)
"""

"""
1.We want to use 3.talk.ppt

Absolut file path:
/Work/Project/talk.ppt

Relative file path (We work in 2.Project(Directory)):
./talk.ppt

2. We work in Work(Directory) and we want to use 3.talk.ppt

Relative path:
./Project/talk.ppt
"""

"""
What if we wanted to go upwards in the directory tree
3. We work in 2.Project(Directory) and we want to use report.doc

Relative path:
../report.doc

4. We work in main.py and we want to use file
./report.doc 
"""