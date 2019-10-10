from jenkins import Jenkins
import json
import sys
from requests.exceptions import ConnectionError

with open('config.json') as j:
    creds = json.load(j)

jenkins = Jenkins(creds['jenkins_server'], username=creds['jenkins_username'], password=creds['jenkins_password'])

def get_all_jobs():
    '''
    for i in jenkins.get_all_jobs():
        print(list(i[3]))
    '''
    return jenkins.get_all_jobs()

def get_job_status(jobname):
    
    for i in get_all_jobs()[1:]:
        job_color = i["color"]
        job_name = i['name']
        if job_name == jobname:
            if job_color == 'blue':
                return jobname,'Success'
            elif job_color == 'red':
                return jobname,'Failed'
            else:
                return jobname,job_color
            
            return job_name,job_color

if len(str(sys.argv[1])) == 0:
    getjobs = get_all_jobs()
    for i in getjobs:
        job_color = i['color']
        if job_color == 'blue':
            print(i['name'], ':', 'Success')
        elif job_color == 'red':
            print(i['name'], ':', 'Failed')
        else:
            print(i['name'], ':', job_color)
else:
    name = str(sys.argv[1])
    status = get_job_status(name)
    print(status)
