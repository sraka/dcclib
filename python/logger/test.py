import os
import sys
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__),"../"))
import utils.pYaml

file_path = os.path.join(os.path.dirname(__file__), 'yaml_config.yaml')

data = utils.pYaml.read_yaml(file_path)


from pprint import pprint
pprint(data)

users = [{'name': ['John Doe' , 'adfkdjfkl'], 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

write_file = os.path.join(os.path.dirname(__file__), 'yaml_config_write.yaml')
print write_file
with open(write_file , 'w') as writer:
    data = yaml.dump(users , writer, default_flow_style=False, explicit_start=True)

print dir(yaml.dump)
'''
explicit_start=True, 
canonical=True
'''