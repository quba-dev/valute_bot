# cost = []
#     sell = []
#     trs = soup.find('div', class_='rate-list active').find('table', class_='vl-list').find_all('td', class_='td-rate td-rate--even')
#     for i in trs:
#         b = i.find('div', class_='td-rate__wrp').text
#         cost.append(b.replace(' ','').replace('\n',''))
#     # print(trs) 
#     trs1 = soup.find('div', class_='rate-list active').find('table', class_='vl-list').find_all('td', class_='td-rate td-rate--even -last-in-group')
#     for i in trs1:
#         b = i.find('div', class_='td-rate__wrp').text
#         sell.append(b.replace(' ','').replace('\n',''))
#     print(sell)