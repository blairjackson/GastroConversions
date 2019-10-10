import pysftp


def upload(host, username, password):
    with pysftp.Connection(host, username=username, password=password) as sftp:
        with sftp.cd('/default/phone-uservisits/'):  # temporarily chdir to public
            print("uploading...." + host, username, password )
            print("uploading via SFTP.....")
            sftp.put('tvsquared_conversions2.csv')  # upload file to public/ on remote
            print("successfully dropped to "+ username)