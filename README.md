# embedded
Embedded computing projects.

## pyclock (7-segment)
This _basic_ clock script uses code from [Adafruit's Raspberry Pi Python Code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_LEDBackpack) to display the current time on a 7-segment LED from Adafruit, connected to I2C on the Pi.

On Raspbian, installing the Aptitude package `python-smbus` will get you all of the dependencies that you need.

Run the clock with `sudo python clock.py`. Consider installing [Supervisor](http://supervisord.org/) to run the clock as a service.

*Status: working.*

### TO DO
* Packaging for distribution, installation, dependency portability.

