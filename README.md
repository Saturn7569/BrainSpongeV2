# BrainSponge V2

An esoteric joke language

## What is BrainSponge?

BrainSponge is a superset to BrainF\*\*k (every BrainF\*\*k program is a valid BrainSponge program).

This is V2.
I made V1 a loong time ago and it was pretty bad so I remade it as V2

## How does it work?

BrainSponge has only a few commands.
You start with a 256 long array of bytes (I know it was 30 000 in BrainF\*\*k but I changed it) and a pointer.
The pointer starts at zero and you can manipulate it using one character long commands.

### Commands

Here is a list of the commands:

- `+`: increment the current value by 1
- `-`: decrement the current value by 1
- `>`: move the pointer to the right
- `<`: move the pointer to the left
- `.`: output the current character as ascii
- `[`: start a loop (the program will loop until the current character is 0)
- `]`: end a loop
- `;`: output the current number followed by a space (eg. `"75 "`)

### Example program

```
++++++++[>+++++++++<-]>.
<+++++[>++++++<-]>+++.
```
If we now run this code we will get this:
```
Hi
```

### Explanation

So we want to print `Hi`.
To do this, we need the ASCII values of all the letters for `Hi` they are `72` and `105`.
We need to get one of the memory cells to `72` and `105`.
Now we could just insert 72 times + but we can use loops.
