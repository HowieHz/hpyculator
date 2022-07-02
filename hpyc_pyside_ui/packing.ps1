chcp 65001
pip install hpyculator hpyc_core --upgrade

del -Force ".\out\__main__.dist\*" -Recurse
del -Force ".\out\__main__.dist\" -Recurse
del -Force ".\out\full\*" -Recurse
del -Force ".\out\full\" -Recurse
del -Force ".\out\lite\*" -Recurse
del -Force ".\out\lite\" -Recurse

nuitka --mingw64 --standalone --windows-disable-console --quiet --show-progress --show-memory --windows-icon-from-ico=.\use_for_packing\ico.ico --follow-imports --nofollow-import-to=jpype1,jpype,numpy,numba,hpyculator,hpyc_core --enable-plugin=pyside6,numpy --output-dir=out __main__.py
#  --windows-disable-console 

copy-item -path ".\out\__main__.dist" -destination ".\out\lite\bin"  -recurse
copy-item -path ".\background_img" -destination ".\out\lite\background_img"  -recurse
copy-item -path ".\Plugin" -destination ".\out\lite\Plugin"  -recurse
copy-item -path ".\use_for_packing\点我启动.exe" -destination ".\out\lite\点我启动.exe"

upx --best ".\out\lite\bin\__main__.exe"

# must
copy-item -path ".\use_for_packing\packing_must\*"  -destination  ".\out\lite\bin" -recurse
copy-item -path "..\hpyc_core\hpyc_core"  -destination  ".\out\lite\bin" -recurse
copy-item -path "..\..\hpyculatorPackage\hpyculator"  -destination  ".\out\lite\bin" -recurse

# extra
copy-item -path ".\out\lite" -destination ".\out\full" -recurse
copy-item -path ".\use_for_packing\packing_extra\*"  -destination  ".\out\full\bin" -recurse
