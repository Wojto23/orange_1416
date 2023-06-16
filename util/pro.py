from memory_profiler import profile
import tracemalloc


tracemalloc.start()

lista = list(range(1000000))

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)

# @profile
# def my_f():
#     a = [1] * (10 ** 6)
#     b = [2] * (2 * 10 ** 7)
#     del b
#     return a
#
# with open('my_f.txt', 'w') as f:
#     f.write(str(my_f()))

