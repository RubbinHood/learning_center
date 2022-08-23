import os


def send_mail(to, fr, subject, text):
    os.system(f'mail -m "{text}" -s "{subject}" -a "FROM: {fr}"  {to}')
