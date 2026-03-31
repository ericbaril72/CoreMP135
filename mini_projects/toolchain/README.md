# Windows vs Ubuntu
WSL has done a lot for me developping software in a Ubuntu environment along with tons of Docker Containers

However, simple tools like dd to write on a USB sdcard do not work.
Using a USB device on Ubuntu often requires to re-apply  "usbipd share"  command

I finally decided to mount a real Ubuntu partition on my PC and it requires to install the full toolchain


# Installing the toolchain from scratch
```
sudo apt update
sudo apt upgrade

sudo apt install build-essential make cmake
```

## Python and virtual environment
```
sudo apt install python3.12-dev python3.12-venv
python3 -m venv myenv

source myenv/bin/activate

pip install parse scons pexpect paramiko scp
```

## Cross-compiler
```
wget https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linaro/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz
sudo tar -xvzf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz -C /opt/
```

## Project Directory
```
mkdir ~/CoreMP135
cd CoreMP135
```
    .
    ├── CoreMP135/
    │   ├── M5Stack_Linux_Libs/
    │   ├── coremp135-bsp/
    │   ├── buildroot/
    



## Buildroot and external defconfig
```
git clone git@github.com:m5stack/CoreMP135_buildroot.git
git clone \<this repo\>
```


## C and CPP based development environment with examples

```
git clone https://github.com/m5stack/M5Stack_Linux_Libs
cd M5Stack_Linux_Libs/examples/hello_world
scons menuconfig
```
1. Press Enter to enter Toolchain Configuration
2. Press Enter to fill the "Toolchain path"
3. type the absolute path from the Cross-compiler installation: /opt/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf/bin
4. Press Enter to fill the "Toolchain prefix": arm-linux-gnueabihf-
5. Press ESC-ESC and "Save to Config"

```
scons
```
will now build & link the software, ready to upload and run


## building your first buildroot
```
cd ~/CoreMP135/buildroot
make BR2_EXTERNAL=../coremp135-bsp/ coremp135_defconfig
make
```
Have a beer ... this may take a while

The Buildroot script goes through all of the defconfig file parameters and checks for all required host and target packages and does the following:
- download the package src to buildroot/dl
- unzip the package to buildroot/output/build
- applies the package patches ( as per defconfig )
- configures the package ( as per defconfig )
- build the package

This defconfig file also runs theese scripts:
- post-build.sh
- post-image.sh





