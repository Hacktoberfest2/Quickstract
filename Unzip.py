from zipfile import ZipFile
import sys
import os


hackfile = (sys.argv[1])
password = (sys.argv[2])

print("Code by Tikvah for HTB")


def updatename(zip):
    with ZipFile(zip, "r") as myzip:
        arcname = myzip.namelist()
        return str(arcname[0])


def openzip(zip, password1):
    with ZipFile(zip) as unzip:
        unzip.extractall(pwd=password1)

while True:
    print("Extracting: " + str(hackfile))
    print("With password: " + str(password))
    openzip(hackfile, password)
    hackfile = updatename(hackfile)
    password = updatename(hackfile)
    if password.endswith('.zip'):
    	password = password[:-4]
