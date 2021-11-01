#/bin/bash

count(){
    name=$1
    echo "Testing $name"
    path="$2/test"
    solved=0

    for pr in ${path}*; do
        python3 sudoku.py $pr > test.txt
        echo "Testing" $pr
        ./checker.bin $pr test.txt
        if [[ $? == 0 ]]; then
            solved=$((solved + 1))
        fi
    done

    num_instances=`ls -1 ${path}* | wc -l`

    echo "################################"
    echo "On" $name
    echo "Solved" $solved "out of" $num_instances
    echo "################################"

    rm -f test.txt
    return $solved
}

if [[ $# < 2 && $1 == "standard" ]]; then
    count "3x3" "./instances/standard"
elif [[ $# < 2 && $1 == "non_standard" ]]; then
    count "random shapes" "./instances/non_standard"
else 
    echo "Please supply a testing argument."
    echo "This command accepts (standard | non_standard)"
    echo "Example: bash" $0 "standard" 
    exit -1
fi
