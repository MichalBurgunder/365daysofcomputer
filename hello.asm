.text
.align 2
.globl _main

_main:
    stp x29, x30, [sp, #-16]!
    mov x29, sp

    adrp x0, msg@PAGE
    add  x0, x0, msg@PAGEOFF
    bl _printf

    mov w0, #0

    ldp x29, x30, [sp], #16
    ret

.section __TEXT,__cstring
msg:
    .asciz "Hello there!\n"


;  as hello.asm -o hello.o
; clang hello.o -o hello
; ./hello