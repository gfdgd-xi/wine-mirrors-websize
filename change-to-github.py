#!/usr/bin/env python3
import os
import json
with open(f"information.json", "r") as file:
    things = json.loads(file.read())
newThings = []
for i in things:
    if not "http://seafile.jyx2048.com:2345/spark-deepin-wine-runner/data/" in i[1]:
        newThings.append(i)
        continue
    lists = i
    pathName = os.path.basename(lists[1])
    pathNameWithoutEnd = os.path.splitext(pathName)[0]
    lists[1] = f"https://github.com/rain-gfd/wine-download/releases/download/{pathNameWithoutEnd}/{pathName}"
    newThings.append(lists)
    #newThings.append()
with open("information.json", "w") as file:
    file.write(json.dumps(newThings, ensure_ascii=False, indent=4))