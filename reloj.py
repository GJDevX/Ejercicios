import time
import sys 

for hora in range(0, 24):
    for minutos in range(0,60):
        for segundos in range(0,60):
            sys.stdout.write(f"\r{hora:02d}:{minutos:02d}:{segundos:02d}.")
            sys.stdout.flush()
            time.sleep(1)
        