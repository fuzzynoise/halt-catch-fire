#!/bin/bash
f() {
    printf '>'
    read
    f
} f
