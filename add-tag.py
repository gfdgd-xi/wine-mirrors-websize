import json
with open("information.json", "r") as file:
    data = json.loads(file.read())
newList = []
for i in data:
    # 自动加 tag
    if (len(i) > 2):
        newList.append(i)
        continue
    # 生产 tag
    tagList = []
    # 架构 .so 对照表
    archMap = {
        "i386": "/usr/lib/i386-linux-gnu/ld-linux.so.2",
        "amd64": "/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2",
        "armhf": "/usr/lib/arm-linux-gnueabihf/ld-linux-armhf.so.3",
        "armel": "/usr/lib/arm-linux-gnueabi/ld-linux.so.3",
        "arm64": "/usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1",
        "aarch64": "/usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1",
        "riscv64": "/usr/lib/riscv64-linux-gnu/ld-linux-riscv64-lp64d.so.1",
        "mips64el": "/usr/lib/mips64el-linux-gnuabi64/ld.so.1",
        "ppc64el": "/usr/lib/powerpc64le-linux-gnu/ld64.so.2",
        "loong64": "/usr/lib/loongarch64-linux-gnu/ld-linux-loongarch-lp64d.so.1",
        "loongarch64": "/usr/lib/loongarch64-linux-gnu/ld.so.1",
        "x86_64": ["/usr/lib/i386-linux-gnu/ld-linux.so.2", "/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2"]
    }
    systemGlibcMap = {
        "debian10": "2.28",
        "debian11": "2.31",
        "debian12": "2.36",
        "ubuntu18": "2.27",
        "ubuntu20": "2.31",
        "ubuntu22": "2.35",
        "ubuntu24": "2.39"
    }
    # 判断名称是否含有指定关键词
    isSearch = False
    for k in archMap.keys():
        if k in i[0]:
            isSearch = True
            isSystem = False
            for g in systemGlibcMap.keys():
                if g in i[0]:
                    isSystem = True
                    if (type(archMap[k]) == list):
                        allTag = [k, systemGlibcMap[g]]
                        for d in archMap[k]:
                            allTag.append(d)
                        tagList.append(allTag)
                    else:
                        tagList.append([k, systemGlibcMap[g], archMap[k]])
            if (not isSystem):
                if (type(archMap[k]) == list):
                    allTag = [k]
                    for d in archMap[k]:
                        allTag.append(d)
                    tagList.append(allTag)
                else:
                    tagList.append([k, archMap[k]])
            # box86+binfmt
            if k == "i386":
                tagList.append("exagear")
                tagList.append(["box86", "binfmt"])
                tagList.append(["lat", "i386", "binfmt"])
                tagList.append(["qemu-user", "i386", "binfmt"])
            if k == "amd64":
                tagList.append("exagear")
                tagList.append(["box64", "binfmt"])
                tagList.append(["lat", "amd64", "binfmt"])
                tagList.append(["qemu-user", "amd64", "binfmt"])
            if k == "x86_64":
                tagList.append("exagear")
                tagList.append(["box86", "box64", "binfmt"])
                tagList.append(["lat", "i386", "amd64", "binfmt"])
                tagList.append(["qemu-user", "i386", "amd64", "binfmt"])
            if "wow64" in i[0]:
                tagList.append("exagear")
                tagList.append(["box86", "box64", "binfmt"])
                tagList.append(["lat", "i386", "amd64", "binfmt"])
                tagList.append(["qemu-user", "i386", "amd64", "binfmt"])
    if (not isSearch):
        tagList = []
        allTag = ["x86_64"]
        # 没有被任何一种情况识别到，则使用默认
        for d in archMap["x86_64"]:
            allTag.append(d)
        tagList = [allTag]
        tagList.append("exagear")
        tagList.append(["box86", "box64", "binfmt"])
        tagList.append(["lat", "i386", "amd64", "binfmt"])
        tagList.append(["qemu-user", "i386", "amd64", "binfmt"])
    newList.append([i[0], i[1], tagList])
jsonStr = json.dumps(newList, ensure_ascii=False, indent=4)
#print(jsonStr)
with open("information.json", "w") as file:
    file.write(jsonStr)
