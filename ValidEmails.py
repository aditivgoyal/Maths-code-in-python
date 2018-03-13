"""
This method is to return a list of valid emails from the directory path given. It will search every file in the 
directory path and return the complete set of valid emails.
"""

import os
import re
def read_email(directory_path):
    files = []
    valid_emails=[]
    for filename in os.listdir(directory_path): #Getting list of all the files in the directory
        files.append(str(filename))
    
    number_of_files = len(files)
    
    for i in range(number_of_files): 
        f= open(number_of_files[i],'r') #reading a file at a time
        content = f.read()
        emails = content.split(',') #splitting all the emails by comma (,)
        for email in emails:
            if(validate_email(email)): #checking if email is valid
                valid_emails.append(email)
        f.close()
    
    return valid_emails       

"""
This method checks for valid emails and return True or False
"""
def validate_email(em):  #Checking whether the email is valid or not
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', em)
    if match is None:
        return False
    else:
        return True

