import smtplib
import config


def send_email(subject, msg):

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.SENDER_EMAIL, config.PASSWORD)
        message = 'Subject: {} {}'.format(subject, msg)
        server.sendmail(config.SENDER_EMAIL, config.RECEIPENT_EMAIL, message)
        server.quit()
        print("Message sent successfully.")
    except:
        print("Message send failed.")


subject = 'Hello Man'
msg = 'How are you? Been a long time.'

send_email(subject, msg)
