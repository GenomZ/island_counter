#!/bin/bash

# Comment if running from the package directory and dont want to use relative path to it for input files
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $(echo "$SCRIPT_DIR" | tr -d '\r') || exit

# If no arguments provided, print:
if [ $# -eq 0 ]; then
    echo ">>>>>>>>>> No arguments provided <<<<<<<<<<"
    echo
    echo "island_counter requires an input file to run"
    echo "Please provide a file of appropriate format."
    echo "  - zeros (ASCII character 48)"
    echo "  - ones (ASCII character 49)"
    echo "  - end-of-line character"
    echo "i.e.:"
    echo
    echo "000000000"
    echo "010000000"
    echo "111000100"
    echo "110001110"
    echo "000001100"
    echo "001000000"
    echo "110000000"
    echo "000001100"
    echo
    echo "and execute:"
    echo "./island_counter.sh <path_to_the_file>"
    
    exit 1
fi

# Uncomment if want to use provided docker container with configured python installed
#sudo docker run -i --rm island_counter ./island_counter.sh "$1"

# Commend if using docker solution
python3 -m src.island_count "$1"
