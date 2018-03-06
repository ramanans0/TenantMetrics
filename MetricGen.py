#!/usr/bin/env python3

import time
import sys
import re
import json
import csv
import os


def dataParse(location, id):
    with open(location+"metrics.json") as metrics:
        metric = json.load(metrics)
    output = []
    for met in metric:
        ts = time.time()
        ts = str(ts)
        regstr = r"([0-9]+)"
        newts = re.search(regstr, ts)
        ts = newts.group(1)
        val = met
        dat = metric[met]
        output.append([ts,id,val,dat])
    with open("tenant_metrics.csv", "a", newline="") as fp:
        data = csv.writer(fp, delimiter=",")
        data.writerows(output)

def setup():
    val = os.listdir("./var/run/tenant/")
    num = 1
    for direc in val:
        dataParse("./var/run/tenant/" + str(direc) + "/",direc)


