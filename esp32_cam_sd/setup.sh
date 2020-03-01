#!/bin/bash
esptool.py --chip esp32 --port $1 --baud 115200 --before default_reset --after hard_reset write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect 0xe000 part1_0xe000.bin 0x1000 part2_0x1000.bin 0x10000 part3_0x10000.bin 0x8000 part4_0x8000.bin
