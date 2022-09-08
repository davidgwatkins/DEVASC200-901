#! /usr/bin/python3

from ne_classes import Router, Switch

rtr1 = Router("NCS540","IOS XR 7.6.2","10.114.15.218")
rtr2 = Router("5164","SA OS 10.7.1.p1","10.114.15.219")
rtr3 = Router("IXR-e","SR OS 21.10.R3","10.114.15.220")
router_inv = [rtr1, rtr2, rtr3]

for rtr in router_inv:
    print(rtr.getdesc())
    print("--------\n")

sw1 = Switch("Catalyst 3650","IOS 16.9.5","10.114.15.221")

print(sw1.getdesc())
print("--------\n")

'''Useful Modules for Infrastructure Automation

Standard Library Modules:
- pprint
- sys
- os
- datetime
- time -- add time-based delays to program
- json
- csv
- unittest

PyPI Modules:
- xmltodict
- pyyaml
- pyang - utility to validate
- requests
- ncclient
- netmiko
- pysnmp
- napalm
- nornir
- pyats

'''