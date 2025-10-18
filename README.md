# CoreMP135
My own dev notes on using the M5Stack CoreMP135<br>
Thanks to @Johandevlabs, fellow user including notes to install older WifiDongle : https://github.com/johandevlabs/CoreMP135-Debian-notes<br>
Another usefull fellow user : https://remyhax.xyz/posts/m5stack-coremp135/

[M5stack CoreMP135](https://docs.m5stack.com/en/core/M5CoreMP135)<br>
[Main M5Stack links](https://docs.m5stack.com/en/guide/linux/coremp135/image)<br>
[Lolin stm32MP157-dk build instructions](https://bootlin.com/blog/building-a-linux-system-for-the-stm32mp1-basic-system/)<br>


## Links
[M5Stack_Linux_Libs](https://github.com/m5stack/M5Stack_Linux_Libs)<br>
[CoreMP135_buildroot](https://github.com/m5stack/CoreMP135_buildroot)<br>
[CoreMP135_buildroot-external-st](https://github.com/m5stack/CoreMP135_buildroot-external-st)<br>
[Buildroot Tutorial](https://bootlin.com/doc/training/buildroot/buildroot-slides.pdf)<br>

[Schematic mid Layer](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24.pdf)<br>
[Schematic CPU ](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24.pdf)<br>

[ILI9342C specsheet](https://www.orientdisplay.com/wp-content/uploads/2021/02/ILI9342C_AN_01_20111228.pdf)<br>

[STM32MP - ARM Cortex-A & Linux ](https://www.st.com/content/ccc/resource/training/technical/product_training/group1/7a/bb/02/0b/e6/77/45/6e/stm32mp1-series-software-architecture-and-secure-boot/files/stm32mp1-series-software-architecture-and-secure-boot.pdf/jcr:content/translations/en.stm32mp1-series-software-architecture-and-secure-boot.pdf)<br>
Arm cortex-A provides Secure and non-secure execution modes.  This presentation explains how peropherals are initialized 

[OpenSTLinux ARchitecture details](https://wiki.st.com/stm32mpu/index.php?title=STM32MPU_Embedded_Software_architecture_overview&oldid=80273)
![blablabla](https://wiki.st.com/stm32mpu/nsfr_img_auth.php/9/9c/STM32MPU_Embedded_Software_architecture_overview.png)

# 1. Extra details
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


## CoreMP135 Bootup process
1- On power-up, the CPU checks BOOTn pins ( 1-0-1 ) and starts loading from SD card.

2- SDcard first partition contains linux U-BOOT
U-Boot is a bootloader that does minor CPU initialisation and starts loading the linux kernel file
based on u-boot config, the kernel file might need to be signed and/or encrypted
u-boot initialize the uart terminal pins, the base  LCD init with startup-logo

3- Linux kernel start



## Change UBOOT displayed Logo
On device power-up, a CoreMP135 logo gets shown within 1-2 seconds.  
This one is transfered to the LCD via spi via the UBOOT bootloader command "show_logo"

Whitin your (workpath)/CoreMP135_buildroot  Directory
> make uboot-menuconfig
--> Boot options > Autoboot options > Delay in seconds before automatically booting = 0   ( way faster ! )

> make uboot-rebuild
( will download the uboot-custom package ready to modify and generate a new uboot-nodtc.bin )

> make arm-trusted-firmware-rebuild
( will update the fip.bin from the uboot-nodtc.bin previously updated )


> make
( will generate a new sdcard.img file )

## edit cmd_show_logo.c
output/build/uboot-custom/cmd/cmd_show_logo.c


Quick BMP to "C" code convertion: https://notisrac.github.io/FileToCArray/
BUT output file creates 16bits array ...
using convert.py to generate proper 8bits array

### generating a patch file
diff -u "old_file" "new_file" > file.patch

## VERY quick image burning
Copy you sdcard.img to a previously programmed and actively running CoreMP135 device
> scp output/images/sdcard.img ericadmin@CoreMP135:.

install your target sdcard into the USB2.0 interface of CoreMP135
> sudo dd if=sdcard.img of=/dev/sda bs=1M status=progress oflag=dsync && sync 
or self update
> dd if=sdcard.img of=/dev/mmblk0 bs=1M && sync


## Untested boot uart stuff
STM32MP1xx platforms from ST uses the STlinkV2.2 mounted to UART4 but the M5Stack CoreMP135 uses those pins differently.
M5Stack changed DTC files to use USART6 ( port-C ) in linux resolving to ttySTM0
<br>BUT<br>
it doesn't work so far with my trials on u-boot.

found in OpTEE-os-custom:
~/CoreMP135/CoreMP135_buildroot/output/build/optee-os-custom/core/arch/arm/plat-stm32mp1/platform_config.h
line 177# #define STM32MP1_DEBUG_USART_BASE	UART4_BASE  > changing to UART6_BASE

found in 
/home/ericb/CoreMP135/CoreMP135_buildroot/output/build/optee-os-custom/core/arch/arm/plat-stm32mp1/conf.mk
line 330# CFG_STM32_EARLY_CONSOLE_UART ?= 6    ( was 4 !!!)

## unknown if required
make optee-client-rebuild
## rebuilds tee.bin used by trusted-firmware
make optee-os-rebuild
cd outp  cdasd
