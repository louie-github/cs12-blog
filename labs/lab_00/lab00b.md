# [CS 12 24.2] Lab 0b - CS 12

# Solution
The full code for the solution can be found at the end of the page. For
now, let's build up the solution from scratch.

According to the problem statement, the following equation holds true
for all $n >= 8$:
$$
c_n = 72c_{n-1} - 1296c_{n-2} - 3c_{n-4} + 108c_{n-5} - 2c_{n-8}
$$
Luckily, we don't have to prove this statement, so let's just implement
it as-is.

We see that the equation is a ***recursive*** formula, because it
depends on the results of its preceding terms. For example, $c_n$
depends on the results of $c_{n-1}$, $c_{n-2}$, $c_{n-4}$, $c_{n-5}$,
and $c_{n-8}$.

Calling back to our CS 11 lectures on recursion, let's implement the
formula through **wishful thinking**!

How? First, we assume the problem is solved. That is, we can already
calculate $c_n$ for any $n$. In programming terms, this means that we
assume that the function `cs12_string_count` already works.

Then, we define the function `cs12_string_count` as follows:
```python
def cs12_string_count(n: int):
    return (
        72 * cs12_string_count(n - 1)
        - 1296 * cs12_string_count(n - 2)
        - 3 * cs12_string_count(n - 4)
        + 108 * cs12_string_count(n - 5)
        - 2 * cs12_string_count(n - 8)
    )
```
This is a direct translation of the above formula.

If we run the code as-is, we see that it becomes an infinite loop; the
program never terminates. This is because we haven't defined any
_base cases_ for our recursive function. Let's go and do that!

First, we have to identify what our base cases actually are. We see that
the recursive formula only holds true for all $n >= 8$, so a good place
to start is assuming that we should implement base cases for all $n <= 7$.

## Important note
In the following cases, we will only be concerned with finding the
number of substrings $n$ characters consisting of uppercase English
letters or digits that contain `CS12` as a substring, but ***we will not
check for strings that contain `CS11` as a substring***. Why?

Let's imagine for a while that `s` is a string $n$ characters long,
where $n <= 7$. Assume that `s` contains `CS12` as a substring, but also
contains `CS11` as a substring. This is the type of string we need to
filter out or take into account.

But notice as well that there is **no possible way** for a string less
than or equal to 7 characters long to contain _both_ `CS11` and `CS12`
as substrings.

We cannot put them next to each other, as `CS11CS12` would be eight (8)
characters long. Since they do not share a starting or ending letter,
we cannot make them "share" a letter in the middle. For example, `CS11`
and `21SC` are both substrings of the string `21SCS11`, which is 7
characters long.

This makes our lives simpler, as we only have to worry about the
substring `CS12`.

### Case: $n <= 3$

To make things simpler, let's start with the lowest case: $n = 0$.
We ask the question:

> How many strings of uppercase alphanumeric characters of length **0**
> contain the substring `CS12`, but not `CS11`?

It should hopefully be obvious that the answer is zero (0).

In fact, for any $n < 4$, the answer to the question is zero (0). Why?
Notice that `CS12` is four characters long. Then, by definition, any
string less than four characters long cannot contain the substring
`CS12`, because a substring cannot have more characters than its
contaning string.

Therefore, we can implement these cases as follows:
```python
    if n <= 3:
        return 0
```
Note that we write `n <= 3` instead of `n < 4`. This is to make the code
clearer as we add the next few cases.


### Case: $n = 4$

Now, we handle the case of $n = 4$. Hopefully, it should also be obvious
that the answer is **one (1)**. There is only one string four (4)
characters long that contains the substring `CS12`, namely, the string
`"CS12"`.

We then implement this case accordingly:
```python
    elif n == 4:
        return 1
```

### Case: $n = 5$
Now we get to the harder cases. Let's break down 

Notice that there are two (2) ways of "positioning" the substring `CS12`
within a string five characters long.