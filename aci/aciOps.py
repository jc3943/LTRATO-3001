def bakeCookies(specDict2):
    import urllib3
    import requests
    baseURL = "https://" + specDict2['hostIp']
    tokenURL = baseURL + "/api/aaaLogin.json"

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    tokenHeader = {"content-type": "application/json"}
    jsonPayload = {'aaaUser':{"attributes":{'name':specDict2['username'],'pwd':specDict2['password']}}}
    tokenResponse = requests.post(tokenURL, json=jsonPayload, verify=False)
    jsonData = tokenResponse.json()
    token = jsonData["imdata"][0]["aaaLogin"]["attributes"]["token"]
    newCookie = {'APIC-cookie':token}
    return newCookie

def createTacacs(specDict, apicSnacks):
    import urllib3
    import requests
    baseURL = "https://" + specDict['hostIp']
    cookie = apicSnacks
    providerURL = baseURL + "/api/node/mo/uni/userext/tacacsext/tacacsplusprovider-172.16.5.1.json"
    loginDomainURL = baseURL + "/api/node/mo/uni/userext.json"
    providerPayload = {"aaaTacacsPlusProvider":{"attributes":{"dn":"uni/userext/tacacsext/tacacsplusprovider-172.16.5.1","name":"172.16.5.1","key":"THORP@ssw0rd!","rn":"tacacsplusprovider-172.16.5.1","status":"created"},"children":[{"aaaRsSecProvToEpg":{"attributes":{"tDn":"uni/tn-mgmt/mgmtp-default/oob-default","status":"created"},"children":[]}}]}}
    loginDomainPayload = {"aaaUserEp":{"attributes":{"dn":"uni/userext","status":"modified"},"children":[{"aaaLoginDomain":{"attributes":{"dn":"uni/userext/logindomain-tacacsLoginDomain","name":"tacacsLoginDomain","rn":"logindomain-tacacsLoginDomain","status":"created"},"children":[{"aaaDomainAuth":{"attributes":{"dn":"uni/userext/logindomain-tacacsLoginDomain/domainauth","realm":"tacacs","providerGroup":"tacacsLoginDomain","rn":"domainauth","status":"created"},"children":[]}}]}},{"aaaTacacsPlusEp":{"attributes":{"dn":"uni/userext/tacacsext","status":"modified"},"children":[{"aaaTacacsPlusProviderGroup":{"attributes":{"dn":"uni/userext/tacacsext/tacacsplusprovidergroup-tacacsLoginDomain","status":"created"},"children":[{"aaaProviderRef":{"attributes":{"dn":"uni/userext/tacacsext/tacacsplusprovidergroup-tacacsLoginDomain/providerref-172.16.5.1","order":"1","name":"172.16.5.1","status":"created"},"children":[]}}]}}]}}]}}
    providerResponse = requests.post(providerURL, json=providerPayload, cookies=cookie, verify=False)
    loginDomainResponse = requests.post(loginDomainURL, json=loginDomainPayload, cookies=cookie, verify=False)
    print(providerURL, providerResponse, sep=": ")
    print(loginDomainURL, loginDomainResponse, sep=": ")