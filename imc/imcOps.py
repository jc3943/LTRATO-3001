# Jeff Comer
# collection of imc functions


import sys, getopt, csv, time
import requests, json
import urllib3
from datetime import datetime, timezone
import psycopg2
from psycopg2.extras import execute_values

def disablePC(specDict):
    j = 0
    k = 1
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        vnicInfoUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Chassis/1/NetworkAdapters/"
        print(vnicInfoUrl)
        vnicResponse = requests.get(vnicInfoUrl, verify=False, auth=(specDict['username'], specDict['password']))
        vnicJson = vnicResponse.json()
        vnicSerialUrl = vnicJson["Members"][0]["@odata.id"]
        vicModUrl = "https://" + csvDict[i]['cimc'] + vnicSerialUrl
        pcOffPayload = {"Oem":{"Cisco":{"VicConfiguration":{"PortChannelEnabled":False}}}}
        print(pcOffPayload)
        pcModResult = requests.patch(vicModUrl, json=pcOffPayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(pcModResult)

def createVnic(specDict):
    j = 0
    k = 1
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        vnicInfoUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Chassis/1/NetworkAdapters/"
        vnicResponse = requests.get(vnicInfoUrl, verify=False, auth=(specDict['username'], specDict['password']))
        vnicJson = vnicResponse.json()
        vnicSerialUrl = vnicJson["Members"][0]["@odata.id"]
        vnicList = csvDict[i]['vnicsAdd'].split(";")
        physPortList = csvDict[i]['uplinkPorts'].split(";")
        pcieOrder = csvDict[i]['pcieOrder'].split(";")
        vnicCreateUrl = "https://" + csvDict[i]['cimc'] + vnicSerialUrl + "/NetworkDeviceFunctions"
        print(vnicCreateUrl)
        for j in range(len(vnicList)):
           physPortUrl = vnicCreateUrl + "/NetworkPorts/" + physPortList[j]
           physPortId = physPortList[j].split("-")
           physPortId[1] = int(physPortId[1]) - 1
           cdnName = "hx-vpc-" + str(j)
           vnicPayload = {"Id":vnicList[j],"Name":vnicList[j],"NetDevFuncType":"Ethernet","Ethernet":{"MTUSize":9000},"Links":{"PhysicalPortAssignment":{"@odata.id":physPortUrl}},"Oem":{"Cisco":{"VnicConfiguration":{"UplinkPort":physPortId[1],"PCIOrder":pcieOrder[j],"EthConfiguration":{"Cdn":cdnName}}}}}
           print(vnicPayload)
           vnicCreateResponse = requests.post(vnicCreateUrl, json=vnicPayload, verify=False, auth=(specDict['username'], specDict['password']))

def powerCycle(specDict):
    j = 0
    k = 1
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        baseUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Systems"
        systemsResponse = requests.get(baseUrl, verify=False, auth=(specDict['username'], specDict['password']))
        systemsJson = systemsResponse.json()
        systemsUrl = systemsJson["Members"][0]["@odata.id"]
        pwrCycleUrl = "https://" + csvDict[i]['cimc'] + systemsUrl + "/Actions/ComputerSystem.Reset"
        print(pwrCycleUrl)
        pwrCyclePayload = {"ResetType":"PowerCycle"}
        pwrCycleResult = requests.post(pwrCycleUrl, json=pwrCyclePayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(pwrCycleResult)

def powerOff(specDict):
    j = 0
    k = 1
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        baseUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Systems"
        systemsResponse = requests.get(baseUrl, verify=False, auth=(specDict['username'], specDict['password']))
        systemsJson = systemsResponse.json()
        systemsUrl = systemsJson["Members"][0]["@odata.id"]
        pwrCycleUrl = "https://" + csvDict[i]['cimc'] + systemsUrl + "/Actions/ComputerSystem.Reset"
        print(pwrCycleUrl)
        pwrCyclePayload = {"ResetType":"GracefulShutdown"}
        pwrCycleResult = requests.post(pwrCycleUrl, json=pwrCyclePayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(pwrCycleResult)

def powerOn(specDict):
    j = 0
    k = 1
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        baseUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Systems"
        systemsResponse = requests.get(baseUrl, verify=False, auth=(specDict['username'], specDict['password']))
        systemsJson = systemsResponse.json()
        systemsUrl = systemsJson["Members"][0]["@odata.id"]
        pwrCycleUrl = "https://" + csvDict[i]['cimc'] + systemsUrl + "/Actions/ComputerSystem.Reset"
        print(pwrCycleUrl)
        pwrCyclePayload = {"ResetType":"On"}
        pwrCycleResult = requests.post(pwrCycleUrl, json=pwrCyclePayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(pwrCycleResult)

def getPwrStats(specDict):
    i = 0
    k = 0
    allPwrStats = []
    #pwrStatsDict = {"Host":[],"pwrData":[]}
    pwrStatsDict = {}
    summaryDict = {}
    summaryInfo = []
    current_time = datetime.now(timezone.utc)

    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print("Host,sysAvgWatts,sysMaxWatts,psu1VoltsOut,psu2VoltsOut,psu1Serial,psu1OutWatts,psu1InVolts,psu1InWatts,psu2Serial,psu2OutWatts,psu2InVolts,psu2InWatts")
    for i in range(len(csvDict)):
        epocSec = time.time()
        pwrInfoUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Chassis/1/Power"
        pwrInfoResponse = requests.get(pwrInfoUrl, verify=False, auth=(specDict['username'], specDict['password']))
        pwrInfoJson = pwrInfoResponse.json()
        pwrStatsDict = {csvDict[i]['cimc']:pwrInfoJson}
        allPwrStats.append(pwrStatsDict)
        avgWatts = allPwrStats[i][csvDict[i]['cimc']]["PowerControl"][0]["PowerMetrics"]["AverageConsumedWatts"]
        maxWatts = allPwrStats[i][csvDict[i]['cimc']]["PowerControl"][0]["PowerMetrics"]["MaxConsumedWatts"]
        psu1VoltOut = allPwrStats[i][csvDict[i]['cimc']]["Voltages"][0]["ReadingVolts"]
        psu2VoltOut = allPwrStats[i][csvDict[i]['cimc']]["Voltages"][1]["ReadingVolts"]
        psu1Serial = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][0]["SerialNumber"]
        psu1OutWatts = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][0]["PowerOutputWatts"]
        psu1InVolts = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][0]["LineInputVoltage"]
        psu1InWatts = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][0]["PowerInputWatts"]
        psu2Serial = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][1]["SerialNumber"]
        psu2OutWatts = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][1]["PowerOutputWatts"]
        psu2InVolts = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][1]["LineInputVoltage"]
        psu2InWatts = allPwrStats[i][csvDict[i]['cimc']]["PowerSupplies"][1]["PowerInputWatts"]
        summaryDict = {"host":csvDict[i]['cimc'],"psu1Serial":psu1Serial,"psu2Serial":psu2Serial,"avgWatts":avgWatts,"maxWatts":maxWatts,"psu1InVolts":psu1InVolts,"psu1VoltOout":psu1VoltOut,"psu1InWatts":psu1InWatts,"psu1OutWatts":psu1OutWatts,"psu2InVolts":psu2InVolts,"psu2VoltOut":psu2VoltOut,"psu2InWatts":psu2InWatts,"psu2OutWatts":psu2OutWatts,"psu2InWatts":psu2InWatts,"time":str(current_time),"timesec":epocSec}
        summaryInfo.append(summaryDict)
        print(csvDict[i]['cimc'], str(avgWatts), str(maxWatts), str(psu1VoltOut), str(psu2VoltOut), psu1Serial, str(psu1OutWatts), str(psu1InVolts), str(psu2InWatts), psu2Serial, str(psu2OutWatts), str(psu2InVolts), str(psu2InWatts), sep=",")

    print(json.dumps(summaryInfo))
    conn = psycopg2.connect(host='172.16.67.14', dbname="envmon", user="postgres")
    cursor = conn.cursor()
    columns = summaryInfo[0].keys()
    query = "INSERT INTO imcpwr ({}) VALUES %s".format(','.join(columns))
    values = [[value for value in pwrData.values()] for pwrData in summaryInfo]
    execute_values(cursor, query, values)
    conn.commit()
    return allPwrStats

