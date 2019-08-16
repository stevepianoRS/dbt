import subprocess

# class ModifiedFiles(object):
modified_sql_models = set()
non_modified_sql_models = set()

def get_modified_files():
    status = subprocess.run(['git', 'status'], capture_output=True)
    diff = subprocess.run(['git', 'diff', 'master', '--name-only'], capture_output=True)

    for word in status.stdout.decode('UTF-8').split():
        if '.sql' in word: 
            modified_sql_models.add(word)

    for word in diff.stdout.decode('UTF-8').split():
        if '.sql' in word:
            modified_sql_models.add(word)

    modified_sql_models.add('testing/doctors.sql')
    modified_sql_models.add('device.sql')
    modified_sql_models.add('device.sql')

    print(modified_sql_models)
    # print(diff.stdout.decode('UTF-8'))

def get_BQ_locations():
    datasets = subprocess.run(['bq', 'ls', '--project_id', 'rsdavinciprod'], capture_output=True)
    datasets = datasets.stdout.decode('UTF-8').split()
    del datasets[0:2]

    for dataset in datasets:
        models = subprocess.run(['bq', 'ls', '-n', '500', 'rsdavinciprod:{}'.format(dataset)], capture_output=True)
        print(models.stdout.decode('UTF-8').split())
        break
    
    print(datasets)

if __name__ == '__main__':
    get_modified_files()
    get_BQ_locations()