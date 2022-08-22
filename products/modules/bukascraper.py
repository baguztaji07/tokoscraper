import requests
   
def get_token_access():
    headers = {
        'authority': 'www.bukalapak.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'browser_id=75b07e160f84863dde66e5e819f5b64b; identity=e7e8cf037d3099fa10a321fba18e6854; browser_id=49da695fdecfdedceeb5046f92a4e889; session_id=bc57722598d11ad2606a28e729703ace; nlbi_2720203=hnlJCDgZp3WyIlekaKZlFQAAAACNlZitcdWtxM5ddxR0QXrs; visid_incap_2720203=FRK7z706TtebUMzzpbssq2gT9WIAAAAAQUIPAAAAAABm2BIp/Vfa7FsT4QBzwnMi; incap_ses_7265_2720203=p7u3F3VSaXb5kfRsIHfSZGkT9WIAAAAAuMUa4JLsQDlDpt5JE+rAHw==; _gcl_au=1.1.1015849132.1660228458; _ga=GA1.2.1381763064.1660228458; _gid=GA1.2.704625322.1660228458; reese84=3:3ExPOF2XBWiGT/dpkwYwlA==:YNgOveZAfpmRRs7chfWiWA7j8nUjFNWU+LFqScYUPTnOLr0uy0/n1AGYsvn5dzRnHjGDJ4DgOfR0OCfmWxC08Qh+wY/gQY8uO/mFCQHmb3FSy9zQ4FK1IBW72yd8kufnTNc3rcdmQJ85ZPptzl9FH1OylYbXQ1RlPBpCZnTuOgW3jGYjg9uK/P113PotN1XL83rpHOUf9DChzJbIbU5tXS1FAPk2bjmapHma5C3xxLodjhKnNzgRlsPbkhZi5NH0BlRM55hiWTpvwVMPAOf8rGNHl7dOuXihqsqI8Cfksng95br3lpHI47q5pDs66EiARUrKzRL6FNo//ckYAydEiY6pYYBs3Kfznk3nvObbrYPGnlW9b0ADGLw7uQvpw92pPDy04lA9eW1ZhOQREAsT1JDTNdX8Gc75zw/uPAe0zPMWmJ9F5YLLTC1IEGPQXug2RrextGBAKGztcLEqYRLzzA==:S/RWPZTZ2ntLixICcw0cUoQ2nefEIprTPg1F+p0YMPY=; logLevel=0; vstreamID=121_751_1962663254; _tt_enable_cookie=1; _ttp=bd7e151a-6692-4de7-9443-7bc91f3ba58b; __asc=d19ec4bf1828d53de969e0c44fe; __auc=d19ec4bf1828d53de969e0c44fe; cto_bundle=Yu8j_F9lM09nbkJNNmptdlhuell3cjZwVlgwd2owMlBFcTNMUlEwMlcxRk1RUFRBT05tek5iRmklMkJYeDN0dFRsVFVtRk1aVWNOJTJGSUpJJTJGSU5aa2VXM2FhRFBRTzJkVURVcm0wUFZva204MmpKaHRlZmdrVEElMkJPdzF4a3pVa3pLaWZ0UmYw; _vid_t=fc5T+Z8WkNJdxD7EtXo1XHxFu686Ttp2RLC9F68dYXFrQLCnFot0y071QeiYcd5bxmTDPHuTIlCrwA==; _dc_gtm_UA-12425854-1=1; _ga_R2T40V5QM5=GS1.1.1660228458.1.1.1660228594.60; lskjfewjrh34ghj23brjh234=d1VXVDJTd2s1QVpubFBuQVBKQzc2c2FYZzZxbkMxQTVkVTgwY25nQXNvMlpRYzQwL2RraHFYTXJ5SzVUZ2xrdzU4QnJ5a2VMbEs3RENjWjVPR1B3M2c9PS0telN4N2tCSHAzalROOVlqRDVhcVYwZz09--8d1c314e4b59379d07396ba7ccf4a40f9703277b; nlbi_2720203_2147483392=SOFaQtLcVnODwpCzaKZlFQAAAAAKFsuvX/ut8kyWCbgljv/j; external_visit_tracker_marketplace={%22referrer%22:%22https://www.google.com/%22%2C%22url%22:%22https://www.bukalapak.com/%22%2C%22max_ages%22:%222022-08-11T15:06:53.878Z%22}; dd_cookie_test=test; _dd_s=logs=0&expire=1660229513925',
        'origin': 'https://www.bukalapak.com',
        'pragma': 'no-cache',
        'referer': 'https://www.bukalapak.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    json_data = {
        'application_id': 1,
        'authenticity_token': '',
    }

    response = requests.post('https://www.bukalapak.com/westeros_auth_proxies', headers=headers, json=json_data)
    data = response.json()
    return data['access_token']

def fetch_product_data(offset, page, token):
    response = requests.get("https://api.bukalapak.com/multistrategy-products?category_id=8&sort=bestselling&limit=30&offset="+str(offset)+"&facet=true&page="+str(page)+"&shouldUseSeoMultistrategy=false&isLoggedIn=false&show_search_contexts=true&access_token="+str(token))
    data1 = response.json()
    data2 = data1['data']
    return data2

def total_of_pages(total):
    return (total+30-1)/30

def bukalapak_main(total):
    total = int(total)
    pages = total_of_pages(total)
    pages = int(pages)
    product_datas = []
    token = get_token_access()
    
    for i in range(1,pages+1):
        product_datas += fetch_product_data(i, (i-1)*30, token)

    # deleting unnecessary data
    length = len(product_datas)
    for i in range(total,length):
        del product_datas[total]

    return product_datas
    
if __name__ == '__main__':
    bukalapak_main(41)
