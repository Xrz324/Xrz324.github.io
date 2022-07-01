---
layout: post
title: Windows下开机启用WiFi热点
slug: wifi
date: 2022-06-24 23:00
status: publish
author: Xuerunze
categories: 
  - Tech
tags:
  - Powershell
  - Windows
  - Tech
excerpt: 这是一个实例，以在Win11上利用Powershell自动开启WiFi热点
---

#Powershell新建脚本
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
if ($tetheringManager.TetheringOperationalState -eq 1) 
{
    "Hotspot is already On!"
}
else{
    "Hotspot is off! Turning it on"
    Await ($tetheringManager.StartTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])
}
```

#调整Powershell执行策略以允许外部脚本运行
```cpp
set-executionpolicy remotesigned
```

#迁移启动项至CMD以配置自动运行
```cpp
pushd %~dp0
powershell.exe -command ^
"& {set-executionpolicy Remotesigned -Scope Process; .'.\wifi.ps1' }"
popd
pause
```

#Kaspersky部署
##https://t.wss.ink/f/8p2m9iru3hp
