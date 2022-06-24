---
layout: post
title: Mapper foreach中循环遍历List、Array参数设置
slug: Mybatis
date: 2021-05-12 16:00
status: publish
author: Xuerunze
categories: 
  - Mybatis
tags:
  - Design
  - Web
excerpt: 使用Mybatis中的foreach循环遍历参数
---
在做mybatis的mapper.xml文件的时候，我们时常用到这样的情况：动态生成sql语句的查询条件，这个时候我们就可以用mybatis的foreach了

foreach元素的属性主要有item，index，collection，open，separator，close。

item：集合中元素迭代时的别名，该参数为必选，意思是每次遍历时的别名，这里是什么参数名，下面引用也是引用这个参数名。
index：在list和数组中,index是元素的序号，在map中，index是元素的key，该参数可选
open：foreach代码的开始符号，一般是(和close=”)”合用。常用在in(),values()时。该参数可选
separator：元素之间的分隔符，例如在in()的时候，separator=”,”会自动在元素中间用“,“隔开，避免手动输入逗号导致sql错误，如in(1,2,)这样。该参数可选。
close: foreach代码的关闭符号，一般是)和open=”(“合用。常用在in(),values()时。该参数可选。
collection: 要做foreach的对象，作为入参时，List对象默认用”list”代替作为键，数组对象有”array”代替作为键，Map对象没有默认的键。当然在作为入参时可以使用@Param(“keyName”)来设置键，设置keyName后，list,array将会失效。 除了入参这种情况外，还有一种作为自定义的Java对象的某个字段的时候。举个例子：如果User有属性List ids。入参是User对象，那么这个collection = “ids”.如果User有属性Ids ids;其中Ids是个对象，Ids有个属性List id;入参是User对象，那么collection = “ids.id”
在使用foreach的时候最关键的也是最容易出错的就是collection属性，该属性是必须指定的，但是在不同情况下，该属性的值是不一样的，主要有一下3种情况：

如果传入的是单参数且参数类型是一个List的时候，collection属性值为list .(注意是小写)
例如：
```cpp
       public List<Tag> selectTagListByIds( List<Long> ids);
```
如果传入的是单参数且参数类型是一个array数组的时候，collection的属性值为array .
例如：
```cpp
     int batchRemove(Integer[] ids);
```
如果传入的参数是多个的时候，我们就需要把它们封装成一个Map了，当然单参数也可以封装成map，实际上如果你在传入参数的时候，在MyBatis里面也是会把它封装成一个Map的，map的key就是参数名，所以这个时候collection属性值就是传入的List或array对象在自己封装的map里面的key.