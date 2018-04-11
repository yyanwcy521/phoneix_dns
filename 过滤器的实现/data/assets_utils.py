from pymongo import MongoClient

def clean_file_from_utf8_lines(filename):
    utf_counter, str_counter = 0, 0
    with open(filename, 'r') as f:
        with open(filename + "_ascii.txt", 'a') as f_a:
            for line in f:
                try:
                    line.decode('ascii')
                    str_counter += 1
                    f_a.write(line)
                except:
                    utf_counter += 1

    print "String counter: " + str(str_counter)
    print "Utf counter: " + str(utf_counter)


def clean_spanish_file():
    clean_file_from_utf8_lines("es.txt")


def clean_german_file():
    clean_file_from_utf8_lines("de.txt")


def clean_french_file():
    clean_file_from_utf8_lines("fr.txt")


def export_domains_txt(documents, output_file):
    with open(output_file, 'wb') as f:
        for document in documents:
            f.write("%s\n" % document["domain"])

def export_domains_es_txt():
    client = MongoClient()
    documents = client.botime.alexa_es_g.find({ "detection.language" : "es" }, timeout=False)
    export_domains_txt(documents, 'alexa_es.txt')


def export_domains_fr_txt():
    client = MongoClient()
    documents = client.botime.alexa_fr_g.find({ "detection.language" : "fr" }, timeout=False)
    export_domains_txt(documents, 'alexa_fr.txt')


def export_domains_ru():
    client = MongoClient()
    slavic_languages = ["pl", "lv", "hr", "sl", "hu", "cs", "sk", "et", "lt", "fi", "sr" ]
    documents = client.botime.alexa_ru_g.find({ "detection.language" : { "$in" : slavic_languages} }, timeout=False)
    export_domains_txt(documents, 'alexa_ru.txt')
