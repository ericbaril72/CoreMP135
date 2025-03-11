# CoreMP135
My own dev notes on using the M5Stack CoreMP135

## Image burning
- Once Image is burnt (sdcard.img ) to sdcard using BalenaEtcher 1.18.11 ( 1.19.25 was returning an error on file open )
- [pre-compiled images](https://docs.m5stack.com/en/guide/linux/coremp135/image#1.download%20image%20file)


## Connect to USB-C
- connect to device using Putty + USB-c interface
-- Windows device manager to find the COMx number
- login: root
- password: (none) <enter><enter>

## Expand the sdcard partition
> cd /usr/local/m5stack
> ./resize_mmc
> reboot

## Create your admin user ( only on DebianImage )
- create new user that will be able to access the device via SSH with sudo rights ( always better not to use root )
> adduser <user1>
> usermod -aG sudo <user1>

# Development
## help links for uboot cmd_show_logo task
https://stackoverflow.com/questions/53374999/custom-u-boot-environment-variables-using-buildroot
