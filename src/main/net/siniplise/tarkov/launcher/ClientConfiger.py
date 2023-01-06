import json

import ClientLoggingHandler

ClientLoggingHandler.Log_ClientConfig.info("开始解析JSON")

MainDirectory = "D:\\Program Files\\EscTkv"

MainMode = "live"

j1 = open(MainDirectory + "\\user\\profiles\\63bf5301ca62b0c744f43fc2.json", "r", encoding="utf-8")

j2 = open(MainDirectory + "\\user\\profiles\\797c5a32f9703eb8a2f04c30.json", "r", encoding="utf-8")

url = open("..\\..\\..\\..\\..\\..\\AKI.Server\\Aki_Data\\Server\\database\\server.json", "r", encoding="utf-8")

ser = json.load(url)

pro1 = json.load(j1)

pro2 = json.load(j2)

UserNamej1 = pro1["info"]["username"]

UserIDj1 = pro1["info"]["id"]

UserEditionj1 = pro1["info"]["edition"]

CharacterPMCNNamej1 = pro1["characters"]["pmc"]["Info"]["Nickname"]

CharacterPMCSidej1 = pro1["characters"]["pmc"]["Info"]["Side"]

CharacterPMCLvlj1 = pro1["characters"]["pmc"]["Info"]["Level"]

UserNamej2 = pro2["info"]["username"]

UserIDj2 = pro2["info"]["id"]

UserEditionj2 = pro2["info"]["edition"]

CharacterPMCNNamej2 = pro2["characters"]["pmc"]["Info"]["Nickname"]

CharacterPMCSidej2 = pro2["characters"]["pmc"]["Info"]["Side"]

CharacterPMCLvlj2 = pro2["characters"]["pmc"]["Info"]["Level"]

AKIVersionj1 = pro2["aki"]["version"]

ClientLoggingHandler.Log_ClientConfig.info("JSON解析完成")
