# -*- coding: utf-8 -*-
import urllib
import re
import sys

if len(sys.argv) > 1:
    a = urllib.urlopen('http://number.whoscall.com/%E5%8F%B0%E7%81%A3%E5%8F%B0%E7%81%A3/{}/'.format(sys.argv[1]))
    b = a.read().decode('utf-8')
    pdata = re.findall("number-info__name.*?<span.*?itemprop.*?name\">(.*?)</span>", b, re.DOTALL)
    if len(pdata) < 1:
        pdata.append("No Info")
else:
    pdata.append("No Info")
sys.stdout.write('<?xml version="1.0"?>')
sys.stdout.write('<items>')
sys.stdout.write('<item arg="a">')
sys.stdout.write('<title>' + pdata[0].encode('utf-8') + '</title>')
sys.stdout.write('</item>')
sys.stdout.write('</items>')
