import requests

url = "https://www.thebodyshop.com/cart/add"

payload = {
  'options[Size]-api-product-upsellproduct-9282926379273-': '60ml',
  'form_type': 'product',
  'utf8': '✓',
  'quantity': '1',
  'product-id': '9282926379273',
  'section-id': 'api-product-upsell',
  'id': '48426679927049'
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
  'Accept': "application/javascript",
  'sec-ch-ua': "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://www.thebodyshop.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.thebodyshop.com/",
  'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
  'Cookie': "localization=GB; cart_currency=GBP; _shopify_y=ed34ca21-777b-4332-b681-b9b988e0e94a; OptanonAlertBoxClosed=2025-10-23T23:56:44.063Z; _blkp_xps=%7B%22HJSHP%22%3A85%2C%22ES%22%3A16%7D; og_session_id=b98838c587ad4238909d5510054ff336.831708.1761263807; _pk_id.4184.4209=bb3847a64b99089f.1761263815.; __kla_id=eyJjaWQiOiJNelV5TVRObE1UZ3RaV1F5TmkwME9EZGxMVGhpWVdJdE5ERTVNRFU1WkRjM00yRXgifQ==; _gcl_au=1.1.2058434329.1761263848; lantern=9f5113b7-4a42-4924-9920-48cfe189ce2f; cart=hWN4SuTwuQv71W345nSP0PS7%3Fkey%3D8eb9f8ff24353cd2e1f1952cf3de4aff; _ga=GA1.1.243745470.1761870292; _shopify_analytics=:AZo_PAXTAAEAdk7zi8TMUN6LwW9lrEEfrl_L3OHnQWjxtSVt8IEAP55N2Gbo5CGiK0mYLAA:; _pk_ref.4184.4209=%5B%22%22%2C%22%22%2C1762259956%2C%22https%3A%2F%2Fwww.thebodyshop.com%2Fcheckouts%2Fcn%2FhWN4SuTwuQv71W345nSP0PS7%2Fen-gb%22%5D; _pk_ses.4184.4209=1; _blka_engage=%7B%7D; _clck=e4jwgn%5E2%5Eg0q%5E1%5E2122; yotpo_pixel=1ce3d4df-7689-4073-aa63-24e60ea8808f; _sp_ses.330a=*; _ga_9X8WCXPR1Z=GS2.1.s1762259993$o4$g0$t1762259993$j60$l0$h0; _aw_j_7899={\"id\":\"744169e1-dad5-47b3-96fa-9189c9909dc5-1\",\"expiration\":1770144002}; _shopify_essential=:AZpO62gKAAEAgOy9yWlyuYpEa2hZpJm9Rbtg2Jn8os3TtG9arAR7DDAtEo7YE361qtFe1WsuXfskrxLZzak-67ldWHqxhX6awlgMOVCYhuIvnePooanz3yq4UWoo0YWCaQlwofbaURi1GqkA48TyhRws1sLCiaPkCN3rhalXM5dMGII4HWxflLE16wMShoa1lEbeyYarS26jpwtOHHOoLIVeepx92NP5cMNic2NFWLAo5cuaDz6Olsc6Nr7q2Xiu5nCdq7e5eRZb3LrryFZXvjVqtrmtQw41q8NDTU_DsQc0CDakIDjKYLH7alGBLgsRicX981YG0ZJ7_Jb5WGcSucudK8pyC2-3KKBilxgcZDCfx5QOK3LcW-ap0oQWOQaPxCz0BVswqLLxaRcAcVN_mLY7fTwx5TeOUXFkbGBeO-0ru314F4RgC64Qz0zrsfLv6F8SREKp-2uO_74H7gL1FW8cP-qpyxVyqksxz07l_uHHn90IKPDe-jxVGoGswdE-WUtiVPBsbeCzFaFwn2sBUbszxMJ3kNeROfkU1Nm6_AQKko8ry0VYiYPSBXmFMi8KkPI8YfurUEr-0RlYuasl7W5e-jI9-lPLH6o3vaB1SupO6uopAnLpKgHxdNntgyx_Ug2yharb7BgFb2FAF-wn2P2Y5RbyRAjCbc6HikIX-QfxaFT7e2-oofarFfJT-rgoUMGO4MLT47FQF-uSGJgMty99VsgeTqTvtAuE8BwaJQB6iHymQWZGgD_shep9BJUl9bsq1iGMiA:; _shopify_s=ee4c4af1-f8a5-4b87-825b-9dd4710e71e1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+04+2025+15%3A51%3A45+GMT%2B0300+(East+Africa+Time)&version=202510.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=0cb2e93a-149b-4082-b950-57d665675527&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=KE%3B30&AwaitingReconsent=false; __blka_ts=1762262512729; _clsk=1xhdxq0%5E1762260731461%5E3%5E1%5Eo.clarity.ms%2Fcollect; _sp_id.330a=b2b50fb4ff8d5ef8.1761263845.5.1762260764.1761997587; keep_alive=eyJ2IjoyLCJ0cyI6MTc2MjI2MDc2OTEzMywiZW52Ijp7IndkIjowLCJ1YSI6MSwiY3YiOjEsImJyIjoxfSwiYmh2Ijp7Im1hIjoxLCJjYSI6MSwia2EiOjAsInNhIjowLCJrYmEiOjAsInRhIjoyLCJ0Ijo2NSwibm0iOjAsIm1zIjowLCJtaiI6MCwibXNwIjowLCJ2YyI6MCwiY3AiOjAsInJjIjowLCJraiI6MCwia2kiOjAsInNzIjowLCJzaiI6MCwic3NtIjowLCJzcCI6MCwidHMiOjAuNDksInRqIjowLjU3LCJ0cCI6MCwidHNtIjoxfSwic2VzIjp7InAiOjQsInMiOjE3NjIyNTk5NTQwNzYsImQiOjY5Nn19"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)