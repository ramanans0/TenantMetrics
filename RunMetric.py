#!/usr/bin/env python3

import threading
import MetricGen

def tenantProcess():
    threading.Timer(60.0, tenantProcess).start()
    MetricGen.setup()

tenantProcess()