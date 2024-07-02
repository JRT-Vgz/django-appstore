from fabric.api import task, local, run, env, cd, prefix, sudo, get

env.user = "Vargath"
env.hosts = ["123.456.789.000"] 

# AUTOMATIZACIÓN DEL DEPLOY CON FABRIC3

def deploy(file_name):    
    with cd("/home/jrtvgz/project/django-appstore"):
        run("git pull")
        with prefix("source env/bin/activate"):
            run("pip install -r requirements.txt")
            run("python3 manage.py migrate")
        sudo("systemctl restart django")
        sudo("systemctl restart nginx")
        
        
def make_deploy(commit=""):
    local("python manage.py test.py")
    local("git add .")
    local(f"git commit -m {commit}")
    local("git push main origin")
    deploy()


@task(alias="download_log")
def download_error_log():
    sudo("tail -n 50 /var/log/nginx/error.log > tmp.log")
    get(
        local_path="error_log.log",
        remote_path="/home/jrtvgz/tmp.log"
    )
    sudo("rm temp.log")