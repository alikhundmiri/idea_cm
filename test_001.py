from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBs-_V2cRaDtt52qiniwukofmqxfpwHCXE"
my_cse_id = "007758778882673451564:_--q0zt43pa"

def google_search(search_term, api_key, cse_id, **kwargs):
	service = build("customsearch", "v1", developerKey=api_key)
	res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	return res['items']

results = google_search(
	'top 10 tips for watch buying', my_api_key, my_cse_id, num=10)
for result in results:
	pprint.pprint(result)