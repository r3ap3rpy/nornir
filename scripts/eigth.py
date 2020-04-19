from nornir import InitNornir
from nornir.plugins.tasks.text import template_file
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(config_file = 'config.yaml')

hosts = nr.filter(site= 'home', role = 'cisco')

fact_result = hosts.run(task = networking.napalm_get, getters = ["facts"])

int_list = fact_result['host2.dc1'][0].result['facts']['interface_list']
int_list.remove('FastEthernet0/0')
result = hosts.run(task = template_file, template = 'jin.j2', path = '.', interfaces = int_list, title= "Shutdown Interfaces")

shutitalldown = hosts.run(task = networking.netmiko_send_config, config_commands =  result['host2.dc1'][0].result.replace('\n\n','\n').split('\n'))

print_result(shutitalldown)
