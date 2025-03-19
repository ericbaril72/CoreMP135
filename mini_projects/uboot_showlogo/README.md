# instant show_logo

When running CoreMP135 with buildroot kernel or debian, the boot process is typically 2 stages
- uboot bootloader
- OS initialisation


uboot initializes the LCD and pushes the image via the LCD spi port <br>
( 2-3 seconds after power-up)

once the OS starts and reaches the point where it executes the /etc/rc.local<br>
and the following script is executed /usr/local/m5stack/init.sh  <br>
( when your hear the logo.wav sound being played  10-30 seconds after boot      kernel vs full-debian boot time)




## UBOOT

UBBOOT is built via the buildroot toolchain and provides just enough drivers support ( based on uboot configuration ) to
load the OS image on the sdcard partition and to then call the OS to RUN

uboot prompt/script allows to run a few commands.   M5stack package creates a new command via  "PATCHES" as seen in <br>
 [CoreMP135_buildroot-external-st/board/m5stack/coremp135_5_15/patches/uboot/0001-cmd_show_logo.patch](https://github.com/m5stack/CoreMP135_buildroot-external-st/blob/a376bc8b735070c4bb6a4e61af40e8b6047c177d/board/m5stack/coremp135_5_15/patches/uboot/0001-cmd_show_logo.patch)


