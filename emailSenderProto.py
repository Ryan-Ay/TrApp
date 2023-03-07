#Imports and Such
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Setting up server and port
smtp_port = 587
smtp_server = "smtp.gmail.com"

#Password is a strange string of character, Can't describe what it is but the string can be find in the security/2 step auth. tab of an email account 
pswd = 

email_from = "EMAIL"
email_list = "LIST"

def send_emails(email_list):
  for person in email_list:
    
    body = f"""
    
    """
    
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = person
    msg['Subject'] = "subject"
    
    #Creating the Email
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    
    TIE_server.sendmail(email_from, person, text)
 
  # Close the port
  TIE_server.quit()

send_emails(email_list)
    
    
    
    
