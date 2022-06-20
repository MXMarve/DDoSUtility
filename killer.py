import os
ip = input("URL: ")
count = input("How hard to hit: 1-50 (Only go more than 3 if your computer supports it): ")
for x in range(int(count)):
  os.system("python3 attacker.py "+ip)