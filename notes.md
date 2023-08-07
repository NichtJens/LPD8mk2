# References
## Device
- https://www.akaipro.com/lpd8-mk2
## LPD8 mk1 libs
- https://github.com/charlesfleche/lpd8editor/blob/master/doc/SYSEX.md
- https://github.com/bennigraf/lpd8-web-editor/blob/main/lpd8-web-editor-preact/src/LPD8Preset.js
- https://github.com/DrLuke/python-lpd8/
- https://github.com/zetof/LPD8/
## MIDI
- Identity Request: http://midi.teragonaudio.com/tech/midispec/identity.htm

# Capturing MIDI via Wireshark
- The official "Program Editor" for Windows starts in Wine under Linux, but does not connect to the device.
- USB monitoring under MacOS needs the XHC20 interface enabled:
  - https://wiki.wireshark.org/CaptureSetup/USB#macos
  - TL;DR: `sudo ifconfig XHC20 up`
- USB monitoring under MacOS **Catalina** needs *System Integrity Protection* disabled:
  - https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection
  - TL;DR: reboot to recovery mode and `csrutil disable`
- The LPD8 needs to be plugged in while Wireshark is already capturing, otherwise Wireshark reads the MIDI messages as generic USB messages.

# Random stuff
- "Note On" etc. also contain the channel number: http://midi.teragonaudio.com/tech/midispec/noteon.htm
- The mido callback mechanism is weird for IOPorts: The constructor argument doesn't seem to do anything. Setting `ioport.callback = func` enables the exception on receive etc., but the callback is not triggering. Setting `ioport.input.callback = func` works as it should.
