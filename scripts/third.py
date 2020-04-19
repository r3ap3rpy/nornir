from nornir import InitNornir
from nornir.plugins.tasks import files,commands
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file = 'config.yaml')

host = nr.filter(site = "home", role = "host")

def deployApp(task):
    task.run(task = commands.remote_command,
            command = "mkdir -p /tmp/pyapp",
            name = "Create App Folder")
    task.run(task = files.sftp,
                        action = "put",
                        src = 'app.py',
                        dst = '/tmp/pyapp/app.py',
                        name = "Upload app source")
    task.run(task = files.sftp,
            action = "put",
            src = 'requirements.txt',
            dst = '/tmp/pyapp/requirements.txt',
            name = 'Upload requirements file.')
    task.run(task = commands.remote_command,
            command = 'pip install -r /tmp/pyapp/requirements.txt --user',
            name = 'Install requirements!')

result = host.run(task = deployApp)

print_result(result)

