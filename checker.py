from pathlib import Path
import os
import add
import learn

x = 1
allow = False
inputuser = "none"

def filecheck(inputuser, directory):
    x = 1
    global printstr
    directory = inputuser
    my_file = Path("lib/" + directory + "/" + str(x))
    if os.path.exists("lib/" + directory):
        if my_file.is_file():
            print(x)
            x = int(x)
            x = x + 1
            filecheck()
    else:
        printstr = "De naam die je ingevoerd hebt bestaat niet"


def foldercheck(directory, entry):
    global printstr
    global allow
    if not allow:
        if not os.path.exists("lib/" + directory):
            os.makedirs("lib/" + directory)
            allow = True
        else:
            printstr = "Deze lijst bestaat al"
            allow = False
            entry.configure(text=printstr, fg="red")

    else:
        pass
