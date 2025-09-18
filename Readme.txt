Readme.txt

## MKS 146B Capacitance Manometers: PC Communication

This repository provides code to communicate with an MKS 146B controller connected to two capacitance manometers, from a Windows PC. It has been tested on Windows 10.

### What this does

Opens a serial connection to the MKS 146B controller

Sends commands and parses responses for two attached capacitance manometers

Reads pressures and basic status information

For full command syntax and protocol details, see the supplementary section of the MKS 146B manual.

### Requirements

MKS 146B controller with more than 1 capacitance manometers attached.

Serial/USB interface and driver depends on your Device.

Windows 10+

Python 3.10 + pyserial, or C++ with Win32 serial API

### Quick start

Connect the controller to your PC via RS-232 or 485.

Check the COM port from Device Manager.

Configure port settings to match your instrument (baud rate, parity, stop bits). Refer to MKS 146B manual for details.

Run the example script/program and set the correct COM port.