import subprocess


# Liste der Bibliotheken herrausfinden
process = subprocess.Popen(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Liste in eine readable-Form bringen
packages = stdout.decode('utf-8').split('\n')[2:]
for p in packages:
    packages[packages.index(p)] = p.split(' ')[0]

# Die Bibliotheken updaten
for p in packages:
    print('\n\n' + p + ':\n')
    process = subprocess.call(['pip', 'install', '--upgrade', p])