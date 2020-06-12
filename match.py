import os
import csv


def read_txt():
    path = '3 Active 187350.txt'
    file = open(file=path, encoding='utf-8', mode='r')
    lines = file.readlines()
    file.close()
    result = []
    for l in lines:
        result.append(l.strip())
    return result


def read_csv():
    path = 'R_1Million-3_toscrub.csv'
    with open(file=path, encoding="ISO-8859-1", mode='r') as csv_file:
        rows = list(csv.reader(csv_file))
    return rows


def write_csv(lines):
    path = 'Whatsapp_3.csv'
    file = open(file=path, encoding='utf-8', mode='a', newline='')
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)
    file.close()


def main():
    phones = read_txt()
    records = read_csv()
    count = 0
    for record in records:
        count += 1
        print(count)
        if '1' + record[1] in phones:
            write_csv(lines=[record])


if __name__ == '__main__':
    main()

