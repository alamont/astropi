## AstroPi Telescope Control

### pigpio

Install pigpio:

```bash
rm pigpio.zip
sudo rm -rf PIGPIO
wget abyz.me.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
sudo make install
```

Before running the motor control server we need to start the pigpio daemon. Make sure to disable polling as it doesn't play well with pyserial when polling is enabled. Using both causes 100% CPU usage.

```
sudo pigpiod -m
```