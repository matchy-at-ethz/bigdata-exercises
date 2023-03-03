
# walk through the directories with name exercise[00-11]
# remove the line contains "restart: always"

import os
import re

def edit_dockercompose():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            if re.match(r"exercise[0-1][0-9]", name):
                dockercompose_file = os.path.join(root, name, "docker-compose.yml")
                if os.path.isfile(dockercompose_file):
                    with open(dockercompose_file, "r") as f:
                        lines = f.readlines()
                    with open(dockercompose_file, "w") as f:
                        for line in lines:
                            if not re.match(r"^\s*restart: always", line):
                                f.write(line)

if __name__ == "__main__":
    edit_dockercompose()
