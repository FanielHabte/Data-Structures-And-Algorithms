# Array Algorithms — Study Reference

> **Core idea behind all four algorithms:** An array is a row of fixed slots in memory.
> You cannot add or remove slots — you can only copy values between them, expand into a new array, or overwrite a slot.
> Every algorithm below is just a smart sequence of copies.

---

## Algorithm 1 - Shift All Elements One Step Left (Rotation)

### What it does
Moves every element one slot to the left. The first element wraps around to the end.

### The mental model
Think of a conveyor belt. Every item slides one position left. The item that falls off the left end gets placed back on the right end.

```
Before:  [ 1 | 2 | 3 | 4 | 5 ]
After:   [ 2 | 3 | 4 | 5 | 1 ]
```

### Why left → right loop order?
You read from the **right neighbor** and write to the **left**. Going left to right means each slot you write to has already been evacuated. If you went right to left, you would overwrite a value before copying it.

### The plan
1. Save the first value — it will be overwritten by the loop
2. Loop from index `0` to `n-2`, copying the right neighbor into the current slot
3. Place the saved value into the last slot

### Why stop at n-2?
The loop reads from `i + 1`. If `i` reached the last index, it would try to read one slot past the end — out of bounds. Stop one short and handle the last slot manually.

---

## Algorithm 2 - Delete Element at Index i, Shift Left

### What it does
Removes the value at a given index and closes the gap by pulling all elements to its right one step left. The last slot is set to `0`.

### The mental model
Think of seats in a row. Someone in the middle leaves. Everyone to their right slides one seat left to fill the gap. The last seat is now empty.

```
Before:  [ 1 | 2 | 3 | 4 | 5 ]   delete at index 2
After:   [ 1 | 2 | 4 | 5 | 0 ]
```

### Why left → right loop order?
Same reason as Algorithm 1 — you are pulling values left, so the destination slot is always one that has already been vacated.

### The plan
1. Start the loop at the deletion index — elements to the left don't move
2. Loop from `index` to `n-2`, copying the right neighbor into the current slot
3. Set the last slot to `0`

### Key upgrade from Algorithm 1
The loop starts at `index`, not `0`. The further right the deletion point, the fewer iterations needed. Elements to the left are completely untouched.

---

## Algorithm 3 - Add a Number to the End

### What it does
Appends a new value to the end of the list by creating a new list one slot larger, then writing the value into the last slot.

### The mental model
An array is a fixed block of memory — you cannot grow it in place. You allocate a new, larger block and write the new value into the extra slot at the end.

```
Before:  [ 1 | 2 | 3 | 4 ]
After:   [ 1 | 2 | 3 | 4 | 5 ]
```

### The plan
1. Create a new list by extending the original with one placeholder slot (`0`)
2. The new slot sits at index `len(original)` — one past the last valid index
3. Write the new value directly into that slot
4. Return the new list — the original is untouched

### No loop needed
There is nothing to shift. The new slot is already at the correct position. This is the simplest of the four.

### The index insight
If the original list has `n` elements, valid indices are `0` through `n-1`. `len(original)` equals `n` — exactly the index of the new slot.

---

## Algorithm 4 - Insert a Number at Index i (Shift Right)

### What it does
Places a new value at a specific index. Every element at that index and to its right shifts one step right to make room.

### The mental model
A new person joins a row of seats in the middle. Everyone from that seat rightward slides one seat right. The last person must move first — otherwise you overwrite someone before they have moved.

```
Before:  [ 1 | 2 | 3 | 4 ]         insert 99 at index 2
After:   [ 1 | 2 | 99 | 3 | 4 ]
```

### Why right → left loop order?
This is the critical reversal from Algorithms 1 and 2. You are shifting right, so each slot must be vacated before you write into it — which means working from the rightmost slot backwards. Going left to right would copy the same value all the way to the end, silently destroying data.

### The plan
1. Create a new list by extending the original with one placeholder slot
2. Loop from the last slot down to `index + 1`, copying the left neighbor into the current slot
3. Write the new value into the now-open slot at `index`
4. Return the new list

### Why stop at index + 1 (exclusive)?
When `i = index + 1`, the loop copies the value at `index` one step right — that's the last useful move. If the loop continued to `i = index`, it would copy the left neighbor into the gap you just opened, clobbering it a moment before you overwrite it with the new value anyway.

---

## Comparison Table

| Algorithm | Loop direction | Loop start | Loop stop | Reads from | Last slot |
|---|---|---|---|---|---|
| Shift all left | → left to right | `0` | `n - 2` | `i + 1` right neighbor | Place saved first value |
| Delete at i, shift left | → left to right | `index` | `n - 2` | `i + 1` right neighbor | Set to `0` |
| Add to end | no loop | — | — | — | Write new value directly |
| Insert at i, shift right | ← right to left | `n` | `index + 1` | `i - 1` left neighbor | Write new value at `index` |

---

## Reading the Table - The One Rule That Ties It All Together

**The loop direction is always determined by which neighbor you read from.**

- Reading from the **right neighbor** (`i + 1`) → loop **left to right**
  The destination slot is always one the previous iteration already vacated.

- Reading from the **left neighbor** (`i - 1`) → loop **right to left**
  The destination slot is always one the previous iteration already vacated.

Going in the wrong direction silently destroys data — you read a value you already overwrote, with no error message.

The start and stop points simply reflect where the action begins and ends:
- Left-shift operations start at the target and stop before the last slot, which is handled manually.
- Right-shift operations start at the last slot and stop just after the target, which is handled manually.
- The "no loop" case is what happens when there is nothing to shift — the new slot is already in the right place.