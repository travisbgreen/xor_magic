# xor_magic
brute forces single byte xor and uses libmagic to try to ID the output

### sample output:
```
$ ~/scripts/xor_magic.py xor_blob 
key: 0x30
Sendmail frozen configuration  - version #3#lai\011??,Wzsf#,@bwbold\011,Sbdfp#1#3#Q==\011fmglai\0111#3#lai\011??,Wzsf#,
00000000: 26 53 47 45 2E 32 2D 37  09 26 E2 EA E8 D0 09 32  &SGE.2-7.&.....2
00000010: 23 33 23 6C 61 69 09 3F  3F 2C 57 7A 73 66 23 2C  #3#lai.??,Wzsf#,
None
key: 0x33
PDF document, version 1.4
00000000: 25 50 44 46 2D 31 2E 34  0A 25 E1 E9 EB D3 0A 31  %PDF-1.4.%.....1
00000010: 20 30 20 6F 62 6A 0A 3C  3C 2F 54 79 70 65 20 2F   0 obj.<</Type /
None
key: 0x59
Solitaire Image Recorder format
00000000: 4F 3A 2E 2C 47 5B 44 5E  60 4F 8B 83 81 B9 60 5B  O:.,G[D^`O....`[
00000010: 4A 5A 4A 05 08 00 60 56  56 45 3E 13 1A 0F 4A 45  JZJ...`VVE>...JE
```
