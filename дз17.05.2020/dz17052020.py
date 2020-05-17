with open("task.txt", "r") as file:
    line = file.readline()
    safari = []
    chrome = []
    firefox = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if a in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari.append(s_sel)
            elif ff in choose:
                firefox.append(s_sel)
            elif ch in choose:
                chrome.append(s_sel)
print("Количество браузеров за 17 мая:")        
print("Браузер Safari: " + str(len(safari)))
print("Браузер Firefox: " + str(len(firefox)))
print("Браузер Chrome: " + str(len(chrome)))
            
with open("task.txt", "r") as file:
    line = file.readline()
    safari = []
    chrome = []
    firefox = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if b in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari.append(s_sel)
            elif ff in choose:
                firefox.append(s_sel)
            elif ch in choose:
                chrome.append(s_sel)
print("Количество браузеров за 18 мая:")        
print("Браузер Safari: " + str(len(safari)))
print("Браузер Firefox: " + str(len(firefox)))
print("Браузер Chrome: " + str(len(chrome)))
            
with open("task.txt", "r") as file:
    line = file.readline()
    safari = []
    chrome = []
    firefox = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if c in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari.append(s_sel)
            elif ff in choose:
                firefox.append(s_sel)
            elif ch in choose:
                chrome.append(s_sel)
print("Количество браузеров за 19 мая:")        
print("Браузер Safari: " + str(len(safari)))
print("Браузер Firefox: " + str(len(firefox)))
print("Браузер Chrome: " + str(len(chrome)))

with open("task.txt", "r") as file:
    line = file.readline()
    safari = []
    chrome = []
    firefox = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if d in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari.append(s_sel)
            elif ff in choose:
                firefox.append(s_sel)
            elif ch in choose:
                chrome.append(s_sel)
print("Количество браузеров за 120 мая:")        
print("Браузер Safari: " + str(len(safari)))
print("Браузер Firefox: " + str(len(firefox)))
print("Браузер Chrome: " + str(len(chrome)))
            

#пока вот так. Код - вырви глаза


