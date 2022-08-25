import csv

def reading_file():
    name = input("Your filename: ")
    subs =[]
    try:
        with open(name+'.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            url1=""
            for url in csv_reader:
                url1+=str(url)
                subs.append(url1[27:-3:])
                url1=""
    except:
        print("File doesn't exist")
        return
    return subs
