import os
if os.path.exists("D:\PythonPracticeAgain\FileHandling\demofile.txt"):
  os.remove("D:\PythonPracticeAgain\FileHandling\demofile.txt")
else:
  print("The file does not exist")