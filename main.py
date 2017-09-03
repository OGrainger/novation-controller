#!/usr/bin/python
#
# Property of EHTrace
# Created by ogr
#

import sys
import requests
import json

# deploy_core_url = "https://jenkins.ehtrace.com/view/DEPLOY/job/Deploy%20Core%20Services/rssAll"
# deploy_admin_url = "https://jenkins.ehtrace.com/view/DEPLOY/job/Deploy%20Admin%20Web/rssAll"

compile_core_url = "https://jenkins.ehtrace.com/job/Core/job/Pipelined%20Core-Services/api/json"

# compile_admin_url = "https://jenkins.ehtrace.com/job/Web/job/Admin%20Web/rssAll"

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

import random
from pygame import time


# create an instance
def open_launchpad():
    lp = launchpad.Launchpad()

    if lp.Open():
        print("Launchpad S detected")
        return lp

    print("Did not find any Launchpads, retrying...")
    time.wait(1000)
    open_launchpad()


def main():
    lp = open_launchpad()
    lp.ButtonFlush()

    while 1:
        # deploy_core_feed = feedparser.parse(deploy_core_url)
        # deploy_admin_feed = feedparser.parse(deploy_admin_url)
        # compile_core_data = requests.get(compile_core_url)

        # compile_admin_feed = feedparser.parse(deploy_admin_url)

        # print("DEPLOY CORE : " + deploy_core_feed["entries"][0]["title"])
        # print("DEPLOY ADMIN WEB : " + deploy_admin_feed["entries"][0]["title"] + "\n")
        # print(json.loads(compile_core_data.content)["displayName"])
        # compile_core_isValid = json.loads(compile_core_data.content)["lastCompletedBuild"]["number"] == json.loads(compile_core_data.content)["lastSuccessfulBuild"]["number"]
        # print(json.loads(compile_core_data.content)["lastCompletedBuild"]["number"] == json.loads(compile_core_data.content)["lastUnstableBuild"]["number"])
        # print(json.loads(compile_core_data.content)["lastCompletedBuild"]["number"] == json.loads(compile_core_data.content)["lastFailedBuild"]["number"])
        # print(json.loads(compile_core_data.content)["lastFailedBuild"]["number"])
        # print("COMPILE ADMIN WEB : " + compile_admin_feed["entries"][0]["title"] + "\n")

        for i in range(0, 300):
            lp.LedCtrlRaw(i, 3, 0)
            time.wait(10)

        '''btn = lp.ButtonStateRaw()

        if btn != []:
            print(btn)
            if btn[1]:
                lp.LedCtrlRaw(btn[0], random.randint(0, 3), 3)
            else:
                lp.LedCtrlRaw(btn[0], 0, 3)'''

        time.wait(1000)


if __name__ == '__main__':
    main()
