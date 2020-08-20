# Basic CPP Command Line Project


<!---[![Build status](https://ci.appveyor.com/api/projects/status/kb60bd7u2wn969l5/branch/master?svg=true)](https://ci.appveyor.com/project/tommccallum/yourapp/branch/master) 
[![codecov](https://codecov.io/gh/tommccallum/yourapp/branch/master/graph/badge.svg?token=QKAZL10PE6)](https://codecov.io/gh/tommccallum/yourapp)
[![Build Status](https://travis-ci.org/tommccallum/yourapp.svg?branch=master)](https://travis-ci.org/tommccallum/yourapp)
[![CMake](https://github.com/tommccallum/yourapp/workflows/CMake/badge.svg)
--->

## Requirements

## Build instructions

This is a C++ application that has been tested with g++ and clang++ using C++17.
Once you have downloaded the source from the git repository then type the following:

```
mkdir build
cd build
cmake ..
make
make test
```

## Docker instructions

```
docker build .
```

You will end up with the following:
```
Successfully built 5d4611cb33c8
```
Copy the final hex number and run as follows:
```
docker run -ti <hex_number>
```
Then type the following to begin a new session:
```
./app
```

## Running the application

The application will be created in the _bin_ directory of the build directory. These instructions assume you are in the build directory.

