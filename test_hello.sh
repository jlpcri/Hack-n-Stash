#!/bin/bash

#[[ `./hello.sh johnny` = "hello johnny!" ]] && (echo "test passed!"; exit 0) || (echo "test failed :-("; exit 1)
[[ `sleep 10 && curl -k -s -o /dev/null -I -w "%{http_code}" https://keystonexxl.app.pcfdev.one.west.com/` = "200" ]] && (echo "test passed!"; exit 0) || (echo "test failed :-("; exit 1)
