#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Tyrell Williams, with help from Mike'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits = bits.strip('0')
    bits_timing = (min([len(element)
                   for element in bits.split('1') +
                   bits.split('0') if element]))
    new_bits = (bits.replace('0000000' * bits_timing, '   ')
                .replace('111' * bits_timing, '-')
                .replace('1' * bits_timing, '.')
                .replace('000' * bits_timing, ' ')
                .replace('0' * bits_timing, ''))
    return new_bits


def decode_morse(morse):
    morse_code = morse.strip().split('   ')
    letters = []
    for morse_word in morse_code:
        chars = morse_word.split(' ')
        for char in chars:
            letters.append(MORSE_2_ASCII[char])
        letters.append(' ')
    print(''.join(letters).strip())
    return ''.join(letters).strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
