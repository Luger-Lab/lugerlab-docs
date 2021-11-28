import random
import sys

def main():   
    goal_gcs = calc_goal_gcs(length, gc_content)
    bases = make_rand_oligo(length, goal_gcs)
    gc_count = count_gc(bases)
    new_oligo = check_gc(gc_count, goal_gcs, bases) 

def calc_goal_gcs(length, gc_content):
    goal_gcs = int(length*gc_content)
    return goal_gcs

def make_rand_oligo(length, goal_gcs):
    bases = []
    for i in range(length):
        rand_int = random.randint(1, length)
        if rand_int <= goal_gcs:
            if rand_int % 2 == 0:
                new_base = 'G'
            else:
                new_base = 'C'
        else:
            if rand_int % 2 == 0:
                new_base = 'A'
            else:
                new_base = 'T'
        bases.append(new_base)
    return bases

def count_gc(bases):
    gc_count = 0
    for base in bases:
        if base == 'G':
            gc_count += 1
        elif base == 'C':
            gc_count += 1
        else:
            continue
    return gc_count    

def check_gc(gc_count, goal_gcs, bases):
    if gc_count == goal_gcs:
        new_oligo = ''.join(bases)
        print(new_oligo)
        return new_oligo
    else:
        main()

if __name__ == '__main__':
    length = int(sys.argv[1])
    gc_content = (float(sys.argv[2]))/100
    main()
