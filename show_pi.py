#!/usr/bin/env python3

def approximate_pi():
    return 355 / 113

def show_pi():
    print("pi is approximately {:.8f}".format(approximate_pi()))

if __name__ == "__main__":
    show_pi()
