set ALGOLIB_PATH $HOME/programming/algolib
set ACL_PATH $HOME/programming/ac-library

set CXX_COMPILER g++
set CXX_COMMON_OPTIONS -std=c++17 -Wall -Wextra -Wno-stringop-overflow -I$ALGOLIB_PATH/src -I$ACL_PATH
set CXX_DEBUG_OPTIONS -O0 -g3 -fsanitize=undefined -D_GLIBCXX_DEBUG -DHOGEPACHI
set CXX_RELEASE_OPTIONS -Ofast -DHOGEPACHI

function dg++
    set source_name $argv[1]
    set binary_name (string replace -r '(.*)\.cpp' '$1.exe' $source_name)
    command $CXX_COMPILER $CXX_COMMON_OPTIONS $CXX_DEBUG_OPTIONS $source_name -o $binary_name
end

function fg++
    set source_name $argv[1]
    set binary_name (string replace -r '(.*)\.cpp' '$1.exe' $source_name)
    command $CXX_COMPILER $CXX_COMMON_OPTIONS $CXX_RELEASE_OPTIONS $source_name -o $binary_name
end

function dgch
    set source_name $argv[1]
    set binary_name $source_name.dg++.gch
    command $CXX_COMPILER $CXX_COMMON_OPTIONS $CXX_DEBUG_OPTIONS $source_name -o $binary_name
end

function fgch
    set source_name $argv[1]
    set binary_name $source_name.fg++.gch
    command $CXX_COMPILER $CXX_COMMON_OPTIONS $CXX_RELEASE_OPTIONS $source_name -o $binary_name
end
