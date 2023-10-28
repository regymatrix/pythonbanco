#site https://curlconverter.com/python/

import requests
from bs4 import BeautifulSoup

cookies = {
    'AUTH_SESSION_ID': '8e828b90-d4e0-4483-92e3-bb8db1596345.ip-10-11-46-185-31401',
    'AUTH_SESSION_ID_LEGACY': '8e828b90-d4e0-4483-92e3-bb8db1596345.ip-10-11-46-185-31401',
    'KC_RESTART': 'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Y2Q2MTU0Ny00NjM5LTRhMjQtODM1Mi0yODdhYjI3Y2E3N2QifQ.eyJjaWQiOiJzcGEtY29yZS1jbGllbnQiLCJwdHkiOiJvcGVuaWQtY29ubmVjdCIsInJ1cmkiOiJodHRwczovL3dlYi5kaW8ubWUvIiwiYWN0IjoiQVVUSEVOVElDQVRFIiwibm90ZXMiOnsic2NvcGUiOiJvcGVuaWQiLCJpc3MiOiJodHRwczovL2F1dGguZGlvLm1lL3JlYWxtcy9tYXN0ZXIiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vd2ViLmRpby5tZS8iLCJzdGF0ZSI6IjRiOTg1OGVmLTY3MjItNDBjZS04MWRjLTQ5ZWRmNzhlNzNlMiIsIm5vbmNlIjoiNjcxOTgwZWQtMzFhNS00MjU4LTgyOWUtY2ZlZWY2NTQwZGI2IiwicmVzcG9uc2VfbW9kZSI6ImZyYWdtZW50In19.9WBlTVS4YlcJVEN1B9RTIUycHZtVm48myBOY9sHcpfI',
    '_hjSessionUser_1255605': 'eyJpZCI6IjkwMzAxYTk2LTVkNTMtNWQ5OS05YzlkLTg4M2RjM2M0OTU0YyIsImNyZWF0ZWQiOjE2NTI0ODE3ODUzNjQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSessionUser_2850119': 'eyJpZCI6IjVlZWU0NDJkLWNhODItNTJmMy1iZWIzLTFmZGZkZWYzOGMxMiIsImNyZWF0ZWQiOjE2NTI0OTMyODcwMzksImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSessionUser_2953130': 'eyJpZCI6ImFmY2I5M2I2LTBlMGEtNTJmNC04MTQ2LTAwZDIyMzFjOTdmOCIsImNyZWF0ZWQiOjE2NTYzNzAzMTk1OTYsImV4aXN0aW5nIjp0cnVlfQ==',
    '_tt_enable_cookie': '1',
    '_ttp': 'o8P9fw28OL74Aaw9FMVv5CSap2N',
    'ajs_user_id': 'ca7cd231-46f5-423a-97fb-62901d648480',
    'ajs_anonymous_id': '53b722b9-96b7-44a3-9f8d-6310eb548a49',
    '_gcl_au': '1.1.1686074729.1693743106',
    '_fbp': 'fb.1.1693743107080.447993567',
    'prism_475833027': 'a3f686d6-1db8-41c8-af83-a47fa6b8efa8',
    'amplitude_idundefineddio.me': 'eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==',
    '_gid': 'GA1.2.985349343.1697902188',
    '_clck': '866jhj|2|fg1|0|1341',
    '_hjAbsoluteSessionInProgress': '1',
    '_hjSession_1255605': 'eyJpZCI6IjRkYWNiNGMzLTk4ODUtNGUzMS1hNTk2LTcxY2NlOWNlYmZjOCIsImNyZWF0ZWQiOjE2OTc5MDY4OTQwNjksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
    'amplitude_id_07386cdc4cb0623b4e371aa5df50cc90dio.me': 'eyJkZXZpY2VJZCI6ImYxZDdiOTM5LTgyZjYtNGYwOC04MGFmLTRkYjlkM2E0Y2I5MVIiLCJ1c2VySWQiOiJjYTdjZDIzMS00NmY1LTQyM2EtOTdmYi02MjkwMWQ2NDg0ODAiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2OTc5MDUwMjgyMTcsImxhc3RFdmVudFRpbWUiOjE2OTc5MDY4OTQ1MTMsImV2ZW50SWQiOjc0NSwiaWRlbnRpZnlJZCI6MzgsInNlcXVlbmNlTnVtYmVyIjo3ODN9',
    '_clsk': '10oq0ln|1697906895053|4|1|y.clarity.ms/collect',
    '_ga_7GXMH3CQ72': 'GS1.1.1697905015.69.1.1697907035.60.0.0',
    '_ga': 'GA1.2.1830271403.1676073314',
    '_uetsid': 'abd9cbe0702611ee9a4da1ad434bdf4f',
    '_uetvid': '0f1b49004a5311ee84990dfae13b3de0',
    '_ga_04PN3J998S': 'GS1.2.1697905015.62.1.1697907036.60.0.0',
}

