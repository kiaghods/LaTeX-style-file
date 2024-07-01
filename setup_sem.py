import os
sem_name = input("What is the name of the semester?")
base_path = os.path.join(os.path.dirname(__file__),'Notes', sem_name)
# print(root)
if not os.path.exists(base_path):
    # print(base_path)
    os.makedirs(base_path)
    path = base_path + '\\figures'
    if not os.path.exists(path):
        os.makedirs(path)
    path = base_path + '\\pdf'
    if not os.path.exists(path):
        os.makedirs(path)
    path = base_path + '\\sty'
    if not os.path.exists(path):
        os.makedirs(path)
    path = base_path + '\\tex'
    if not os.path.exists(path):
        os.makedirs(path)
    json = os.path.join(os.path.dirname(__file__),'Notes',sem_name,'menu.json')
    if not os.path.exists(json):
        with open(json, 'w'): pass
    last_sem = input("What was the last semester? (If this is the first semester, type 'none')")
    if last_sem == 'none':
        exit()
    ls_path = os.path.join(os.path.dirname(__file__),'Notes', last_sem)
    last_sty = os.listdir(ls_path + '\\sty')
    for sty in last_sty:
        os.system('copy \"' + ls_path + '\\sty\\' + sty + '\" \"' + base_path + '\\sty\\' + sty + '\"')
    template_path = os.path.join(os.path.dirname(__file__),'Notes', last_sem, 'template.tex')
    os.system('copy \"' + template_path + '\" \"' + base_path + '\\template.tex\"')
else:
    print("Semester already exists")
    exit()