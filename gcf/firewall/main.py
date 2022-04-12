from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
import requests
import resource
import re
import os
import base64
from curses import raw
import json
import re
import sys


def getSVC():
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    return service


def remediation_vars():
    # There are two option
    # 1. action = disable, Disable whole firewall rule
    # 2. action = replace, Replace it with trusted_ips

    doAction = os.environ.get(
        'action', 'variable `action` is not set.').strip()
    doIP = os.environ.get(
        'trusted_ips', 'variable `trusted_ips` is not set.').split(",")

    if doIP != "":
        doIP = ([[i] for i in doIP])
        print(f"Raw trusted_ips value is {doIP}")
        print(f"Converted trusted_ips value is {doIP}")

    if doAction != "disable" and doAction != "replace":
        print(f"Found Value of {doAction}")
        print("variable `action` is not set.")
        sys.exit(0)
    else:
        if doAction == "replace" and doIP == "":
            print(doIP)
            print(
                "variable `action `is set to `replace` but `trusted_ips` value not found.")
            sys.exit(0)
    return doIP, doAction


def entrypoint(event, context):

    service = getSVC()
    doIP, doAction = remediation_vars()

    resourceName, resourceProject = process_pubsub_event(
        event, context, service, doAction, doIP)

    webhook = "https://hooks.slack.com/services/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"
    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {
                        "type": "plain_text",
                        "text": "Auto Remediation Action",
                        "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Type:*\nFirewall"
                        },
                    {
                            "type": "mrkdwn",
                            "text": "*Created by:*\n66Degrees Security Bot"
                            }
                ]
            },
            {
                "type": "section",
                "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Resource Project:*\n {resourceProject}"
                        },
                    {
                            "type": "mrkdwn",
                            "text": f"*Resource Name:*\n {resourceName}"
                            }
                ]
            },
            {
                "type": "section",
                "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Action:*\n {doAction}"
                        },
                    {
                            "type": "mrkdwn",
                            "text": f"*Allowed Ports:*\n {doIP}"
                            }
                ]
            },
            {
                "type": "section",
                "text": {
                        "type": "mrkdwn",
                        "text": ":shield: Powered By 66Degrees."
                }
            }
        ]
    }
    send_slack_message(payload, webhook)
    print(f"Excuted Resource Slack Notification Request")


def process_pubsub_event(event, context, service, doAction, doIP):
    rawObject = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    resourceName = rawObject['resource']['displayName']
    resourceProject = rawObject['resource']['name']

    exp = re.compile(r"(projects\/)([\d\D]+)(\/global)")
    resourceProject = re.search(exp, resourceProject).group(2)

    print(f"Culprit Resource Found : {resourceName}")
    print(f"Culprit Resource's Project Found : {resourceProject}")

    # Get Current info of resource.
    request = service.firewalls().get(project=resourceProject, firewall=resourceName)
    response = request.execute()
    print(f"Excuted Resource Get Request : {response}")

    projectNetwork = response['network']

    # Condition to check if doIP set.
    if doAction == 'disable':
        request = service.firewalls().patch(project=resourceProject,
                                            firewall=resourceName, body={"disabled": True, "network": projectNetwork
                                                                         })
    elif doAction == 'replace':
        request = service.firewalls().patch(project=resourceProject,
                                            firewall=resourceName, body={
                                                "sourceRanges": doIP, "network": projectNetwork
                                            })
    else:
        print(doAction)
    response = request.execute()
    print(f"Excuted Resource Remediation Request : {response}")

    return resourceName, resourceProject


def send_slack_message(payload, webhook):
    """Send a Slack message to a channel via a webhook.

    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
        webhook (str): Full Slack webhook URL for your chosen channel.

    Returns:
        HTTP response code, i.e. <Response [503]>
    """
    return requests.post(webhook, json.dumps(payload))
