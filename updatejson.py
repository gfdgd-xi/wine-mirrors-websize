#!/usr/bin/env python3
import os
import json
with open("information.json", "r") as file:
    lists = json.loads(file.read())
listsnew = []
for i in lists:
    listsnew.append([i[0], f"https://github.com/rain-gfd/wine-download/releases/download/{os.path.splitext(os.path.basename(i[1]))[0]}/{i[1]}"])
print(listsnew)
with open("information.json", "w") as file:
    file.write(json.dumps(listsnew, ensure_ascii=False, indent=4))
