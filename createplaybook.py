#/usr/bin/#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from lxml import etree
import os
import yaml

def Logmsg(msg):
    print msg

installlist = []
playbookname = "playbook.yml"
playbook = []
host = "host"
ansible_target_temp_path = "/tmp/"
os_class = "linux"
varslistfile = "varslist"
varslist = []

with open("installlist","r") as installlistf:
    for line in installlistf.readlines():
        line = line.strip("\r\n")
        installlist.append(line)

for component in installlist:
    componentxml = component + ".xml"
    if not os.path.exists(componentxml):
        msg = componentxml + ' not existed!'
        Logmsg(msg)
        continue
    componenttree = etree.parse(componentxml)
    task = {}

    #name task
    task['name'] = componenttree.xpath('//appname')[0].text
    task['task'] = []

    #collect vars
    task['vars'] = {}
    vars = {}
    vars[component] = {}
    for x in componenttree.xpath('//parameters')[0].xpath('parameter'):
        vars[component][x.xpath('parametername')[0].text] = None
        if x.xpath('default'):
            task['vars'][x.xpath('parametername')[0].text] = x.xpath('default')[0].text
            vars[component][x.xpath('parametername')[0].text] = x.xpath('default')[0].text

    varslist.append(vars)

    #copy package
    for x in componenttree.xpath('//packages')[0].xpath('package'):
        packname = x.xpath('packagename')[0].text
        step = {}
        step['name'] = 'copy package'
        step['copy'] = {}
        step['copy']['src'] = packname
        step['copy']['dest'] = ansible_target_temp_path
        task['task'].append(step)

    #copy template
    for a in componenttree.xpath('//deploy')[0].xpath('step'):
        for x in a.xpath('script'):
            filename = x.xpath('scriptname')[0].text
            templatename = x.xpath('templatename')[0].text
            step = {}
            step['name'] = 'copy template'
            step['template'] = {}
            step['template']['src'] = templatename
            step['template']['dest'] = ansible_target_temp_path + filename
            task['task'].append(step)

        for x in a.xpath('configuration'):
            filename = x.xpath('configurationname')[0].text
            templatename = x.xpath('templatename')[0].text
            step = {}
            step['name'] = 'copy template'
            step['template'] = {}
            step['template']['src'] = templatename
            step['template']['dest'] = ansible_target_temp_path + filename
            task['task'].append(step)

    #run script
    for a in componenttree.xpath('//deploy')[0].xpath('step'):
        runlist = []
        scriptname = a.xpath('script')[0].xpath('scriptname')[0].text
        runlist.append(scriptname)
        for x in a.xpath('configuration'):
            configurationname = x.xpath('configurationname')[0].text
            runlist.append(configurationname)
        command = " ".join(runlist)
        step = {}
        step['name'] = 'run script'
        if os_class == 'windows':
            shell = 'win_shell'
        else:
            shell = 'shell'
        step[shell] = command
        step['args'] = {'chdir':ansible_target_temp_path}
        task['task'].append(step)

    playbook.append(task)


noalias_dumper = yaml.dumper.SafeDumper
noalias_dumper.ignore_aliases = lambda self, data: True

with open(playbookname,'w') as pf:
    yaml.dump(playbook, pf, default_flow_style=False, Dumper=noalias_dumper)

with open(varslistfile,'w') as pf:
    yaml.dump(varslist, pf, default_flow_style=False, Dumper=noalias_dumper)
