; Hello World example for PyMADS
; A simple program that displays "HELLO WORLD" on the screen

    org $2000       ; Start at memory location $2000

    ; Set up display
    lda #$00        ; Load accumulator with 0
    sta $02         ; Store in zero page
    
    ; Print "HELLO WORLD"
    ldx #0          ; Initialize X register as counter
print_loop:
    lda message,x   ; Load character from message
    beq done        ; If zero (end of string), we're done
    jsr $f6a4       ; Call ROM routine to print character
    inx             ; Increment counter
    jmp print_loop  ; Repeat for next character
    
done:
    rts             ; Return from subroutine

message:
    .byte "HELLO WORLD", 0  ; Null-terminated string
