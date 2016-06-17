from ftplib import FTP
import sys
import glob

# 	USER DETAIL
USER=''
PASS=''

#	SERVER DETAILS
SERVER=''
PORT='21'
BINARY_STORE = True


def connect_ftp():
    #Connect to the server
    ftp = FTP()
    ftp.connect(SERVER, PORT)
    ftp.login(USER, PASS)
    ftp.cwd('')             #folder name if any else delete this line
    return ftp


def upload_file(ftp_connetion, upload_file_path):

    #Open the file
    try:
        upload_file = open(upload_file_path, 'r')
        
        #get the name
        path_split = upload_file_path.split('/')
        final_file_name = path_split[len(path_split)-1]
    
        #transfer the file
        print('Uploading ' + final_file_name + '...')
        
        if BINARY_STORE:
            ftp_connetion.storbinary('STOR '+ final_file_name, upload_file)
        else:
            #ftp_connetion.storlines('STOR ' + final_file_name, upload_file, print_line)
            ftp_connetion.storlines('STOR '+ final_file_name, upload_file)
            
        print('Upload finished.')
        
    except IOError:
        print ("No such file or directory... passing to next file")


if __name__=='__main__':
        #Take all the files and upload all
        ftp_conn = connect_ftp()
	
        f_name=raw_input("      Enter file name:        ")
        upload_file(ftp_conn,f_name)

	