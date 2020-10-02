
import os
import boto3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_name, sender_email, recipient_email, subject, body_text, body_html=None, attachment=None, region_name='us-east-1'):
    try:
        client = boto3.client('ses', region_name=region_name)
        charset = "utf-8"

        msg = MIMEMultipart('mixed')

        msg['Subject'] = subject
        msg['From'] = f'{sender_name} <{sender_email}>'
        msg['To'] = recipient_email

        msg_body = MIMEMultipart('alternative')

        textpart = MIMEText(body_text, 'plain', charset)

        msg_body.attach(textpart)

        if body_html:
            htmlpart = MIMEText(body_html, 'html', charset)
            msg_body.attach(htmlpart)

        if attachment:
            att = MIMEApplication(open(attachment, 'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
            msg.attach(att)

        msg.attach(msg_body)

        response = client.send_raw_email(
            Source=msg['From'],
            Destinations=[msg['To']],
            RawMessage={'Data': msg.as_string()}
        )

        return response
    except Exception as e:
        print(e)
        raise e
