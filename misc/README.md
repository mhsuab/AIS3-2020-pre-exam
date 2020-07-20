# MISC

## 💤Piquero (solved)

-   Score: 100, Solves: 347

### Problem

![Piquero_99c9aa83fe492df8d52229017d4dca92297c9aeb](piquero/Piquero_99c9aa83fe492df8d52229017d4dca92297c9aeb.jpg)

### Solution

The flag was encoded using ***Braille***.

1.  Find a [Braille decoder](https://www.dcode.fr/braille-alphabet) online to solve the problem.

    ![Braille decoder](../img/Braille decoder.png)

2.  Type down the Braille ciphertext and get `⠠A⠠I⠠S3⠐⠸⠠I-FEEL-SLEEPY-⠠GOOD-⠠NIGHT!!!⠐⠸`.

3.  As the flag format, `AIS3{...}` are given, adjust the result.

    -   ignore all the `⠐ and ⠠`
    -   change `⠸` to `{ or }` and `-` to `_`



#### NOTES

This problem is quite easy but since there are many way of braille decoding. It’s hard to find the one that the problem setter used. Therefore, I took several attempts to get the exact flag.



## 🐥Karuego (unsolved)

-   Score: 100, Solves: 245

### problem

![Karuego_0d9f4a9262326e0150272debfd4418aaa600ffe4](karuego/Karuego_0d9f4a9262326e0150272debfd4418aaa600ffe4.png)

### Solution

1.  Check the filetype of the image.

    ![karuego file](../img/karuego file.png)

    ➜ correspond to the extension

2.  `binwalk` to check for any file within the image and extract them.

    `binwalk -e Karuego_0d9f4a9262326e0150272debfd4418aaa600ffe4.png`

    

    ***Find out the all the files need password and get stuck.***

3.  



## 🌱Soy (solved)

-   Score: 139, Solves: 172



### Problem

![Soy_b692c44dd2a32b30eee8a9315091d79f7dd8c8a8](soy/Soy_b692c44dd2a32b30eee8a9315091d79f7dd8c8a8.png)



### Solution

**Target**: recover the QR code



Recover the QR code with the help of the [webpage](https://merricx.github.io/).

1.  Choose the version that fit the given QR code.

    ![soy new](../img/soy new.png)

2.  Fill the as much pixel in black and whie as possible.

    ![soy after](../img/soy after.png)

3.  Use **Tools**, *Extract QR Information*, then the it can decode the hidden information in the QR code and find the flag.



#### NOTES

The problem is quite easy after finding the tool for extracting the decoded information within the QR code. However, before knowning it, it’s a bit difficult to learn how the QR code encode from zero.







