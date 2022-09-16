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
#Wallpaper
https://www.imagecu.be/
https://oskarstalberg.com/game/planet/planet.html
https://2017.makemepulse.com/
https://classic.minecraft.net/

#热点


powershell -executionpolicy remotesigned -file "%appdata%\Microsoft\Windows\Start Menu\Programs\pondsihotspot.ps1"  

exit


set-executionpolicy remotesigned


```cpp
Add-Type -AssemblyName System.Runtime.WindowsRuntime 

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0] 

Function Await($WinRtTask, $ResultType) { 

    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType) 

    $netTask = $asTask.Invoke($null, @($WinRtTask)) 

    $netTask.Wait(-1) | Out-Null 

    $netTask.Result 

} 

Function AwaitAction($WinRtAction) { 

    $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and !$_.IsGenericMethod })[0] 

    $netTask = $asTask.Invoke($null, @($WinRtAction)) 

    $netTask.Wait(-1) | Out-Null 

} 

$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile() 

$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile) 

if ($tetheringManager.TetheringOperationalState -eq 1) { 

    "" 

} 

else{ 

    Await ($tetheringManager.StartTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]) 

}
```

#资源站
https://al.chirmyram.com/

#影视站
https://azx.me/

