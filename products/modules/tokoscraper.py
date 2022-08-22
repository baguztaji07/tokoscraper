import requests

def fetch_product_data(page, start, total):
    # print('page= ',page,' start= ',start,' total= ',total)
    cookies = {
        'bm_sz': 'EA6FBA10C92C14CC0C70D7608FA9AFA8~YAAQxVN9cufVR1yCAQAA1W7gYhDfnU9Zjg4LOjOQOu61AapnWBhhPs/MP9zNH7O/zSK2b3Mmc0thFQD9+BD0LJKlSokU+tbbNCjteIu7O1+t42CJzEZyvPg8BmyZkMm3e241K6ILI66kkIUcjX1GLcqep08jXIqD35N7XUkpdL9FWijWFeloDc3lJJX8zOrmNQYWonxKWTmrzafXv4EwYW9XVbhlb9pFU19RS4YoFoqeTZwBuKaNMvEYK2+ZmWXuGPbqRdhVxeSJ6I1wlH7XAnyAWcHtm8rDKZoygh3+zogD5XXIKb0=~3682869~4338482',
        '_SID_Tokopedia_': 'nknH76K5L6oxwKYWCTcrYLhrWmkMozZAVrkDB31g-D4_uzjhlKtVRxrrsZUz3VkBLSbSxyvNfqOeGghtAzxMncF8f7IgMS8_olRKl8D6CbEvaTaXE-9dNbLevn7o6acN',
        'DID': '31dca0776593753c594412fe0011d00a2ad6c4f8814ecb2a07f08026612cdd385f6c413b2f4772a1da316880202afd1d',
        'DID_JS': 'MzFkY2EwNzc2NTkzNzUzYzU5NDQxMmZlMDAxMWQwMGEyYWQ2YzRmODgxNGVjYjJhMDdmMDgwMjY2MTJjZGQzODVmNmM0MTNiMmY0NzcyYTFkYTMxNjg4MDIwMmFmZDFk47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=',
        '_UUID_NONLOGIN_': '0aedd0d64bf064b34c347a0f7694f7a1',
        '_gcl_au': '1.1.765602541.1659516251',
        'ak_bmsc': '743A34DCF0535858873A678D9F4BC135~000000000000000000000000000000~YAAQxVN9cvjVR1yCAQAAC3LgYhAeo/0t8LKgtqsIZ+fS6oFJh1TQpLKqQ1MgZTt0mJmJ+CGKC7edGgv26rs/hC7/jumtmRZTgiQmJ5LtB7Tzs+xxLZHim10T+2gJAJpF2++bkkj8Pb9Y3H5jLG0nJvDNA0RXGvq9sGM/M5cyqkl7WyZxnHzKUo01nCxP2jc2+/g4vPvJMsCn7qZ5M2z9z2ZH1fex7w/zDORNeCefnhkzIHu3MKm4jbuFARYHh/j7HYJJngmPxSrglRUvfML60/uKqGPq76ir0EwEnlSOqqgjiRhmCqX1uJZ24laE3FSuHnPN0PjZ0V8/0ttua8vjMlzHSGzeehXpF1wZXugrJDnAAcKuaZ15yC3nYYikFhMKLTkbRiu/JNuqTCpWhaDNA0TM2T5SQWWgP9ao8DMu3egd3IWvGKlKlRKAhRKHy4hONOEuLbZTbnIHAlYFn9hGIu9D46C0EueB1qO7d8g/0JAJ/8FZOT9ibz2P/Rfi',
        '_gid': 'GA1.2.1023631153.1659516251',
        '_dc_gtm_UA-126956641-6': '1',
        '_abck': '554E997680C404E944CE2CE5ECBBBA55~0~YAAQxVN9cvzVR1yCAQAAHXPgYghWnaNfl98FIMf6tqQLebswE1TmDbeGwEkVaZOT5hC05Nn0jBi8zch8LWe94psxC+mu2krCjRMoFBC/RMwk0JGQE7uy8BElFDsvUpS4ZHMpeTmZwM88DlA260MRIx9XCwv4DAechNyAaBPObD4JssNfuXdpqKx1p7zvlDMUyrzYAerUXJFMAwlFW8LIidx0vwFXXYn9vD1pcu5YwAO1yUJoSOoHsrYsEnb6f3Oq7y9DzU3BO52deanBtVrjc0NLs/RM7oWBZkNFRB7Tqh3z2cMkQtGB0nj1wzpVuXCQe1nZ4nKB804uVlTzYlKi1AXPB0kg/cczxrrYTuq+BQw2N91xMZbmX029jwD7YQrQ/qUTUG4WPaA8OmnyxNvqhph4HJ0n+bN/O6ic~-1~-1~-1',
        '_dc_gtm_UA-9801603-1': '1',
        '_jxxs': '1659516254-73cfae90-1308-11ed-ae5a-77307b398ccd',
        '_jxx': '73cfae90-1308-11ed-ae5a-77307b398ccd',
        '_jx': '73cfae90-1308-11ed-ae5a-77307b398ccd',
        '_jxs': '1659516254-73cfae90-1308-11ed-ae5a-77307b398ccd',
        'hfv_banner': 'true',
        '_UUID_CAS_': '76bf600e-7f83-4c3b-961d-9043c85e2016',
        '_CASE_': '2b72341934726a626267647c72311934726a607c723c323c726a721a313b31222431700025233124727c72331934726a6167667c723c3f3e37726a72727c723c3124726a72727c7220133f726a72727c72271934726a61626261606367657c72231934726a61616563606567637c722304292035726a726238727c72273823726a720b2b0c7227312235383f2523350f39340c726a61626261606367657c0c72233522263933350f242920350c726a0c7262380c727c0c720f0f242920353e313d350c726a0c7207312235383f252335230c722d7c2b0c7227312235383f2523350f39340c726a607c0c72233522263933350f242920350c726a0c7261653d0c727c0c720f0f242920353e313d350c726a0c7207312235383f252335230c722d0d722d',
        '__asc': '57b0eb6918262e080b72ffc1e59',
        '__auc': '57b0eb6918262e080b72ffc1e59',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_gat_UA-9801603-1': '1',
        '_ga': 'GA1.2.2022022964.1659516251',
        '_ga_70947XW48P': 'GS1.1.1659516251.1.1.1659516299.12',
    }

    headers = {
        'authority': 'gql.tokopedia.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'bm_sz=EA6FBA10C92C14CC0C70D7608FA9AFA8~YAAQxVN9cufVR1yCAQAA1W7gYhDfnU9Zjg4LOjOQOu61AapnWBhhPs/MP9zNH7O/zSK2b3Mmc0thFQD9+BD0LJKlSokU+tbbNCjteIu7O1+t42CJzEZyvPg8BmyZkMm3e241K6ILI66kkIUcjX1GLcqep08jXIqD35N7XUkpdL9FWijWFeloDc3lJJX8zOrmNQYWonxKWTmrzafXv4EwYW9XVbhlb9pFU19RS4YoFoqeTZwBuKaNMvEYK2+ZmWXuGPbqRdhVxeSJ6I1wlH7XAnyAWcHtm8rDKZoygh3+zogD5XXIKb0=~3682869~4338482; _SID_Tokopedia_=nknH76K5L6oxwKYWCTcrYLhrWmkMozZAVrkDB31g-D4_uzjhlKtVRxrrsZUz3VkBLSbSxyvNfqOeGghtAzxMncF8f7IgMS8_olRKl8D6CbEvaTaXE-9dNbLevn7o6acN; DID=31dca0776593753c594412fe0011d00a2ad6c4f8814ecb2a07f08026612cdd385f6c413b2f4772a1da316880202afd1d; DID_JS=MzFkY2EwNzc2NTkzNzUzYzU5NDQxMmZlMDAxMWQwMGEyYWQ2YzRmODgxNGVjYjJhMDdmMDgwMjY2MTJjZGQzODVmNmM0MTNiMmY0NzcyYTFkYTMxNjg4MDIwMmFmZDFk47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _UUID_NONLOGIN_=0aedd0d64bf064b34c347a0f7694f7a1; _gcl_au=1.1.765602541.1659516251; ak_bmsc=743A34DCF0535858873A678D9F4BC135~000000000000000000000000000000~YAAQxVN9cvjVR1yCAQAAC3LgYhAeo/0t8LKgtqsIZ+fS6oFJh1TQpLKqQ1MgZTt0mJmJ+CGKC7edGgv26rs/hC7/jumtmRZTgiQmJ5LtB7Tzs+xxLZHim10T+2gJAJpF2++bkkj8Pb9Y3H5jLG0nJvDNA0RXGvq9sGM/M5cyqkl7WyZxnHzKUo01nCxP2jc2+/g4vPvJMsCn7qZ5M2z9z2ZH1fex7w/zDORNeCefnhkzIHu3MKm4jbuFARYHh/j7HYJJngmPxSrglRUvfML60/uKqGPq76ir0EwEnlSOqqgjiRhmCqX1uJZ24laE3FSuHnPN0PjZ0V8/0ttua8vjMlzHSGzeehXpF1wZXugrJDnAAcKuaZ15yC3nYYikFhMKLTkbRiu/JNuqTCpWhaDNA0TM2T5SQWWgP9ao8DMu3egd3IWvGKlKlRKAhRKHy4hONOEuLbZTbnIHAlYFn9hGIu9D46C0EueB1qO7d8g/0JAJ/8FZOT9ibz2P/Rfi; _gid=GA1.2.1023631153.1659516251; _dc_gtm_UA-126956641-6=1; _abck=554E997680C404E944CE2CE5ECBBBA55~0~YAAQxVN9cvzVR1yCAQAAHXPgYghWnaNfl98FIMf6tqQLebswE1TmDbeGwEkVaZOT5hC05Nn0jBi8zch8LWe94psxC+mu2krCjRMoFBC/RMwk0JGQE7uy8BElFDsvUpS4ZHMpeTmZwM88DlA260MRIx9XCwv4DAechNyAaBPObD4JssNfuXdpqKx1p7zvlDMUyrzYAerUXJFMAwlFW8LIidx0vwFXXYn9vD1pcu5YwAO1yUJoSOoHsrYsEnb6f3Oq7y9DzU3BO52deanBtVrjc0NLs/RM7oWBZkNFRB7Tqh3z2cMkQtGB0nj1wzpVuXCQe1nZ4nKB804uVlTzYlKi1AXPB0kg/cczxrrYTuq+BQw2N91xMZbmX029jwD7YQrQ/qUTUG4WPaA8OmnyxNvqhph4HJ0n+bN/O6ic~-1~-1~-1; _dc_gtm_UA-9801603-1=1; _jxxs=1659516254-73cfae90-1308-11ed-ae5a-77307b398ccd; _jxx=73cfae90-1308-11ed-ae5a-77307b398ccd; _jx=73cfae90-1308-11ed-ae5a-77307b398ccd; _jxs=1659516254-73cfae90-1308-11ed-ae5a-77307b398ccd; hfv_banner=true; _UUID_CAS_=76bf600e-7f83-4c3b-961d-9043c85e2016; _CASE_=2b72341934726a626267647c72311934726a607c723c323c726a721a313b31222431700025233124727c72331934726a6167667c723c3f3e37726a72727c723c3124726a72727c7220133f726a72727c72271934726a61626261606367657c72231934726a61616563606567637c722304292035726a726238727c72273823726a720b2b0c7227312235383f2523350f39340c726a61626261606367657c0c72233522263933350f242920350c726a0c7262380c727c0c720f0f242920353e313d350c726a0c7207312235383f252335230c722d7c2b0c7227312235383f2523350f39340c726a607c0c72233522263933350f242920350c726a0c7261653d0c727c0c720f0f242920353e313d350c726a0c7207312235383f252335230c722d0d722d; __asc=57b0eb6918262e080b72ffc1e59; __auc=57b0eb6918262e080b72ffc1e59; AMP_TOKEN=%24NOT_FOUND; _gat_UA-9801603-1=1; _ga=GA1.2.2022022964.1659516251; _ga_70947XW48P=GS1.1.1659516251.1.1.1659516299.12',
        'iris_session_id': 'd3d3LnRva29wZWRpYS5jb20=.b341fecf45fcc4ed5afeb52b6926e542.1659516251165',
        'origin': 'https://www.tokopedia.com',
        'pragma': 'no-cache',
        'referer': 'https://www.tokopedia.com/p/handphone-tablet/handphone?page='+str(page),
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'tkpd-userid': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-device': 'desktop-0.0',
        'x-source': 'tokopedia-lite',
        'x-tkpd-lite-service': 'zeus',
        'x-version': '81d205c',
    }

    json_data = [
        {
            'operationName': 'SearchProductQuery',
            'variables': {
                'params': 'page='+str(page)+'&ob=&identifier=handphone-tablet_handphone&sc=24&user_id=0&rows='+str(total)+'&start='+str(start)+'&source=directory&device=desktop&page='+str(page)+'&related=true&st=product&safe_search=false',
                'adParams': 'page='+str(page)+'&page='+str(page)+'&dep_id=24&ob=&ep=product&item=15&src=directory&device=desktop&user_id=0&minimum_item=15&start=1&no_autofill_range=5-14',
            },
            'query': 'query SearchProductQuery($params: String, $adParams: String) {  CategoryProducts: searchProduct(params: $params) {    count    data: products {      id      url      imageUrl: image_url      imageUrlLarge: image_url_700      catId: category_id      gaKey: ga_key      countReview: count_review      discountPercentage: discount_percentage      preorder: is_preorder      name      price      original_price      rating      wishlist      labels {        title        color        __typename      }      badges {        imageUrl: image_url        show        __typename      }      shop {        id        url        name        goldmerchant: is_power_badge        official: is_official        reputation        clover        location        __typename      }      labelGroups: label_groups {        position        title        type        __typename      }      __typename    }    __typename  }  displayAdsV3(displayParams: $adParams) {    data {      id      ad_ref_key      redirect      sticker_id      sticker_image      productWishListUrl: product_wishlist_url      clickTrackUrl: product_click_url      shop_click_url      product {        id        name        wishlist        image {          imageUrl: s_ecs          trackerImageUrl: s_url          __typename        }        url: uri        relative_uri        price: price_format        campaign {          original_price          discountPercentage: discount_percentage          __typename        }        wholeSalePrice: wholesale_price {          quantityMin: quantity_min_format          quantityMax: quantity_max_format          price: price_format          __typename        }        count_talk_format        countReview: count_review_format        category {          id          __typename        }        preorder: product_preorder        product_wholesale        free_return        isNewProduct: product_new_label        cashback: product_cashback_rate        rating: product_rating        top_label        bottomLabel: bottom_label        __typename      }      shop {        image_product {          image_url          __typename        }        id        name        domain        location        city        tagline        goldmerchant: gold_shop        gold_shop_badge        official: shop_is_official        lucky_shop        uri        owner_id        is_owner        badges {          title          image_url          show          __typename        }        __typename      }      applinks      __typename    }    template {      isAd: is_ad      __typename    }    __typename  }}',
        },
    ]

    response = requests.post('https://gql.tokopedia.com/graphql/SearchProductQuery', cookies=cookies, headers=headers, json=json_data)
    arr_data = response.json()
    first_arr_data = arr_data[0]
    data_json = first_arr_data['data']
    cat_product_json = data_json['CategoryProducts']
    arr_data2 = cat_product_json['data']
    return arr_data2

