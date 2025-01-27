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