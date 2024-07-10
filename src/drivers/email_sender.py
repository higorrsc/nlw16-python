import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from typing import List


def send_email(to_address: List[str], body: str):
    from_address = "i7iqpwc3vcvkevip@ethereal.email"
    login = "i7iqpwc3vcvkevip@ethereal.email"
    password = "BwbjPSnBnBpSGrw2gP"

    message = MIMEMultipart()
    message["From"] = "viagens_confirmar@email.com"
    message["To"] = ", ".join(to_address)
    message["Subject"] = "Confirmação de viagem"
    message.attach(MIMEText(body, "HTML"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.ehlo()
    server.starttls()
    server.login(login, password)
    for email in to_address:
        server.sendmail(from_address, email, message.as_string())
    server.quit()
