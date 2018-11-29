# Snapshot Mod Maker

Reorganized some files now that I know how to mod snapshots (thx Pokechu22 <3)

## Process:
- Generate a remapped copy of the source code (basically to find what you need)
- Decompile the obfuscated versions of the classes you want to change
- ``javac -cp <libs> <modified classes>``

## Folders
mc-code
	<version>
		mapped-src
		<mod>
		mappings.tsrg
		mapped-<version>.jar

## TODO
- recomp.py (find a nice way to get from knowing what files do you want to modify to getting the actual obf classes)
- gen_patched_json.py (port it from another project)


## Old Info

This decompiler should work for any version as long as its mappings are available (a printed message with the url is given for manual check), its wip (for now only decompiling and class name renaming is done).


SpecialSource is distributed by https://github.com/md-5/SpecialSource (license: https://github.com/md-5/SpecialSource/blob/master/LICENSE)

Cfr is distributed by http://www.benf.org/other/cfr/ (no source disclosed yet and still in beta) (its under MIT: http://www.benf.org/other/cfr/license.html)


The Srg mappings were kindly provided by skyrising: https://github.com/skyrising/mc-data (its under CC0: https://github.com/skyrising/mc-deobfuscator/blob/02ba679d42000f43cfd74639d74681192bcdb138/base-data/LICENSE.md)

Run "run.bat" or `python decompiler.py` in shell (you will need python 3.6+, ok lets say 3.7 to be sure)
You will need ofc, java jre and jdk (8 is fine) and the version .jar installed either in the regular windows directory (%appdata%/.minecraft/versions/1.13.1/1.13.1.jar and so on)


The program and the files are under MIT license (the cfr ls still property of ben and SpecialSource of md-5). You can credit me or not, your choice.
