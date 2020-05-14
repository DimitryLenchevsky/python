
import re
from collections import Counter
import csv


def unique_id():
    with open('task.txt', 'r') as file:
        id_list = []
        line = file.readline()
        for line in file:
            unique = line.split(' ')[0]
            if unique not in id_list:
                id_list.append(unique)
        print('Количество уникальных ID: ')
        print(len(id_list))
        browsers()


def browsers():
    with open('task.txt', 'r') as file:
        line = file.readline()
        safari = []
        chrome = []
        firefox = []
        
        for line in file:
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
    
    print("Браузер Safari: " + str(len(safari)))
    print("Браузер Firefox: " + str(len(firefox)))
    print("Браузер Chrome: " + str(len(chrome)))



def reader(filename):

    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.read()

        ips_list = re.findall(regexp, log)

    return ips_list


def count(ips_list):
    count = Counter(ips_list)

    return count


def write_csv(count):

    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']
        writer.writerow(header)

        for item in count:
            writer.writerow( (item, count[item]) )



if __name__ == '__main__':

    write_csv(count(reader('task.txt')))


unique_id()