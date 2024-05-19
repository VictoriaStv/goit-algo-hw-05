import timeit

def boyer_moore(text, pattern):
    pass  


def knuth_morris_pratt(text, pattern):
    pass  


def rabin_karp(text, pattern):
    pass  

def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


article1 = open("article1.txt", "r").read()
article2 = open("article2.txt", "r").read()

existing_pattern = "pattern"  
non_existing_pattern = "xyz" 

boyer_moore_time_article1_existing = measure_time(boyer_moore, article1, existing_pattern)
knuth_morris_pratt_time_article1_existing = measure_time(knuth_morris_pratt, article1, existing_pattern)
rabin_karp_time_article1_existing = measure_time(rabin_karp, article1, existing_pattern)


boyer_moore_time_article1_non_existing = measure_time(boyer_moore, article1, non_existing_pattern)
knuth_morris_pratt_time_article1_non_existing = measure_time(knuth_morris_pratt, article1, non_existing_pattern)
rabin_karp_time_article1_non_existing = measure_time(rabin_karp, article1, non_existing_pattern)


boyer_moore_time_article2_existing = measure_time(boyer_moore, article2, existing_pattern)
knuth_morris_pratt_time_article2_existing = measure_time(knuth_morris_pratt, article2, existing_pattern)
rabin_karp_time_article2_existing = measure_time(rabin_karp, article2, existing_pattern)


boyer_moore_time_article2_non_existing = measure_time(boyer_moore, article2, non_existing_pattern)
knuth_morris_pratt_time_article2_non_existing = measure_time(knuth_morris_pratt, article2, non_existing_pattern)
rabin_karp_time_article2_non_existing = measure_time(rabin_karp, article2, non_existing_pattern)

# Результатм
print("Час виконання для алгоритму Боєра-Мура:")
print("Стаття 1, підрядок, який існує:", boyer_moore_time_article1_existing)
print("Стаття 1, вигаданий підрядок:", boyer_moore_time_article1_non_existing)
print("Стаття 2, підрядок, який існує:", boyer_moore_time_article2_existing)
print("Стаття 2, вигаданий підрядок:", boyer_moore_time_article2_non_existing)
print()

print("Час виконання для алгоритму Кнута-Морріса-Пратта:")
print("Стаття 1, підрядок, який існує:", knuth_morris_pratt_time_article1_existing)
print("Стаття 1, вигаданий підрядок:", knuth_morris_pratt_time_article1_non_existing)
print("Стаття 2, підрядок, який існує:", knuth_morris_pratt_time_article2_existing)
print("Стаття 2, вигаданий підрядок:", knuth_morris_pratt_time_article2_non_existing)
print()

print("Час виконання для алгоритму Рабіна-Карпа:")
print("Стаття 1, підрядок, який існує:", rabin_karp_time_article1_existing)
print("Стаття 1, вигаданий підрядок:", rabin_karp_time_article1_non_existing)
print("Стаття 2, підрядок, який існує:", rabin_karp_time_article2_existing)
print("Стаття 2, вигаданий підрядок:",rabin_karp_time_article2_existing)