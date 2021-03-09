set APT_ARCH=WIN
ECHO APT_ARCH=%APT_ARCH%
SET APT_HOME=%CD%
ECHO APT_ARCH=%APT_HOME%
if ("%10" NEQ "") goto :cmd10
if ("%9" NEQ "") goto :cmd9
if ("%8" NEQ "") goto :cmd8
if ("%7" NEQ "") goto :cmd7
if ("%6" NEQ "") goto :cmd6
if ("%5" NEQ "") goto :cmd5
if ("%4" NEQ "") goto :cmd4
if ("%3" NEQ "") goto :cmd3
if ("%2" NEQ "") goto :cmd2
if ("%1" NEQ "") goto :cmd1
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar
:cmd1
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1
:cmd2
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2
:cmd3
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3
:cmd4
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4
:cmd5
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4 %5
:cmd6
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4 %5 %6
:cmd7
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4 %5 %6 %7
:cmd8
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4 %5 %6 %7 %8
:cmd9
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4 %5 %6 %7 %8 %9
:cmd10
java -Duser.language=en -Duser.region=US -mx2048M -jar C:/ProgramData/APT_v2.8.3/APT_v2.8.3/APT.jar %1 %2 %3 %4 %5 %6 %7 %8 %9 %10
