import json
import os
import urllib
import pyodbc

#with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
with open('secrets.json') as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        print("Invalid Key")


def connection_string(type='sqlite'):
    if type == 'sqlite':
        # Use a local sqlite database
        return 'sqlite:///rubs.db'
    elif type == 'dev':
        # Import 'secret' info
        drivers = [item for item in pyodbc.drivers()]
        driver = drivers[-1]
        print("driver:{}".format(driver))

        username = get_secret('user')
        password = get_secret('password')
        server = get_secret('server')
        dbname = get_secret('dbname')
        #params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 17.0};"
        params = urllib.parse.quote_plus("DRIVER=" + driver + ";"
                                 "SERVER=" + server + ";"
                                 "PORT=1433;"
                                 "DATABASE=" + dbname + ";"
                                 "UID="+ username + ";"
                                 "PWD=" + password)
        return ('mssql+pyodbc:///?odbc_connect={}'.format(params))
    else:
        print("Unrecognised type, connecting to local sqlite.  Valid types are 'sqllite' or 'dev'.")
        return 'sqlite:///rubs.db'
