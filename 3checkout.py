import requests

url = "https://www.thebodyshop.com/checkouts/cn/hWN4SuTwuQv71W345nSP0PS7/en-gb?_r=AQABSc5zg11EhJGgbPJNqqvv0cLg6zYDGu8CFgyqvibJajA"

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'cache-control': "max-age=0",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'sec-ch-ua': "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'referer': "https://www.thebodyshop.com/",
  'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
  'Cookie': "localization=GB; cart_currency=GBP; _shopify_y=ed34ca21-777b-4332-b681-b9b988e0e94a; OptanonAlertBoxClosed=2025-10-23T23:56:44.063Z; _blkp_xps=%7B%22HJSHP%22%3A85%2C%22ES%22%3A16%7D; og_session_id=b98838c587ad4238909d5510054ff336.831708.1761263807; _pk_id.4184.4209=bb3847a64b99089f.1761263815.; __kla_id=eyJjaWQiOiJNelV5TVRObE1UZ3RaV1F5TmkwME9EZGxMVGhpWVdJdE5ERTVNRFU1WkRjM00yRXgifQ==; _gcl_au=1.1.2058434329.1761263848; lantern=9f5113b7-4a42-4924-9920-48cfe189ce2f; cart=hWN4SuTwuQv71W345nSP0PS7%3Fkey%3D8eb9f8ff24353cd2e1f1952cf3de4aff; _ga=GA1.1.243745470.1761870292; _shopify_analytics=:AZo_PAXTAAEAdk7zi8TMUN6LwW9lrEEfrl_L3OHnQWjxtSVt8IEAP55N2Gbo5CGiK0mYLAA:; _pk_ref.4184.4209=%5B%22%22%2C%22%22%2C1762259956%2C%22https%3A%2F%2Fwww.thebodyshop.com%2Fcheckouts%2Fcn%2FhWN4SuTwuQv71W345nSP0PS7%2Fen-gb%22%5D; _pk_ses.4184.4209=1; _clck=e4jwgn%5E2%5Eg0q%5E1%5E2122; yotpo_pixel=1ce3d4df-7689-4073-aa63-24e60ea8808f; _sp_ses.330a=*; _aw_j_7899={\"id\":\"744169e1-dad5-47b3-96fa-9189c9909dc5-1\",\"expiration\":1770144002}; _blka_engage=%7B%7D; _clsk=1xhdxq0%5E1762261540829%5E4%5E1%5Eo.clarity.ms%2Fcollect; _ga_9X8WCXPR1Z=GS2.1.s1762259993$o4$g0$t1762261542$j60$l0$h0; _shopify_s=ee4c4af1-f8a5-4b87-825b-9dd4710e71e1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+04+2025+16%3A07%3A08+GMT%2B0300+(East+Africa+Time)&version=202510.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=0cb2e93a-149b-4082-b950-57d665675527&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=KE%3B30&AwaitingReconsent=false; __blka_ts=1762263432134; _sp_id.330a=b2b50fb4ff8d5ef8.1761263845.5.1762261686.1761997587; keep_alive=eyJ2IjoyLCJ0cyI6MTc2MjI2MTY5MjEyMSwiZW52Ijp7IndkIjowLCJ1YSI6MSwiY3YiOjEsImJyIjoxfSwiYmh2Ijp7Im1hIjoyLCJjYSI6Miwia2EiOjAsInNhIjo3LCJrYmEiOjAsInRhIjo3LCJ0Ijo3Mywibm0iOjAsIm1zIjowLCJtaiI6MCwibXNwIjowLCJ2YyI6MSwiY3AiOjAuNjksInJjIjowLCJraiI6MCwia2kiOjAsInNzIjowLjUzLCJzaiI6MC40OSwic3NtIjowLjksInNwIjoxLCJ0cyI6MC40OSwidGoiOjAuMjEsInRwIjoxLCJ0c20iOjF9LCJzZXMiOnsicCI6MiwicyI6MTc2MjI2MTUyODcyNywiZCI6MTA1fX0%3D; _shopify_essential=:AZpO-2DYAAEA4668_asILnXGOmgimKxw--2291y4LyRWLFMb4qmMbBK1j_DJXKK0zXOgyps2XbuQYfAeBHjnYFjFd6hOUd0RmOxsVMQFiyeAeHrE6GHuhTM16FSGTGMFcqqWKKdUrutK0Sxty4XF0cn93i4CLJoH7EzbYIoMBuvTMB38W1VKItaFBRuDTlcAwKn-XgCWMGYB-QFBxCRQkdyaKFJW7v2fUqWX1n8dY4_dYbsnDrEbrzHQWtgqeJzq2oNwahtjcpsN_kgquw9x8dMomCOSdtyHLmsSMZMj4EFXauhnSxU4lX3FoU6BY41qR_Bx6EpHJMoqD3250aZclMnpe6sA7DoqJLeIILLxNXUdf75jtLcMorf3o-pcVmislZF2xUmV6fWfUxRraM2vaBEXYf1D1xbJmtPRTy1Pb0ZSRI_9q1LlS8ROSN7mzWCb4E1ZsHNVpgJTywBekP0yNfPblpfKwGOts90_aSzf3_7FLY9AnQB5L8JuwsCsUjU8SJJVfmEK34xNJsj66ZO1wDDKmaQNxsdXVkhuESG-_hHRFUbo-p_HIdXgSlm2L_GAwx7ZgBpW_7LblQdquFwN7bGqetSxmUPw7qyfT_80t1E-A6gMtvVBKhXl41QdwCagTHNXhV0TdprVmXE3QkOMZZ1dgBkjizaSUZ2U4W1xdqo2OenPGSE30oBlYLF3TvPSvl000eRm_dK8hiPu4JcFvFz3RHDeCjKUgqA47Dvo_CwH_JfTc2Y2rJ3SuxSCQWieH-usjZxfQrMGvA:"
}

response = requests.get(url, headers=headers)

print(response.text)