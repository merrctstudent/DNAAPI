# Script to grab an Auth token from CIsco DNA and use the token to request Site Topology#
import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth
from pprint import pprint

# Prompts for username and password and stores as variables#
DNACUSER = input("Please enter your DNAC Username: ")
DNACPASS = getpass("Please enter your DNAC Password: ")

# Specifies headers and payload for http post#
payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# Cisco always on sandbox and request for token appended#
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

# Post using User provided input as username and password#
response = requests.post(url, auth=HTTPBasicAuth(DNACUSER,DNACPASS), headers=headers, data=payload)

# Takes response, grabs token and stores as a variable#
DNACToken = response.json()

authtoken = DNACToken['Token']

# Cisco always on sandbox and get request for site topology API call#
Sitetopologyurl = "https://sandboxdnac.cisco.com/dna/intent/api/v1/topology/site-topology"

# Specifies headers and payload for get request#
payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-auth-token': authtoken
}

# Requests using specified values for Site Topology#
SITETOPresponse = requests.get(Sitetopologyurl, headers=headers, data=payload)
Sitetop = SITETOPresponse.json()

# pretty Prints the Response from Site Topolgy API request#
pprint(Sitetop)
