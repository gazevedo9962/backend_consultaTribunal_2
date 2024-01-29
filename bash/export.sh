#!/usr/bin/bash

var=$1
valor=$2
#bash -c "export $var" 
export $var=$valor
env | grep "$var"