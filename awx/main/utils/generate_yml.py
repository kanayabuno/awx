import json
import yaml
import os
import requests
from git import Repo

### convert device config in json to ansible playbook and run the playbook

PATH_TO_REPO = os.path.expanduser('~') + "/awx-playbooks/"
URL = 'http://10.4.19.251:32121/api/v2/'
USER = 'admin'
PWD = 'temple123'
### Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

def sync_project():
  response = requests.post(URL + "projects/9/update/", auth=(USER, PWD), headers=headers, verify=False)
  if response.status_code != 202:
    print('Status:', response.status_code, '\nHeaders:', response.headers, '\nError Response:',response)

  return response.json()['id']
  

def sync_inventory_source():
  response = requests.post(URL + "inventory_sources/10/update/", auth=(USER, PWD), headers=headers, verify=False)
  if response.status_code != 202:
    print('Status:', response.status_code, '\nHeaders:', response.headers, '\nError Response:',response)

  return response.json()['id']

def add_template(new_yml):
  # get a list of available templates for this project
  response = requests.get(URL + "projects/9/playbooks/", auth=(USER, PWD), headers=headers, verify=False)
  if response.status_code != 200:
    print('Status:', response.status_code, '\nHeaders:', response.headers, '\nError Response:',response)
    
  playbooks = response.json()
  #print(json.dumps(playbooks, indent=2))

  data = {
    'name': new_yml,
    'inventory': '2',
    'project': '9',
    'playbook': new_yml 
  }

  # Create a job template
  response = requests.post(URL + "job_templates/", auth=(USER, PWD), json=data, headers=headers, verify=False)
  if response.status_code != 201:
    print('Status:', response.status_code, '\nHeaders:', response.headers, '\nContent:', response.content, '\nError Response:',response)
    exit()
  
  return response.json()['id']

def run_template(template_id):
  response = requests.post(URL + "job_templates/" + str(template_id) + "/launch/", auth=(USER, PWD), headers=headers, verify=False)
  if response.status_code != 201:
    print('Status:', response.status_code, '\nHeaders:', response.headers, '\nContent:', response.content, '\nError Response:',response) 

  return response.json()['id']

# return the file name
def git_push(id, output_yaml):
  output_file = str(id) + '.yml' 
  output_file_path = PATH_TO_REPO + output_file
  with open(output_file_path, 'w') as outfile:
    yaml.dump(yaml.safe_load(output_yaml), outfile, default_flow_style=False, sort_keys=False)

  try:
    repo = Repo(PATH_TO_REPO)
    repo.git.add('--all')
    repo.index.commit("commit from python script")
    origin = repo.remote(name='origin')
    origin.push()
  except:
    print("error occured while pushing the code")
    
  return output_file

def awplus_vlans(tasks):
  tmp_dict = {}

  for item in tasks:
    item['vlan_id'] = item.pop('id')

  tmp_dict['name'] = "Create vlans"
  tmp_dict['awplus_vlans'] = {}
  tmp_dict['awplus_vlans']['config'] = tasks
  tmp_dict['awplus_vlans']['state'] = "merged"

  return tmp_dict

def awplus_openflow(tasks):
  tmp_dict = {}

  for item in tasks['ports']:
    item['openflow'] = True

  tmp_dict['name'] = "Add openflow config"
  tmp_dict['awplus_openflow'] = tasks

  return tmp_dict
  
def json_to_yaml(input_json):
  jobs = json.loads(input_json)['jobs']
  formatted_jobs = []

  for item in jobs:
    tmp = {}
    task_list = []

    tmp = {
      'connection': 'network_cli',
      'hosts': item['name'],
      'collections': 'alliedtelesis.awplus'
    }

    tasks = item['tasks']
    for key in tasks:
      if (key == "vlans"):
        task_list.append(awplus_vlans(tasks[key]))

      if (key == "openflow"):
        task_list.append(awplus_openflow(tasks[key]))

    tmp['tasks'] = task_list
    formatted_jobs.append(tmp)

  return yaml.safe_dump(formatted_jobs, sort_keys=False)