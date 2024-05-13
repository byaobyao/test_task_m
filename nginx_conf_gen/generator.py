#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.txt')

with open('info.yml') as f:
    sites = yaml.safe_load(f)

for site in sites:
    r1_conf = site['name']+'.conf'
    with open(r1_conf, 'w') as f:
        f.write(template.render(site))
