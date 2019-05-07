#!/usr/bin/env python
'''
 -*- coding: utf-8 -*-
 @File  : Unittest.py
 @Author: kiki
 @Date  : 2019-05-07
 
 '''
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        pass

    def test_1_login_blog(self):
        print('登录博客')

    def test_2_add_essay(self):
        print('添加随笔')

    def test_3_release_essay(self):
        print('发布随笔')

    def test_4_quit_blog(self):
        print('退出博客园')

    def tearDown(self):
        pass


if __name__ == '__main__':
    # 启动单元测试
    unittest.main()
