import spacy
from sys import argv

def spacy_analise_propn_dig(text):
    '''
    :param text: text for tokinisation
    :return: dict whith propn & digital lists
    '''


    result = {'PROPN': [], 'DIGIT': []}
    nlp = spacy.load("en_core_web_sm")
    propn_lable_list = ['PERSON', 'FAC', 'NORP', 'ORG', 'GPE'] #Выбранные мной сущности относящиеся к PROPN
    doc = nlp(text)

    result['DIGIT'] = [token.text for token in doc if token.text.isdigit()]
    result['PROPN'] = [entity.text for entity in doc.ents if entity.label_ in propn_lable_list]

    return (result)

def input_tetx_from_stdin (filename):
    '''
    :param filename: name of file
    :return: text from file
    '''

    with open(filename, 'r') as text:
        return text.read()

def output_to_html(htmlname, dict_s):
    '''
    :param htmlname: name of out file
    :param htmlname: dict_s
    :return: None, write file
    '''

    with open(htmlname, 'w', encoding='utf_8_sig') as html:
        for i in dict_s['PROPN']:
                html.write('<p align="right">' + str(i) + ' ' + str(dict_s['PROPN'].count(i)) + '</p>' + '\n')
        for i in dict_s['DIGIT']:
                html.write('<p align="right">' + str(i) + ' ' + str(dict_s['DIGIT'].count(i)) + '</p>' + '\n')


text_file_name = argv[1]
html_out_file_name = argv[2]

text = input_tetx_from_stdin (text_file_name)
dict_s = spacy_analise_propn_dig(text)
output_to_html(html_out_file_name, dict_s)'''