import requests

def get_response_from_pdql(host, user, password, secret, filter, assets, limit):

    url = 'https://' + host + ':3334/connect/token'

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = {
                'username': user,
                'password': password,
                'client_id': 'mpx',
                'client_secret': secret,
                'grant_type': 'password',
                'response_type': 'id_token',
                'scope': 'mpx.api'
            }
    
    response = requests.post(url, data=data, headers=headers, verify=False)
    print("Token Request (" + url + ") has following Response", response)
    
    token = response.json()['access_token']
    print("Token: ", token)

    headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json;charset=UTF-8',
    'authorization': 'Bearer ' + token
    }

    json_data = {
        'pdql': filter,
        'selectedGroupIds': [],
        'additionalFilterParameters': {
            'groupIds': [],
            'assetIds': assets,
            },
        'includeNestedGroups': True,
        'utcOffset': '+03:00',
    }

    response = requests.post(
        "https://" + host + ":443/api/assets_temporal_readmodel/v1/assets_grid",
        headers=headers,
        json=json_data,
        verify=False,
    )
    print("PDQL Token Request has following Response", response)

    pdql_token = response.json()['token']
    print("PDQL Token: ", pdql_token)
    
    params = {
        'pdqlToken': pdql_token,
        'limit': limit
    }

    response = requests.get(
        "https://" + host + ":443/api/assets_temporal_readmodel/v1/assets_grid/data",
        params=params,
        headers=headers,
        verify=False,
    )

    return response
