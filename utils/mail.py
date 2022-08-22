import os


def send_mail(to, fr, subject, text):
    os.system(f'echo "{text}" | mail -s "{subject}" -a "FROM: {fr}"  {to}')
