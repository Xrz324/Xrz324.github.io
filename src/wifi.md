---
layout: post
title: 给班里传文件用...
slug: wifi
date: 2022-07-04 22:00
status: publish
author: Xuerunze
categories: 
  - Tech
tags:
  - Powershell
  - Windows
  - Tech
excerpt: U盘不方便带，故用博客传文件🤣
---


#Tools
https://wwi.lanzoup.com/ilO4i04hohcf
https://www.iconfont.cn/

#Fun
https://www.imagecu.be/
https://oskarstalberg.com/game/planet/planet.html
https://2017.makemepulse.com/
https://classic.minecraft.net/

#资源站
https://al.chirmyram.com/
https://zf.chirmyram.com/

#影视站
https://azx.me/

#Clash
https://api.v1.mk/sub?target=clash&url=https%3A%2F%2Fpre.paimon.gq%2Fclash.yaml&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online_Full_MultiMode.ini&emoji=true&list=false&udp=false&tfo=false&expand=true&scv=true&fdn=false&new_name=true

#Manjaro配置
##懒得现打，提前弄好😶
配置镜像 `sudo pacman-mirrors -i -c China -m rank`
配置ArchlinuxCN源 `sudo gedit /etc/pacman.conf`
```
[archlinuxcn]
SigLevel = Optional TrustedOnly
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```
同步秘钥`sudo pacman -S archlinuxcn-keyring`
输入法相关`sudo pacman -S fcitx-im` `sudo pacman -S fcitx-configtool` `sudo pacman -S fcitx-sogoupinyin`
加载输入法`gedit ~/.xprofile`
```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```
Fix Sougou`yay -S fcitx-qt4`
WPS
```
sudo pacman -S wps-office
sudo pacman -S ttf-wps-fonts
yay -Ss wps | grep zh
yay -S archlinuxcn/wps-office-mui-zh-cn
```
