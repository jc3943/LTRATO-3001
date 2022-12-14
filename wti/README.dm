# WTI Device Upgrade Demonstration

This WTI Device Upgrade program will query WTI devices for their version and device type, then go online to see if there is a newer version available. If there is a newer version it will be downloaded and the WTI device updated.

This `Device Upgrade` Python script will work on any modern WTI device, the device upgrade automation calls are universal on all WTI OOB and PDU type devices.

# To Configure Python Script:
This Python script requires Python 3.0 and above and the `requests` module.


# To Run:
`python3 upgrade.py`

The program will ask for the protocol "http or https", the location of your WTI device and the username/password of that WTI device, and if you want to only check the device without updating.

These prompts can also be bypassed with command line parameters.
`python3 upgrade.py -h`

will print out the command line options that are accepted by the program

# Contact US
This software is presented for demonstration purposes only, but if you have any questions, comments or suggestions you can email us at kenp@wti.com

# About Us
WTI - Western Telematic, Inc.
5 Sterling, Irvine, California 92618

Western Telematic Inc. was founded in 1964 and is an industry leader in designing and manufacturing power management and remote console management solutions for data centers and global network locations. 
Our extensive product line includes Intelligent PDUs for remote power distribution, metering, reporting and control, Serial Console Servers, RJ45 A/B Fallback Switches and Automatic Power Transfer Switches.