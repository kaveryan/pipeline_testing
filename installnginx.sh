#!/bin/#!/usr/bin/env bash
cd /data/pipeline1/unzipnginx/nginx-1.15.5
./configure  --prefix=/opt/pipeline1/nginx
make && make install
