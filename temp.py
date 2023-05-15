import time
from gpiozero import CPUTemperature

duration = 15

print(f"Running Temps for {duration}")

for second in range(1, duration):
    cpu = CPUTemperature()
    print(f"{second}:{cpu.temperature}")
    
print("Done.")