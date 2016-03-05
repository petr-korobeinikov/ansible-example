<?php

$hostname = trim(file_get_contents('/etc/hostname'));
$version  = phpversion();

printf("Hello, I am php '%s' on '%s' machine!\n", $version, $hostname);
