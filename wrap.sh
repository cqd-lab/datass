#!/bin/bash

Color_Off='\033[0m'       # Text Reset
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan


echo -e "${Purple}# Removing old build...${Color_Off}"
rm -r dist/ > /dev/null 2>&1

case "$1" in
    "b")
        echo -e "${Purple}# Creating new build...${Color_Off}"
        python3 setup.py sdist bdist_wheel
        python3 -m build > /dev/null 2>&1
        ;;
    "p")
        echo -e "${Purple}# Uploading to PyPi...${Color_Off}"
        twine upload dist/*
        ;;
    *)
esac

echo -e "${Purple}# Done${Color_Off}"