def getThermStats(specDict):
    #unfinished business
    i = 0
    k = 0
    allThermStats = []
    thermStatsDict = {}
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        thermInfoUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Chassis/1/Thermal"
        thermInfoResponse = requests.get(thermInfoUrl, verify=False, auth=(specDict['username'], specDict['password']))
        thermInfoJson = thermInfoResponse.json()
        thermStatsDict = {csvDict[i]['cimc']:thermInfoJson}
        allThermStats.append(pwrStatsDict)

def imcAdminPw(specDict):

    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        adminPwUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/AccountService/Accounts/1"
        adminPwPayload = {"Id":"1","UserName":"admin","Password":specDict['newPw']}
        adminPwResponse = requests.patch(adminPwUrl, json=adminPwPayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(csvDict[i]['cimc'] + " PW Reset:\t", adminPwResponse)

def imcNetSet(specDict):
    
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        netConfigUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Managers/CIMC/EthernetInterfaces/NICs"
        netConfigDnsList = [csvDict[i]['dns1'],csvDict[i]['dns2']]
        netConfigPayload = {"HostName":csvDict[i]['hostName'],"NameServers":netConfigDnsList,"StaticNameServers":netConfigDnsList}
        netConfigResult = requests.patch(netConfigUrl, json=netConfigPayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(csvDict[i]['cimc'] + " DNS:\t", netConfigResult)

def imcNetProtSet(specDict):

    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        netProtConfigUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Managers/CIMC/NetworkProtocol"
        ntpList = [csvDict[i]['ntp1'],csvDict[i]['ntp2']]
        netProtPayload = {"NTP":{"ProtocolEnabled":True,"NTPServers":ntpList}}
        netProtResult = requests.patch(netProtConfigUrl, json=netProtPayload, verify=False, auth=(specDict['username'], specDict['password']))
        print(csvDict[i]['cimc'] + " NTP:\t", netProtResult)

def getChassisSerial(specDict):

    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)
    keys = csvDict[0].keys()

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        chassisUrl = "https://" + csvDict[i]['cimc'] + "/redfish/v1/Chassis/1"
        chassisInfoResponse = requests.get(chassisUrl, verify=False, auth=(specDict['username'], specDict['password']))
        chassisInfoJson = chassisInfoResponse.json()
        chassisSerial = chassisInfoJson["SerialNumber"]
        if (csvDict[i]['chassisSerial'] == ""):
            csvDict[i]['chassisSerial'] = chassisSerial
    print(csvDict)
    with open(specDict['infile'], "w", newline='') as out_file:
        dictWrite = csv.DictWriter(out_file, keys)
        dictWrite.writeheader()
        dictWrite.writerows(csvDict)
