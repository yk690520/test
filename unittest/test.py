from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import requests,json,time
rsponse=requests.get("http://www.junx.ink/get_code.html")
resault=json.loads(rsponse.text)
if not resault["state"] == "success":
    time.sleep(5)
code = resault["code"]
print(code)