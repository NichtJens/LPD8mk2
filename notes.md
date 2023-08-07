# References
- https://www.akaipro.com/lpd8-mk2
- https://github.com/charlesfleche/lpd8editor/blob/master/doc/SYSEX.md
- https://github.com/DrLuke/python-lpd8/
- https://github.com/zetof/LPD8/

# Capturing MIDI via Wireshark
- The official "Program Editor" for Windows starts in Wine under Linux, but does not connect to the device.
- USB monitoring under MacOS needs the XHC20 interface enabled:
  - https://wiki.wireshark.org/CaptureSetup/USB#macos
  - TL;DR: `sudo ifconfig XHC20 up`
- USB monitoring under MacOS **Catalina** needs *System Integrity Protection* disabled:
  - https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection
  - TL;DR: reboot to recovery mode and `csrutil disable`
- The LPD8 needs to be plugged in while Wireshark is already capturing, otherwise Wireshark reads the MIDI messages as generic USB messages.
