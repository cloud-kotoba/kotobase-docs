#!/bin/bash
{
date '+NOW: %Y-%m-%d %H:%M:%S %Z'
uptime
} > /tmp/bench_time.txt 2>&1
echo done