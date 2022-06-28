$rc = "info.rc"
$c = "点我启动.c"
$o = "点我启动.o"
$exe= "点我启动.exe"
windres $rc $o
gcc -O3 $o $c -o $exe
del $o

upx --best 点我启动.exe