import timeit

setup = """
output = "some_random_file_name_that_is_long.webp"
IMAGE_EXTENTIONS_LIST = [".png", ".jpg", ".jpeg", ".gif", ".webp"]
IMAGE_EXTENTIONS_TUPLE = (".png", ".jpg", ".jpeg", ".gif", ".webp")
"""

stmt_list_comp = "any([output.endswith(ext) for ext in IMAGE_EXTENTIONS_LIST])"
stmt_gen_expr = "any(output.endswith(ext) for ext in IMAGE_EXTENTIONS_LIST)"
stmt_tuple = "output.endswith(IMAGE_EXTENTIONS_TUPLE)"

n = 1000000

t1 = timeit.timeit(stmt_list_comp, setup=setup, number=n)
print(f"List comprehension (Baseline): {t1:.6f} seconds")

t2 = timeit.timeit(stmt_gen_expr, setup=setup, number=n)
print(f"Generator expression: {t2:.6f} seconds")

t3 = timeit.timeit(stmt_tuple, setup=setup, number=n)
print(f"Tuple (Optimized): {t3:.6f} seconds")
