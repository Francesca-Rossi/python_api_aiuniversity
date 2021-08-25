import  json as js
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