headers = {
    'authority': 'auth.dio.me',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'AUTH_SESSION_ID=8e828b90-d4e0-4483-92e3-bb8db1596345.ip-10-11-46-185-31401; AUTH_SESSION_ID_LEGACY=8e828b90-d4e0-4483-92e3-bb8db1596345.ip-10-11-46-185-31401; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Y2Q2MTU0Ny00NjM5LTRhMjQtODM1Mi0yODdhYjI3Y2E3N2QifQ.eyJjaWQiOiJzcGEtY29yZS1jbGllbnQiLCJwdHkiOiJvcGVuaWQtY29ubmVjdCIsInJ1cmkiOiJodHRwczovL3dlYi5kaW8ubWUvIiwiYWN0IjoiQVVUSEVOVElDQVRFIiwibm90ZXMiOnsic2NvcGUiOiJvcGVuaWQiLCJpc3MiOiJodHRwczovL2F1dGguZGlvLm1lL3JlYWxtcy9tYXN0ZXIiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vd2ViLmRpby5tZS8iLCJzdGF0ZSI6IjRiOTg1OGVmLTY3MjItNDBjZS04MWRjLTQ5ZWRmNzhlNzNlMiIsIm5vbmNlIjoiNjcxOTgwZWQtMzFhNS00MjU4LTgyOWUtY2ZlZWY2NTQwZGI2IiwicmVzcG9uc2VfbW9kZSI6ImZyYWdtZW50In19.9WBlTVS4YlcJVEN1B9RTIUycHZtVm48myBOY9sHcpfI; _hjSessionUser_1255605=eyJpZCI6IjkwMzAxYTk2LTVkNTMtNWQ5OS05YzlkLTg4M2RjM2M0OTU0YyIsImNyZWF0ZWQiOjE2NTI0ODE3ODUzNjQsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2850119=eyJpZCI6IjVlZWU0NDJkLWNhODItNTJmMy1iZWIzLTFmZGZkZWYzOGMxMiIsImNyZWF0ZWQiOjE2NTI0OTMyODcwMzksImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2953130=eyJpZCI6ImFmY2I5M2I2LTBlMGEtNTJmNC04MTQ2LTAwZDIyMzFjOTdmOCIsImNyZWF0ZWQiOjE2NTYzNzAzMTk1OTYsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=o8P9fw28OL74Aaw9FMVv5CSap2N; ajs_user_id=ca7cd231-46f5-423a-97fb-62901d648480; ajs_anonymous_id=53b722b9-96b7-44a3-9f8d-6310eb548a49; _gcl_au=1.1.1686074729.1693743106; _fbp=fb.1.1693743107080.447993567; prism_475833027=a3f686d6-1db8-41c8-af83-a47fa6b8efa8; amplitude_idundefineddio.me=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _gid=GA1.2.985349343.1697902188; _clck=866jhj|2|fg1|0|1341; _hjAbsoluteSessionInProgress=1; _hjSession_1255605=eyJpZCI6IjRkYWNiNGMzLTk4ODUtNGUzMS1hNTk2LTcxY2NlOWNlYmZjOCIsImNyZWF0ZWQiOjE2OTc5MDY4OTQwNjksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; amplitude_id_07386cdc4cb0623b4e371aa5df50cc90dio.me=eyJkZXZpY2VJZCI6ImYxZDdiOTM5LTgyZjYtNGYwOC04MGFmLTRkYjlkM2E0Y2I5MVIiLCJ1c2VySWQiOiJjYTdjZDIzMS00NmY1LTQyM2EtOTdmYi02MjkwMWQ2NDg0ODAiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2OTc5MDUwMjgyMTcsImxhc3RFdmVudFRpbWUiOjE2OTc5MDY4OTQ1MTMsImV2ZW50SWQiOjc0NSwiaWRlbnRpZnlJZCI6MzgsInNlcXVlbmNlTnVtYmVyIjo3ODN9; _clsk=10oq0ln|1697906895053|4|1|y.clarity.ms/collect; _ga_7GXMH3CQ72=GS1.1.1697905015.69.1.1697907035.60.0.0; _ga=GA1.2.1830271403.1676073314; _uetsid=abd9cbe0702611ee9a4da1ad434bdf4f; _uetvid=0f1b49004a5311ee84990dfae13b3de0; _ga_04PN3J998S=GS1.2.1697905015.62.1.1697907036.60.0.0',
    'origin': 'null',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    'session_code': 'tOUir7ZP-3jE8zkXhgtjSEklQifEV1Xn8GnTTK3lPrk',
    'execution': '1ecc3b57-7fd0-47a5-921c-ba3f9c445fc5',
    'client_id': 'spa-core-client',
    'tab_id': 'EpZOlSDTvJ8',
}

data = {
    'username': 'regymatrix@gmail.com',
    'password': 'acesso1',
    'credentialId': '',
}

response = requests.post(
    'https://auth.dio.me/realms/master/login-actions/authenticate',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

with requests.session() as s:
    login_url ='https://auth.dio.me/'
    r=s.get(login_url)
    soup = BeautifulSoup(r.text,'html.parser')
    token = soup