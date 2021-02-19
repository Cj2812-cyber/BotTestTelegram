from methods.rtlabs.adapters import ssh_connector



def get_logs_by_text(text_error):

    with ssh_connector.SSHConnectFromSSH(True) as ftp:
        #stdin, stdout, stderr = ssh.exec_command("cd /egov/logs/prod")
        print(ftp.getcwd())
