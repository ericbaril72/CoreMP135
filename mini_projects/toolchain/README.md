# Windows vs Ubuntu
WSL has done a lot for me developping software in a Ubuntu environment along with tons of Docker Containers

However, simple tools like dd to write on a USB sdcard do not work.
Using a USB device on Ubuntu often requires to re-apply  "usbipd share"  command

I finally decided to mount a real Ubuntu partition on my PC and it requires to install the full toolchain


# Installing the toolchain from scratch
```
sudo apt update
sudo apt upgrade

sudo apt install make cmake
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
```mkdir CoreMP135
cd CoreMP135
```



## Buildroot and external defconfig
```git clone git@github.com:m5stack/CoreMP135_buildroot.git
```
git clone <this repo>

## C and CPP based development environment with examples

```git clone https://github.com/m5stack/M5Stack_Linux_Libs```

