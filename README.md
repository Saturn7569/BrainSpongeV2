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
Whatever is inside a loop will loop until the cell the loop ends at is 0.
Using this we can use one cell as a counter, move to it at the end of the loop and subtract from it so the loop happens only a limited ammount of times.

In order to get `72` we can get it's square root which is around `8.5`. If we now divide 72 by 8 we will get `9`.
That means that we need to loop 8 times and increment the cell by 9.

Coding this, we can use the _first_ cell as the counter and the _second_ as the actual character.

```
Increment the current by 8
++++++++
Start a loop
[
    Move left
    >
    Increment by 9
    +++++++++
    Move back and decrement the counter
    <-
]
Move back to the actual character and output it
>.
```

Running this will print the capital `H`.

We can follow the same steps for the second letter but this time we don't have to do 105 but only 33 since 72 is already in the character cell.

```
Move back to the counter cell
<
Increment by 5
+++++
Start a loop
[
    Move right
    >
    Increment the character by 6
    ++++++
    Move back and decrement the counter
    <-
]
This loop puts 102 in the character cell
Move to the character cell
>
Increment by 3 to set the cell to 105
+++
Output the character
.
```

Here is the full code with comments:

```
Increment the current by 8
++++++++
Start a loop
[
    Move left
    >
    Increment by 9
    +++++++++
    Move back and decrement the counter
    <-
]
Move back to the actual character and output it
>.

Move back to the counter cell
<
Increment by 5
+++++
Start a loop
[
    Move right
    >
    Increment the character by 6
    ++++++
    Move back and decrement the counter
    <-
]
This loop puts 102 in the character cell
Move to the character cell
>
Increment by 3 to set the cell to 105
+++
Output the character
.
```
