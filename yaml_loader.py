#!/usr/bin/env python

import yaml
import lazyxml

with open("test.yaml", 'r') as stream:
    yaml_source = yaml.load(stream)
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
        exit

print(lazyxml.dumps(yaml_source, indent=' ' * 4))
