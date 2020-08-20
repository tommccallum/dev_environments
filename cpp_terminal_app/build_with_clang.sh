#!/bin/bash

cd build
cmake -DCMAKE_C_COMPILER=$(which clang) -DCMAKE_CXX_COMPILER=$(which clang++) ..
if [ $? == 0 ]
then
    make -j6
fi
if [ $? == 0 ]
then   
    make test
fi