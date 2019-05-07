#!/usr/bin/env python
'''
 -*- coding: utf-8 -*-
 @File  : practice1.py
 @Author: kiki
 @Date  : 2019-05-07
 @project:学习和使用unittest框架编写测试用例思路
 '''
import unittest

import time

class Test(unittest.TestCase):
    def setUp(self):
        print('start!')

    def tearDown(self):
        time.sleep(1)
        print('end!')

    def test1(self):
        print('执行测试用例 1')
    def test3(self):
        print('执行测试用例 3')

    def test2(self):
        print('执行测试用例 2')

    def addtest(self):
        print('add 方法')

if __name__ == '__main__':
    unittest.main()
'''
3、运行结果分析

1、从运行结果可以看出执行顺序：

　　start!-执行测试用例 01-end!

　　start!-执行测试用例 02-end!

　　start!-执行测试用例 03-end!

2、从执行结果可以看出几点

　　--先执行的前置 setUp，然后执行的用例(test*)，最后执行的后置 tearDown

　　--测试用例（test*）的执行顺序是根据 01-02-03 执行的，也就是说根据用例名称来顺序执行的

　　--addtest（self）这个方法没执行,说明只执行 test 开头的用例
'''
