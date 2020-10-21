@ECHO OFF

SET A=1
SET B=0
SET FIB=0
SET N=%1

:loop
	ECHO %FIB%
	SET /a FIB = %A% + %B%
	SET A=%B%
	SET B=%FIB%
	SET /a N -= 1

	IF %N% GTR 0 (goto loop:)

pause