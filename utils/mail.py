import smtplib

def test():
    server = smtplib.SMTP('185.252.29.126', port=25)
    server.sendmail(from_addr='mail@xtechno.ir', to_addrs='s.s.gholamzadeh@outlook.com', msg='hello')
    print('test was successful')
