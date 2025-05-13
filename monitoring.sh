#!/bin/bash

#Time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

#CPU
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')

#Memory
mem_total=$(free -m | awk '/Mem:/ {print $2}')
mem_used=$(free -m | awk '/Mem:/ {print $3}')
mem_usage=$(awk "BEGIN {printf \"%.2f\", (${mem_used}/${mem_total})*100}")

# Disk usage (harddisk)
disk_usage=$(df -h | awk '/\/$/ {print $5}' | tr -d '%')

#RAM
swap_total=$(free -m | awk '/Swap:/ {print $2}')
swap_used=$(free -m | awk '/Swap:/ {print $3}')
swap_usage=0
if [ "$swap_total" -ne 0 ];
then
swap_usage=$(awk "BEGIN {printf \"%.2f\", (${swap_used}/${swap_total})*100}")
fi

echo "[$timestamp] CPU: $cpu_usage% | RAM: $mem_usage% | Swap: $swap_usage% | Disk: $disk_usage%"

echo "$timestamp, CPU: $cpu_usage%, RAM: $mem_usage%, Swap: $swap_usage%, Disk: $disk_usage%" >> server_monitor.log

