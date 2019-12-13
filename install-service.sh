#!/bin/bash

systemctl disable iot-ht
systemctl stop iot.ht
cp iot-ht.service /lib/systemd/system/iot-ht.service 
systemctl daemon-reload
systemctl start iot-ht
systemctl enable iot-ht


