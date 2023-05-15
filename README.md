<!--<img width="10%" src="./repo/argon-neo-featured.jpg">-->

# <img width="4%" src="https://img.icons8.com/?size=512&id=13443&format=png"> Raspberry Pi 4 Model B 
Current Hobby-Build and DIY projects using a `Raspberry Pi 4 Model B (2GB RAM)`.

<br>

<img width="40%" src="./repo/pi-4-b-schematic.png">

<br>

## Specs and Parts
```
Raspberry Pi 4 Model B (2GB LPDDR4-3200 RAM)
Raspbian: Raspberry Pi OS (32-bit)

32GB Micro SD Card

Argon NEO Case
Argon Fan Hat
Argon 18W 5V Power Supply w/ Switch
```

If you want more information about this Raspberry Pi 4 model, **[you can find it here](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)**.
<br>
Here are some other product links:
<br>
- **[Argon NEO Case](https://argon40.com/products/argon-neo-case-for-raspberry-pi-4)**
- **[Argon Fan Hat](https://argon40.com/products/argon-fan-hat?_pos=1&_sid=683d0d276&_ss=r)**
- **[Argon 18W 5V Power Supply](https://argon40.com/products/argon-type-c-power-supply-with-switch-18-watts-5-volts?_pos=3&_sid=4e581e253&_ss=r)**

<br>

# Getting Started
Here are the steps I took configure a brand new `Raspberry Pi 4 Model B`.

<br>

## Raspberry Pi OS Image
1. Use a **32GB Micro SD Card** (any size works), and flash it using the `Raspberry Pi OS Imager`.
2. Download the `Raspberry Pi OS Imager` from **https://www.raspberrypi.com/software/**, or **[for Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe)**.
3. Install the `Raspberry Pi OS Imager` and run it.
4. **OS:** choose `Raspbian: Raspberry Pi OS (32-bit) Debian Port w/ Raspberry Pi Desktop`.
5. **SD:** choose the mounted `32GB Micro SD Card`.
6. Now make any last minute **Advanced Settings** changes as necessary.
7. **Write**.

<br>

## Bash (RPi)
```
$ [sudo] apt-get update
$ [sudo] apt-get update && [sudo] apt-get upgrade
$ [sudo] apt full-upgrade
$ [sudo] reboot
```

<br>

## Hostname
```
$ [sudo] cat /etc/hosts
$ [sudo] nano /etc/hostname
$ [sudo] reboot
$ hostname
```

<br>

## Argon Fan Hat Config
```
$ curl https://download.argon40.com/argon1.sh | bash
$ [sudo] reboot
$ argonone-config
```
```
Fan Power Settings:
55°C=10%
60°C=55%
65°C=100%
```
<br>


## SSH
```
$ echo
```
<br>

## Stressberry 
```
[sudo] apt install stress
pip3 install stressberry --user
pip3 install --upgrade numpy
```
```
mkdir ~/TemperatureTests
cd ~/TemperatureTests
```
```
/home/pi/.local/bin/stressberry-run -n "My Test" -d 1800 -i 300 -c 4 mytest.out
```
### Links: 
**https://github.com/nschloe/stressberry**
<br>
**https://core-electronics.com.au/guides/raspberry-pi/how-to-stress-test-temperature-on-raspberry-pi/**

## Custom Shell Scripts

### **~/temperature.sh**
```
touch ~/temperature.sh
chmod +x ~/temperature.sh
nano ~/temperature.sh
cat ~/temperature.sh
./temperature.sh
```
