import smtplib
import getpass

def sendMail(theirMail, content):
    yourMail = input("Enter your mail Id : ")
    password = getpass.getpass("Enter Your password : ")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(yourMail, password)
        message = f"Subject: Test Email\n\n{content}"
        server.sendmail(yourMail, theirMail, message)
        print("Email has been sent")
    except Exception as e:
        print("Error:", e)
        print("Email Not Sent")
    finally:
        server.quit()

# Run the function
theirMail = input("Enter recipient's email: ")
content = input("Enter the message: ")
sendMail(theirMail, content)
