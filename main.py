import subprocess

def ishga_tushirish():
    natija = subprocess.run(['ls', '-la'], capture_output=True, text=True)
    return natija.stdout

print(ishga_tushirish())
