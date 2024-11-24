"""notification manager"""
import smtplib
import os

MY_EMAIL = "sundalei2011@163.com"

class NotificationManager:
    """notification manager"""

    def send_mail_notification(self, emails, content):
        """send mail notification"""
        emails.append("sundalei1988@gmail.com")

        for email in emails:
            with smtplib.SMTP_SSL(host="smtp.163.com", port=465) as connection:
                connection.login(user=MY_EMAIL, password=f"{os.getenv('MAIL_APP_PASSWORD')}")
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Low price alert!\n\n{content}")


if __name__ == "__main__":
    notification_manager = NotificationManager()
    notification_manager.send_mail_notification(emails=["sundalei1988@gmail.com"], content="test")