def fetch_product_description(url):
    referer = extract_desc_key(url)
    cookies = {
        '_UUID_NONLOGIN_': '3d8330ac7ee9c90acdacff8fb7a416de',
        '_UUID_NONLOGIN_.sig': 'RhOoWHzSduY2Srfd25ueRRStRIU',
        'DID': '02c6b8bded583e28b704b24f591e7c09ae7d66080f8d0f14be8ca9e31dd2ab952fa168829805a9becf7dfd65b16035a1',
        'DID_JS': 'MDJjNmI4YmRlZDU4M2UyOGI3MDRiMjRmNTkxZTdjMDlhZTdkNjYwODBmOGQwZjE0YmU4Y2E5ZTMxZGQyYWI5NTJmYTE2ODgyOTgwNWE5YmVjZjdkZmQ2NWIxNjAzNWEx47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=',
        '_gcl_au': '1.1.1525942349.1655650355',
        '_UUID_CAS_': 'b496183c-3ccc-4b4b-a86a-90e05d6d7dc6',
        '__auc': 'fc273a2c1817c739b3fe834320d',
        'g_yolo_production': '1',
        '_hjSessionUser_714968': 'eyJpZCI6ImRmNjk0OGU0LTllODktNWJiNS1iY2NmLWEwZTM1YzQwZjNlZSIsImNyZWF0ZWQiOjE2NTU2NTAzNjM2MTMsImV4aXN0aW5nIjpmYWxzZX0=',
        '_jxx': 'c6fce740-fa30-11ec-a264-c3172eb5e9ad',
        '_jx': 'c6fce740-fa30-11ec-a264-c3172eb5e9ad',
        'NR_SID': 'NRl6gtd1z2r7u59b',
        'bm_sz': '4047C53FD3EB4004E790AD060405899E~YAAQxGjBFyZ+tniCAQAAT0MDghBTsYYY+tYgwpiUmjW77jCWhUvqjL5l12tBJEYDzTgmlCxjzxy5zXcGuj1AOv7xuSJeCdImGvNcrUl5vV4NghP1cqClgXZ1//MIvKqP3V100+gzwIwgRfF7V5SEhNYkj16fRus460hFRPHNEfJtQNEMpmvyjB3Dkno0K4LEJ0eKxCI99mO5ToaGJwxFD2MdCvRpl0bAZHLzwE5HX2auiwmtjcOkWYR0bTt0BXUg7nvh+sb3uh2Xi3mvXjfW++FzQ6u+fdgls4hkixe61kNdBrpaZFo=~3289141~3159089',
        '_gid': 'GA1.2.1961356172.1660048261',
        'ak_bmsc': '6C24A046573D614E2BFA61C4A25EE2BE~000000000000000000000000000000~YAAQDopRaFViNEeCAQAAP0iWghBF/Mf8TOtbXqGtHWV7HSOLOvj8coDl1I/Wa6fyv19T8iFVhEyaNIlCdFTOlv2NZcDN54CqqMQUUoJ2MViATT1B/OXMBvdS2vqVBUuHXKcjHg0tncxDtexjyTdYq/XLVosLd42rlWBKdUoKkmxnA9zzNlVm81esQk4AdJ3RBOK9rOEnAcXs0YNpvQzmM0g3pq5Kl4IdZwg1ZIYs7MuHZ2zwvYxWzTWUAkMq9VWFT19yisFFEiSrBMoj2CMmRcTqqsJ/By7mIqX4Y0EVG5cMFQdUcXSP3veBWutdFNZ3tSEZxtmuzZfZomz1sa26VsNDeUNmsEatBDxq/s/7FAqz7rFYjUMlaGpBH5vkgv+EWyz3eENZBw31iEnffwZB7m3TP6lDKhgPNo8UI82Vq/qErEQTlX+M3LO8aI6VAmC1yocuFh905RUH7541CahPAz1gz9arA0pyHAGH15I957tKNLgPmgn/wdMtUgk=',
        '_jxxs': '1660048262-c6fce740-fa30-11ec-a264-c3172eb5e9ad',
        '_jxs': '1660048262-c6fce740-fa30-11ec-a264-c3172eb5e9ad',
        '__asc': '56ac8d7518282964cecf207fcfb',
        '_SID_Tokopedia_': 'PAYebd0wR3FPcwz0VvfOD0AondxTzbnERnKVsVBb2e7_zZv3zrF8KdxPsKcYJVi_4z4k1sEYZHqIYMYmsuclv_bCz0t186X9GXrrPfmGVBykd5ercCSaysynbQukhV4I',
        'shipping_notif': '0',
        'l': '1',
        'TOPATK': 'kA12q0p2Q3an21dj6b8hZg',
        'FPF': '1',
        'tuid': '211921174',
        'uide': 'E8jVEfrLZWWKXIM8287G2iBywhiYNT3YagrMFb/gHEW9o2xkZQ==',
        'uidh': 'ja2SgTexE9txKF76WgBJjBakoZGmKeav+YPYoO2L+X4=',
        '_abck': '4253AD1D5ED85B49E02531EA3802EDA7~0~YAAQDopRaD1jNEeCAQAAO7SWgghgmNxy1Pq1sqZhuUfK7TQTtBTLHhqF/49HWc9QJt+NPMdGzEHvElWparG42oIsRe3+FLaPkEYpizItZybI0KDJ6TyNHtBgvfkpf4gq8bWpUoxfXoo9Y5vUwi4bwm0jR9EOCxB69LY16JDHee1HtnYrv6qLJ8MLvHdO0QqGXCKDe4FJp33NZNsHVM2tzwaZb4H37qzLY/it8imbntZqAo9wnguu6m0iEoSWdoVDEufETBlS+bAlMj1UMwa82Cnc+V4247AI/Iy7KbGms4wyGQsaEObETzra3pLjX0/4NYLLWDpFjmf6iwzDFRoWq0jIlXFgcp33RUzOdYX66Q0Tmviw8W0+PPyjvxGEBS8eLRmSXq4ig0dcgrRmkSoUZN3+Ccs+8o4eXtNw~-1~-1~-1',
        'aus': '1',
        '_CASE_': '7c25634e63253d353530332b25664e63253d372b256b656b253d254d666c66757366275772746673252b25644e63253d3630312b256b686960253d25252b256b6673253d25252b25774468253d25252b25704e63253d36353536373430322b25744e63253d36363234373230342b2574537e7762253d25356f252b25706f74253d255c7c5b25706675626f68727462586e635b253d36353536373430322b5b25746275716e646258737e77625b253d5b25356f5b252b5b255858737e776269666a625b253d5b25506675626f68727462745b257a2b7c5b25706675626f68727462586e635b253d372b5b25746275716e646258737e77625b253d5b2536326a5b252b5b255858737e776269666a625b253d5b25506675626f68727462745b257a5a252b256b527763253d25353735352a373f2a373e53363e3d34363d34312c37303d3737257a',
        'bm_sv': '583E478957655B640AA77FD166E52B9A~YAAQDopRaAhkNEeCAQAALPOWghCpXu+0gqqZdVq5jGze3eV4QgDHTAUs3nYwRuU3679uwd2yRSWHuLZsQfZlgCtitsLmTI5a4B6X0iOpg6JTGAkedVmMSLzVvZucMbqiXFjySJpj0QKtJZCTWTQVybxI0WahQYnS3KufVEBJaqsNDXr/Tl7K+lxK62Hp2hh4JBeXFVRiSPUS4xlD/WEQ/JaJOFQMg+uxqzjnttssjbYuyBMx0OtIPGyhtO/+Ywxze0ye~1',
        '_dc_gtm_UA-9801603-1': '1',
        '_ga_70947XW48P': 'GS1.1.1660048261.23.1.1660048331.52',
        '_dc_gtm_UA-126956641-6': '1',
        '_ga': 'GA1.2.1203349446.1655650355',
        'webauthn-session': '8baec156-fdf9-488f-94f2-281bda7cd263',
    }

    headers = {
        'authority': 'gql.tokopedia.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://www.tokopedia.com',
        'pragma': 'no-cache',
        'referer': str(url),
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-device': 'desktop',
        'x-source': 'tokopedia-lite',
        'x-tkpd-akamai': 'pdpGetLayout',
        'x-tkpd-lite-service': 'zeus',
        'x-version': '93ddf3d',
    }

    json_data = [
        {
            'operationName': 'PDPGetLayoutQuery',
            'variables': {
                'shopDomain': str(referer[0]),
                'productKey': str(referer[1]),
                'layoutID': '',
                'apiVersion': 1,
                'userLocation': {
                    'cityID': '176',
                    'addressID': '0',
                    'districtID': '2274',
                    'postalCode': '',
                    'latlon': '',
                },
                'extParam': 'ivf%3Dfalse',
            },
            'query': 'fragment ProductVariant on pdpDataProductVariant {  errorCode  parentID  defaultChild  sizeChart  totalStockFmt  variants {    productVariantID    variantID    name    identifier    option {      picture {        urlOriginal: url        urlThumbnail: url100        __typename      }      productVariantOptionID      variantUnitValueID      value      hex      stock      __typename    }    __typename  }  children {    productID    price    priceFmt    optionID    productName    productURL    picture {      urlOriginal: url      urlThumbnail: url100      __typename    }    stock {      stock      isBuyable      stockWordingHTML      minimumOrder      maximumOrder      __typename    }    isCOD    isWishlist    campaignInfo {      campaignID      campaignType      campaignTypeName      campaignIdentifier      background      discountPercentage      originalPrice      discountPrice      stock      stockSoldPercentage      startDate      endDate      endDateUnix      appLinks      isAppsOnly      isActive      hideGimmick      isCheckImei      minOrder      __typename    }    thematicCampaign {      additionalInfo      background      campaignName      icon      __typename    }    __typename  }  __typename}fragment ProductMedia on pdpDataProductMedia {  media {    type    urlThumbnail: URLThumbnail    videoUrl: videoURLAndroid    prefix    suffix    description    __typename  }  videos {    source    url    __typename  }  __typename}fragment ProductHighlight on pdpDataProductContent {  name  price {    value    currency    __typename  }  campaign {    campaignID    campaignType    campaignTypeName    campaignIdentifier    background    percentageAmount    originalPrice    discountedPrice    originalStock    stock    stockSoldPercentage    threshold    startDate    endDate    endDateUnix    appLinks    isAppsOnly    isActive    hideGimmick    __typename  }  thematicCampaign {    additionalInfo    background    campaignName    icon    __typename  }  stock {    useStock    value    stockWording    __typename  }  variant {    isVariant    parentID    __typename  }  wholesale {    minQty    price {      value      currency      __typename    }    __typename  }  isCashback {    percentage    __typename  }  isTradeIn  isOS  isPowerMerchant  isWishlist  isCOD  isFreeOngkir {    isActive    __typename  }  preorder {    duration    timeUnit    isActive    preorderInDays    __typename  }  __typename}fragment ProductCustomInfo on pdpDataCustomInfo {  icon  title  isApplink  applink  separator  description  __typename}fragment ProductInfo on pdpDataProductInfo {  row  content {    title    subtitle    applink    __typename  }  __typename}fragment ProductDetail on pdpDataProductDetail {  content {    title    subtitle    applink    showAtFront    isAnnotation    __typename  }  __typename}fragment ProductDataInfo on pdpDataInfo {  icon  title  isApplink  applink  content {    icon    text    __typename  }  __typename}fragment ProductSocial on pdpDataSocialProof {  row  content {    icon    title    subtitle    applink    type    rating    __typename  }  __typename}query PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation, $extParam: String) {  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation, extParam: $extParam) {    name    pdpSession    basicInfo {      alias      isQA      id: productID      shopID      shopName      minOrder      maxOrder      weight      weightUnit      condition      status      url      needPrescription      catalogID      isLeasing      isBlacklisted      menu {        id        name        url        __typename      }      category {        id        name        title        breadcrumbURL        isAdult        isKyc        minAge        detail {          id          name          breadcrumbURL          isAdult          __typename        }        __typename      }      txStats {        transactionSuccess        transactionReject        countSold        paymentVerified        itemSoldFmt        __typename      }      stats {        countView        countReview        countTalk        rating        __typename      }      __typename    }    components {      name      type      position      data {        ...ProductMedia        ...ProductHighlight        ...ProductInfo        ...ProductDetail        ...ProductSocial        ...ProductDataInfo        ...ProductCustomInfo        ...ProductVariant        __typename      }      __typename    }    __typename  }}',
        },
    ]

    response = requests.post('https://gql.tokopedia.com/graphql/PDPGetLayoutQuery', cookies=cookies, headers=headers, json=json_data)
    arr_data = response.json()
    first_arr_data = arr_data[0]
    data_json = first_arr_data['data']
    cat_product_json = data_json['pdpGetLayout']
    arr_data2 = cat_product_json['components']
    detail_json = arr_data2[4]
    data_arr = detail_json['data']
    data_json = data_arr[0]
    data_arr = data_json['content']
    for x in data_arr:
        if x['title']=='Deskripsi':
            data = x['subtitle']
            break
    return data

def extract_desc_key(url):
    start = url.find('.com/') + 5
    end = url.find('/', start)
    
    key = [None] * 2
    key[0] = url[start:end]

    stop = url.find('?')
    key[1] = url[end+1:stop]
    return key

def total_of_pages(total):
    return (total+60-1)/60

def start_from(page):
    return ((page-1)*60) + 1

def tokopedia_main(total):
    total = int(total)
    pages = total_of_pages(total)
    pages = int(pages)
    product_datas = []
    # print('pages: ', pages)
    for i in range(0,pages):
        if total <= 60:
            # print('masuk =1 dan <= 60')
            product_datas += fetch_product_data(i+1, start_from(i+1), total)
        elif total > 60:
            # print('masuk elif total > 60')
            product_datas += fetch_product_data(i+1, start_from(i+1), 60)
            total = total - 60

    # get product description data but for now deactived still find the best solution
    # for x in product_datas:
    #     x['description']=fetch_product_description(x['url'])
    return product_datas


if __name__ == '__main__':
    tokopedia_main(60)