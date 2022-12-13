#!/bin/sh

echo -e '\n\nExample > expr.logo\n';
python logoParser.py examples/expr.logo;

echo -e '\n\nExample > ifelse.logo\n';
python logoParser.py examples/ifelse.logo;

echo -e '\n\nExample > minimal.logo\n';
python logoParser.py examples/minimal.logo;

echo -e '\n\nExample > square.logo\n';
python logoParser.py examples/square.logo;

echo -e '\n\nExample > while.logo\n';
python logoParser.py examples/while.logo;
