# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 17:06
# @Author  : Ian Leto
# @Site    : 
# @File    : usage_lxml.py
# @Software: PyCharm

from lxml import etree

root = etree.Element('root')

child0 = etree.SubElement(root, 'child0')
child1 = etree.SubElement(root, 'child1')


