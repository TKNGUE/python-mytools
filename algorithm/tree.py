#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BinaryIndexedTree(object):
    def __init__(self, size):
        self.data = [0] * size
        pass

    def sum(self, i):
        assert i > 0
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        assert i > 0
        while i < self.size:
            self.data[i] += x
            i += i & -i
        return x

def main():
    """entry point"""
    N = raw_input()
    print N

if __name__ == '__main__':
    main()
