import  json as js
from datetime import date

def get_slug_degree_course():
    file = open("doc\slug_degree.json", 'r')
    slug_degree_course = js.load(file)
    file.close()
    return slug_degree_course


#TODO: funzione che possiamo utilizzare per aggiungere nuovi slug alla leaure
def set_slug_degree_course(key, value):
    readFile = open("doc\slug_degree.json", 'r')
    slug_degree_course = js.load(readFile)
    print(slug_degree_course)
    #TODO: controllare che il dizionario non contenga già questa chiave
    slug_degree_course[key]= value;
    readFile.close()
    writeFile = open("doc\slug_degree.json", 'w')
    print(slug_degree_course)
    writeFile.write(js.dumps(slug_degree_course))
    writeFile.close()

def average_dict(dictionary, field):
    sum = 0
    count = 0
    for i in dictionary:
        if field in i.keys():
            if type(i[field]) == int:
                sum = sum + i[field]
                count += 1
    if count > 0:
        avg = sum / count
        return avg
    return 0

def average_list(list):
    sum = 0
    count = 0
    for i in list:
        if type(i) == int:
            sum = sum + i
            count += 1
    if count > 0:
        avg = sum / count
        return avg
    return 0

def fromFloatToYearAndMonth(float_n):
    year = int(float_n)
    month_decimal = float_n - year
    if month_decimal >0:
        month = int(month_decimal * 12)
        return(str(year) + ' anni e '+ str(month) +' mesi')
    else:
        return( str(year) + ' anni')

def todayToString():
    today = date.today()
    date_today = today.strftime("%d-%m-%Y")
    return date_today