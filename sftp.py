import pysftp


def upload(host, username, password, file):
    with pysftp.Connection(host, username=username, password=password) as sftp:
        with sftp.cd('/default/phone-uservisits/'):  # temporarily chdir to public
            #print("uploading...." + host, username, password )
            print("uploading via SFTP.....")
            sftp.put(file)  # upload file to public/ on remote
            print("successfully dropped to "+ username)
