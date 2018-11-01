#!/bin/#!/usr/bin/env bash
mkdir /tmp/pipelinetesting/
mount -t cifs //192.168.56.110/pipeline /tmp/pipelinetesting -o username=pipelineuser,password=1,iocharset=utf8
