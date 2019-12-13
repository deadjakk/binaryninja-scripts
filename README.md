# binaryninja-scripts
## r2func2bin.py
---

A short script that autoruns and parses the output of `rabin2 -sr <binary_name>` 
after which, takes the function names and corresponding addresses and updates the
symbols for the current binaries

Useful since binja doesn't like to recognize/resolve some functions appropriately in ARM MSB
[bug link](https://github.com/Vector35/binaryninja-api/issues/1471)

To use: be sure not to use while in a bndb file, if you so wish, you can edit the very simple
script and hardcode your desired binary address
Anywho, place in plugins folder, tools> "import r2 function names"
