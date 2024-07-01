import os
sem_name = input("What semester is this class?")
class_name = input("What is the name of the class?")
path = os.path.join(os.path.dirname(__file__),'Problem Sets', sem_name,class_name)
num_psets = int(input("How many problem sets are there?"))
pset_path = os.path.join(path,"tex")
for i in range(num_psets):
    ps = os.path.join(pset_path, "Problem Set " + str(i+1) + '.tex')
    if not os.path.exists(ps):
        if os.path.exists(os.path.join(path, 'template.tex')):
            os.system('copy \"' + path + '\\template.tex\" \"' + ps + '\"')
        else:
            with open(ps, 'w'): pass