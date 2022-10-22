#!/bin/bash

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

python3 -m src.island_count "$1"
