#!/usr/bin/env python

from time import sleep
from lpd8mk2 import LPD8


lpd8 = LPD8("LPD8")

print("port:", lpd8.port)
print("callback:", lpd8.port.input.callback)

print()
for k, v in lpd8.all_knobs.items():
    print(k, v)

print()
for k, v in lpd8.all_pads.items():
    print(k, v)

print()
print("attributes:")
for name in dir(lpd8):
    if not name.startswith("_"):
        print("-", name)

print()



lpd8.send_id_request()
n = lpd8.send_which_program()
print("Program:", n)

for i in range(4):
    knobs, pads = lpd8.send_get_program(i+1)
    print("Knobs:", knobs)
    print("Pads: ", pads)



def cb_test(x):
    print("cb test", x)

lpd8.knob1.change.add_callback(cb_test)
lpd8.pad1.on.add_callback(cb_test)



while True:
    sleep(1)



