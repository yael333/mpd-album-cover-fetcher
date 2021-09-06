#!/bin/bash
mpc --format "%artist%---%album%" current -p 6600 | nc -c localhost 65432