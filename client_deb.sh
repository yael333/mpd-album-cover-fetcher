#!/bin/bash
mpc --format "%artist%---%album%" current -p 6600 | ncat -C localhost 65432
