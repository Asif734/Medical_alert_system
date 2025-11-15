from fastapi import BackgroundTasks
from typing import Any, Dict
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

def trigger_alert(urgency_level: str, message: str, doctors: List[str], background_tasks: BackgroundTasks) -> None:
    if urgency_level == "high":
        background_tasks.add_task(send_sms_alert, message, doctors)
        background_tasks.add_task(send_email_alert, message, doctors)
    elif urgency_level == "medium":
        background_tasks.add_task(send_email_alert, message, doctors)

def send_sms_alert(message: str, doctors: List[str]) -> None:
    account_sid = "your_twilio_account_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    for doctor in doctors:
        client.messages.create(
            body=message,
            from_="your_twilio_phone_number",
            to=doctor
        )

def send_email_alert(message: str, doctors: List[str]) -> None:
    smtp_server = "smtp.your_email_provider.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_email_password"

    for doctor in doctors:
        msg = MIMEText(message)
        msg['Subject'] = "Urgent Medical Alert"
        msg['From'] = smtp_user
        msg['To'] = doctor

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, doctor, msg.as_string())