# [CS 12 24.2] Lab 0a - The Smoking Pearl

# Solution

As described in the problem statement, we should simulate Pearl smoking
with loops. This is relatively straightforward to implement:

```python
# pyright: strict
def pearl_smoke_count(n: int, k: int):
    cigs: int = n
    butts: int = 0
    total_smoked: int = 0
    while cigs > 0:
        total_smoked += cigs
        butts += cigs
        cigs, butts = divmod(butts, k)
    return total_smoked
```
Parameters:
- `n` - the number of cigarettes Pearl initially has
- `k` - the number of cigarette butts Pearl needs to make one (1) new
        cigarette

## Line-by-line explanation

We start the file with `#pyright: strict` to ensure that we do type
checking. Then, we start defining the function `pearl_smoke_count` (note
that the parameters are type-annotated):
```python
# pyright: strict
def pearl_smoke_count(n: int, k: int):
```

We define some initial variables to keep track of Pearl's current state
of affairs:
```python
    cigs: int = n
    butts: int = 0
    total_smoked: int = 0
```
- `cigs` - the number of cigarettes available for Pearl to smoke.
           Note that we set this to `n`.
- `butts` - the number of cigarette butts Pearl currently has.
- `total_smoked` - the number of cigarettes Pearl has finished smoking.

Note the use of type hints for the variable initializations. This is not
strictly required, but it helps make the code clearer.


Then, we implement the main loop of the function. First, we check if
there are any cigarettes available for Pearl to smoke:
```python
    while cigs > 0:
        ...
```
If not, we exit the main loop and return `total_smoked`.

Next, we simulate Pearl smoking all the available cigarettes (`cigs`) by
updating the variables accordingly:
```python
    total_smoked += cigs
    butts += cigs
```

Then comes the _magic_. We create one cigarette per every `k` butts,
which can be done with division. Then, the remainder, or the leftover
butts which can't be made into a new cigarette, remain butts.
```python
        cigs, butts = divmod(butts, k)
```
We make use of the Python built-in `divmod` function to make the code
cleaner. You could also write the following:
```python
        cigs = butts // k  # creating new cigarettes
        butts = butts % k  # getting leftover butts
```
Then, the main loop starts again. The loop continues until we have no
more cigarettes left to smoke.

Note that we may still have some cigarette butts leftover, but we can't
reconstitute them into a new cigarette.

The last line returns the total number of cigarettes smoked:
```python
    return total_smoked
```