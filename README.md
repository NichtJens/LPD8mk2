# LPD8mk2

<img src="https://d1jtxvnvoxswj8.cloudfront.net/wysiwyg/akai-pro/pdp/lpd8mk2/LPD8_II_RGB_angle_right_web.png" width=50%>


## Example

```python
from time import sleep
from lpd8mk2 import LPD8

# create the interface object
lpd8 = LPD8()

# define a callback
def cb(x):
    print("got:", x)

# add the callback to a knob and a pad
lpd8.knob1.change.add_callback(cb)
lpd8.pad1.on.add_callback(cb)

# keep python from exiting
while True:
    sleep(1)
```
