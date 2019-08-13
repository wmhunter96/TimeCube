# TimeCube

est. 7.29.19

description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Bill of Materials

- RTC (DS3231) - [https://amzn.to/315dmPr](https://amzn.to/315dmPr)
- IMU (MPU-6050) - [https://amzn.to/2YAOMrY](https://amzn.to/2YAOMrY)
- OLED screens(6) (SSD1306?)  - [https://amzn.to/310JpQw](https://amzn.to/310JpQw)
- Rasperry pi Zero W - [https://amzn.to/314JqTK](https://amzn.to/314JqTK)
- Neopixels
- Various 3d printed parts
- USB C breakout - [https://amzn.to/2STxCRo](https://amzn.to/2STxCRo)
- Charge controller
- 18650 cells
- Power switch - [https://amzn.to/2LNmepm](https://amzn.to/2LNmepm)
- DC-DC Adjustable Step-up boost Power Converter Module XL6009
- TCA9548A I2C Multiplexer
- MP1584EN DC-DC Buck Converter Adjustable Voltage Regulator Step-Down Power Module


### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
1. Raspian
2. Python 3
```

RTC

```
1. put the below line into the /boot/config.txt file: (edit it with your favourite editor and type the line in - or copy and paste it from here :-) )

dtoverlay=i2c-rtc,ds3231

2. edit the /lib/udev/hwclock-set file (sudo nano /lib/udev/hwclock-set) and "comment out" the following lines ("comment out" means put a # at the beginning of each of the lines, so they become comments and are ignored by the system)

if [ -e /run/systemd/system ] ; then
exit 0
fi

so they become:

#if [ -e /run/systemd/system ] ; then
# exit 0
#fi


reboot

sudo hwclock -r
```

IMU
```
https://pypi.org/project/mpu6050-raspberrypi/
```
OLED
```
https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/usage
```


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Hunter Rodriguez** - [Github](https://github.com/wmhunter96)
* **Brian Bugert** - [Github](https://github.com/coolbots7)

See also the list of [contributors](https://github.com/wmhunter96/TimeCube/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

## Inspiration

* https://timeular.com/
* https://timeflip.io/
* https://learn.adafruit.com/time-tracking-cube
