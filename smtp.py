import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import argparse

class smtpJob():
    def __init__(self, ip, sender, receivers, mail_host, mail_port, mail_user, mail_pass):
        self.__ip = ip
        self.sender = sender
        self.receivers = receivers

        # 第三方SMTP服务
        self.mail_host = mail_host
        self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_pass = mail_pass

        self.send_email()

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        # print(name, addr)
        # print(formataddr((Header(name, 'utf-8').encode(), addr)))
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_email(self):
        # 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个 utf8 编码设置
        message = MIMEText('实验室电脑IP：{}'.format(self.__ip), 'plain', 'utf-8')
        message['From'] = self._format_addr('xiaoyun<{}>'.format(self.sender))
        message['To'] = self._format_addr('lqy<{}>'.format(self.receivers))

        subject = '实验室电脑IP地址：'
        message['Subject'] = Header(subject, 'utf-8').encode()

        try:
            smtpObj = smtplib.SMTP(self.mail_host, self.mail_port)
            smtpObj.set_debuglevel(1)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, [self.receivers], message.as_string())
            print('发送成功')
        except smtplib.SMTPException:
            print('Error：无法发送邮件.')

# smtpObj = smtplib.SMTP(mail_host, 25)
# smtpObj.set_debuglevel(1)
# smtpObj.login(mail_user, mail_pass)
# smtpObj.sendmail(sender, [receivers], message.as_string())
# print('发送成功')

if __name__ == '__main__':
    # argparse的用法
    parser = argparse.ArgumentParser(prog="login-NEU", description="get id_addr",
                                     usage="%(prog)s [options]")
    parser.add_argument('--ip', help="input IP address of %(prog)s program.", required=True, type=str)
    parser.add_argument('--sender', help="input sender address of %(prog)s program.", required=True, type=str)
    parser.add_argument('--receivers', help="input receivers address of %(prog)s program.", required=True, type=str)
    parser.add_argument('--mail_host', help="input mail_host address of %(prog)s program.", required=True, type=str)
    parser.add_argument('--mail_port', help="input mail_port of %(prog)s program.", required=True, type=int)
    parser.add_argument('--mail_user', help="input mail_user address of %(prog)s program.", required=True, type=str)
    parser.add_argument('--mail_pass', help="input mail_pass address of %(prog)s program.", required=True, type=str)
    args = parser.parse_args()

    # 发送邮件
    smtpJob(args.ip, args.sender, args.receivers, args.mail_host, args.mail_port, args.mail_user, args.mail_pass)
