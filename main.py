import sys
import os

project_dir = sys.argv[0].replace('main.py', '')

if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-r', '--reverse']:
    print('Ты, по-моему, перепутал!')
else:
    for path in sys.argv[1]:
        if len(path.split('.')) == 1 and os.path.isdir(project_dir+path):
            dir_files = [file for file in os.listdir(project_dir+path) if '.py' in file]
            for file in dir_files:
                with open(project_dir+path+'/'+file, 'r') as f:
                    lines = [line[:-1] for line in f.readlines()]
                for line in lines:
                    line = line.replace('\t', '    ')
                with open(project_dir+path+'/'+file, 'w') as f:
                    f.write('\n'.join(lines)
        elif path.split('.')[1] == 'py':
            with open(project_dir+path, 'r') as f:
                lines = [line[:-1] for line in f.readlines()]
            for line in lines:
                line = line.replace('\t', '    ')
            with open(project_dir+path, 'w') as f:
                f.write('\n'.join(lines)

print('Все, господин, я сделал, всё что ты захотел!')
