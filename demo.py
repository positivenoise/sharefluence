import requests

from atlassian import Confluence
from requests_ntlm import HttpNtlmAuth

SITE = ""
PASSWORD = ""
USERNAME = ""

confluence = Confluence(
    url='',
    username=USERNAME[5:],
    password=PASSWORD)

#Check to see if Sharepoint connection works. Returns 200 OK if OK
#response = requests.get(SITE, auth=HttpNtlmAuth(USERNAME,PASSWORD))
#print(response.status_code)

#Runs a search for sharepoint, prints text
#response = requests.get("http://intranet/_api/search/query?querytext='sharepoint'", auth=HttpNtlmAuth(USERNAME,PASSWORD))
#print(response.text)

#Returns all networking pages
#results = confluence.get_all_pages_from_space("NET", start=0, limit=500)
#confluence.page_exists("Networking", "Cisco Networking")
#print(results)

#Search using cql
#cql = "text ~ \"hello\""
#results = confluence.cql(cql, start=0, limit=None, expand=None, include_archived_spaces=None, excerpt=None)
#print(results)