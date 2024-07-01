import os
sem_name = input("What semester is this class?")
base_path = os.path.join(os.path.dirname(__file__),'Problem Sets', sem_name)
if not os.path.exists(base_path):
    os.makedirs(base_path)
    json = os.path.join(base_path, 'menu.json')
    if not os.path.exists(json):
        with open(json, 'w'): pass
class_name = input("What is the name of the class?")
path = os.path.join(base_path, class_name)
if not os.path.exists(path):
    os.makedirs(path)
    pdf = os.path.join(path, 'pdf')
    os.makedirs(pdf)
    tex = os.path.join(path, 'tex')
    os.makedirs(tex)
    sty = os.path.join(path, 'sty')
    os.makedirs(sty)
    figures = os.path.join(path, 'figures')
    os.makedirs(figures)
class_copy = input("Do you want to copy files from a previous class? (y/n)")
if class_copy == 'n':
    pass
elif class_copy == 'y':
    prev_sem = input("What semester is the previous class?")
    prev_class = input("What is the name of the previous class?")
    prev_path = os.path.join(os.path.dirname(__file__),'Problem Sets', prev_sem, prev_class)
    for sty in os.listdir(prev_path + '\\sty'):
        os.system('copy \"' + prev_path + '\\sty\\' + sty + '\" \"' + path + '\\sty\\' + sty + '\"')
    if os.path.exists(prev_path + '\\template.tex'):
        os.system('copy \"' + prev_path + '\\template.tex\" \"' + path + '\\template.tex\"')