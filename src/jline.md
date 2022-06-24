---
layout: post
title: Java四种线程池的使用
slug: blog
date: 2020-09-06 22:00
status: publish
author: Xuerunze
categories: 
  - Java
tags:
  - Code
  - Java
excerpt: Java中四种线程池的使用实例
---
##实现
```cpp
/**
     * 1.创建一个可缓存线程池，如果线程池长度超过处理需要，可灵活回收空闲线程，若无可回收，则新建线程
     */
    public static void cachedThreadPool() {
        ExecutorService cachedThreadPool = Executors.newCachedThreadPool();
        for (int i = 0; i < 10; i++) {
            final int index = i;
            try {
                Thread.sleep(1 * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            cachedThreadPool.execute(new Runnable() {
                @Override
                public void run() {
                    System.out.println(index + "--" + Thread.currentThread().getId());
                }
            });

        }
    }

    /**
     * 2.创建一个定长线程池，可控制线程最大并发数，超出的线程会在队列中等待
     */

    public static void newFixedThreadPool() {
        ExecutorService fixedThreadPool = Executors.newFixedThreadPool(5);
        for (int i = 0; i < 10; i++) {
            final int index = i;
            fixedThreadPool.execute(new Runnable() {
                @Override
                public void run() {
                    try {
                        System.out.println(index + "-----" + Thread.currentThread().getId());
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }
        //fixedThreadPool.shutdown();
    }

    /**
     * 3.创建一个定长线程池，支持定时及周期性任务执行
     */
    public static void newScheduledThreadPool() {
        ScheduledExecutorService scheduledThreadPool = Executors.newScheduledThreadPool(5);
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, 10); // 时
        calendar.set(Calendar.MINUTE, 53);// 分
        calendar.set(Calendar.SECOND, 00); // 秒
        //计算现在时间和计划任务执行时间差多久，单位毫秒
        Long date = calendar.getTime().getTime() - System.currentTimeMillis();
//        //延迟3秒执行
        scheduledThreadPool.schedule(new Runnable() {
            @Override
            public void run() {
                System.out.println("delay 3 seconds--" + new Date().toLocaleString());
            }
        }, 3, TimeUnit.SECONDS);

        //延迟5秒执行，然后每隔2秒执行一次
        scheduledThreadPool.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                System.out.println("延迟5秒执行，然后每隔2秒执行一次--" + new Date().toLocaleString());
            }
        }, 5, 2, TimeUnit.SECONDS);

        //定时在某一时刻执行任务，然后间隔执行,如果时间过了会立马执行
        scheduledThreadPool.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                System.out.println("定时在某一时刻执行任务，然后间隔执行--" + new Date().toLocaleString());
            }
        }, date / 1000, 2, TimeUnit.SECONDS);
    }

    /**
     *4. 创建一个单线程化的线程池，它只会用唯一的工作线程来执行任务，
     * 保证所有任务按照指定顺序(FIFO, LIFO, 优先级)执行
     */
    public static void newSingleThreadExecutor() {
        ExecutorService singleThreadExecutor = Executors.newSingleThreadExecutor();
        for (int i = 0; i < 10; i++) {
            final int index = i;
            singleThreadExecutor.execute(new Runnable() {
                @Override
                public void run() {
                    try {
                        System.out.println("单线程执行任务。。。");
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }
    }
    ```