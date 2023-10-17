import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
  headers = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

  api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'  
  # params = {'linkedin_profile_url': 'https://www.linkedin.com/in/ekkarat-prasongsap-3180b5114/',}

  response = requests.get(
    api_endpoint, params={"linkedin_profile_url": linkedin_profile_url}, headers=headers
  )

  data = response.json()
  data = {
    k: v
    for k, v in data.items()
    if v not in ([], '', ' ', None) and k not in ['people_also_viewed', 'certifications']
  }

  if data.get('groups'):
    for groupd_dict in data.get('groups'):
      groupd_dict.pop('profile_pic_url')
  
  return data