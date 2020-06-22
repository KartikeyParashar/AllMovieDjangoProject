from fabric.api import local


def backup():
    local("git pull")
    local("git add .")
    print("Enter Your Commit Comment: ")
    comment = input()
    local("git commit -m '%s'" % comment)
    local("git push")


def fuser():
    local("fuser -k 8000/tcp")


def makemigrations():
    local("python3 manage.py makemigrations")


def migrate():
    local("python3 manage.py migrate")


def runserver():
    local("python3 manage.py runserver")


def shell():
    local("python3 manage.py shell")