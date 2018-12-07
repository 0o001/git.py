import os

commitFolderPath = "X:\\github\\project"
commitFilePath = "README.md"
commitDescription = "updated read.md"

commitFile = open(commitFolderPath + "\\" + commitFilePath, "a+", encoding="utf-8")

commitFile.write(" ")
commitFile.close()

os.system("cd " + commitFolderPath + " & " + "git commit -am \"" + commitDescription + "\" & git push")