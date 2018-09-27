#!/bin/bash

abcd='abcd'
if [[ ${abcd} == *d ]]
then
echo 'yh'
fi

echo $(${abcd} == *d)