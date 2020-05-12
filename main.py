#!/usr/bin/env python
import sys
from Crypto.Hash import MD5
import markdown2

def markdown(content):
    return markdown2.markdown(content)

def md5_digest(data):
    return MD5.new(data).hexdigest()

def main():
    print("-----------------------------------------------")
    print("Simple application for test scanning with jake")
    print("-----------------------------------------------")
    print("> Testing Crypto:")
    print('>> MD5 of abc = ' + md5_digest(b'abc'))
    print("> Testing Markdown:")
    content = "**boom!**"
    print(">> Markdown of :" + content + ' is ' + markdown(content))
    return 0

if __name__ == '__main__':
    sys.exit(main())
