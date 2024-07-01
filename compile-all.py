import pathlib, os
tex_files = list(pathlib.Path('./').rglob('*.tex'))
compiled = []
for tex_file in tex_files:
    if 'template.tex' in str(tex_file):
        print('Skipped: ' + str(tex_file))
        continue
    text = open(tex_file, 'r').read()
    if 'documentclass' in text:
        os.system('latexmk -pdf \"' + str(tex_file) + '\" -cd -f -g -outdir=..\\pdf')
        compiled.append(str(tex_file))
print('-------------------')
print('Compiled:\n' + '\n'.join(compiled))