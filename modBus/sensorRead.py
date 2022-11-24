#!/usr/bin/env python

import sys
import serial
import time
import RPi.GPIO as GPIO
import minimalmodbus

sensorBoard = minimalmodbus.Instrument('/dev/serial0',int(sys.argv[1]))

sensorBoard.serial.port
sensorBoard.serial.baudrate = 19200
sensorBoard.serial.bytesize = 8
sensorBoard.serial.stopbits = 1
sensorBoard.serial.parity = serial.PARITY_NONE
sensorBoard.serial.timeout = 0.5
sensorBoard.address
sensorBoard.mode = minimalmodbus.MODE_RTU
sensorBoard.clear_buffers_before_each_transaction = True
sensorBoard.close_port_after_each_call = True
sensorBoard.handle_local_echo = True
#sensorBoard.debug = True

try:
	reading = sensorBoard.read_registers(0,31)
	print(reading)

except IOError:
	print("Failed to read from sensorBoard "+sys.argv[1])

sensorBoard.serial.close()
#GPIO.cleanup()
