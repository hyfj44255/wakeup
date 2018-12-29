#!/bin/bash
# Start the first process
nohup python -u /usr/src/app/double/z1.py > /usr/src/app/double/log 2>&1 &
ps aux |grep z1 |grep -q -v grep
PROCESS_1_STATUS=$?
echo "z1 status..."
echo $PROCESS_1_STATUS
if [ $PROCESS_1_STATUS -ne 0 ]; then
echo "Failed to start my_first_process: $PROCESS_2_STATUS"
exit $PROCESS_1_STATUS
fi
sleep 2
# Start the second process
nohup python -u /usr/src/app/double/z2.py > /usr/src/app/double/log2 2>&1 &
ps aux |grep z2 |grep -q -v grep
PROCESS_2_STATUS=$?
echo "z2 status..."
echo $PROCESS_2_STATUS
if [ $PROCESS_2_STATUS -ne 0 ]; then
echo "Failed to start my_second_process: $PROCESS_2_STATUS"
exit $PROCESS_2_STATUS
fi
# 每隔60秒检查进程是否运行
while sleep 5; do
ps aux |grep z1 |grep -q -v grep
PROCESS_1_STATUS=$?
ps aux |grep z2 |grep -q -v grep
PROCESS_2_STATUS=$?
# If the greps above find anything, they exit with 0 status
# If they are not both 0, then something is wrong
if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
echo "One of the processes has already exited."
exit 1
fi
done
