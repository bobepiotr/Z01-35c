@echo off
ECHO -----------Expected 6-----------
python p_tree.py "2 + 2 * 2" -t

ECHO -----------Expected 8-----------
python p_tree.py "( 2 + 2 ) * 2" -t

ECHO -----------Expected 18-----------
python p_tree.py "( ( 4 + 2 ) + ( 3 * ( 5 - 1 ) ) )" -t #expected 18

ECHO -----------Expected 2-----------
python p_tree.py "( ( 3 + 4 ) * 2 ) / 7" -t #expected 2

ECHO -----------Expected 2160-----------
python p_tree.py "( ( 4 + 2 ) + ( 3 * ( 5 + ( 3 * ( 9 - 1 ) ) - 1 ) ) ) * ( 3 + 21 )" -t #expected 2160

pause