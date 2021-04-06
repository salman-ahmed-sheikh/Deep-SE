import os
import time
# run preprocess_storypoint.py

datasetDict = {
      'mesos': 'apache'
    , 'usergrid': 'apache'
    , 'appceleratorstudio': 'appcelerator'
    , 'aptanastudio': 'appcelerator'
    , 'titanium': 'appcelerator'
    , 'duracloud': 'duraspace'
    , 'bamboo': 'jira'
    , 'clover': 'jira'
    , 'jirasoftware': 'jira'
    , 'moodle': 'moodle'
    , 'datamanagement': 'lsstcorp'
    , 'mule': 'mulesoft'
    , 'mulestudio': 'mulesoft'
    , 'springxd': 'spring'
    , 'talenddataquality': 'talendforge'
    , 'talendesb': 'talendforge'
}

dataPres = ['apache', 'appcelerator', 'duraspace', 'jira', 'moodle', 'lsstcorp', 'mulesoft', 'spring', 'talendforge']


time1=time.time()
for project, repo in datasetDict.items():
    print (project + ' ' + repo)
    cmd = 'python divide_data_sortdate.py ' + project
    print (cmd)
    os.system(cmd)
 
time2=time.time()
print()
print("Execution done on dicide_data_sortdate in: ",(time2-time1))
print()

for dataPre in dataPres:
    print (project + ' ' + repo)
    cmd = 'python preprocess.py ' + dataPre
    print (cmd)
    os.system(cmd)
    
time3=time.time()
print()
print("Execution done on preprocess in: ",(time3-time2))
print()

for project, repo in datasetDict.items():
    print (project + ' ' + repo)
    cmd = 'python preprocess_storypoint.py ' + project + ' ' + repo
    print (cmd)
    os.system(cmd)

time4=time.time()
print()
print("Execution done on preprocess_storypoint in: ",(time4-time3))
print()