#!/bin/bash

SRC_DIR=$1

INDENT_PAM="-bap -bbb -bbo -nbc -bl -bli0 -bls -c33 -cd33 -ncdb -ncdw -nce -cli4 -cp33 -d0 -nbfda -di2 -nfc1 -nfca -hnl -ip5 -l80 -lp -nprs -nsc -nsob -nss -i4 -ts4 -ut"

INDENT_PATH="/usr/bin/indent"

echo "format source file in $SRC_DIR"

for i in `find $SRC_DIR -name '*.c' -o -name '*.h' `
do
    echo "formatting file   "$i
    RUN_CMD="$INDENT_PATH $i $INDENT_PAM"
    echo $RUN_CMD
    $RUN_CMD
  #  rm -f $i~
    echo "---------------------------------------"
done