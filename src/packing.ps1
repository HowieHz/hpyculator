
nuitka --mingw64 --standalone --quiet --show-progress --show-memory --follow-import-to=utils --nofollow-import-to=jpype1,jpype,numpy,numba --enable-plugin=pyside6,numpy --output-dir=out __main__.py
#  --windows-disable-console 

copy-item -path ".\out\__main__.dist" -destination ".\out\lite\bin"  -recurse
copy-item -path ".\background_img" -destination ".\out\lite\background_img"  -recurse
copy-item -path ".\Plugin" -destination ".\out\lite\Plugin"  -recurse
copy-item -path ".\use_for_packing\点我启动.exe" -destination ".\out\lite\点我启动.exe"

upx --best ".\out\lite\bin\__main__.exe"

copy-item -path ".\out\lite" -destination ".\out\full" -recurse
copy-item -path ".\use_for_packing\打包所需\*"  -destination  ".\out\full\bin" -recurse
