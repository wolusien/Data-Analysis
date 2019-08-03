import numpy as np

bound_limit = 10e-8
def logloss(p, y):
    p = max(min(p, 1. - bound_limit), bound_limit)
    return -np.log(p) if y == 1. else -np.log(1. - p)

def magic(*args, **kwargs):
    print ("unnamed args: ", args)
    print ("keyword args: ", kwargs)
    # prints
    # unnamed args: (1, 2)
    # keyword args: {'key2': 'word2', 'key': 'word'}

def other_way_magic(x, y, z):
    return x + y + z

def f2(x, y):
    return x + y

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g
   

def main():
    four_with_replacement = [np.random.choice(range(10)) for _ in range(4)]
    print(np.random.choice(range(10)))
    print(four_with_replacement)
    magic(1, 2, key="word", key2="word2")
    x_y_list = [1, 2]
    z_dict = { "z" : 3 }
    print(other_way_magic(*x_y_list, **z_dict))
    g = doubler_correct(f2)
    print(g(1, 2)) # 6 
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    print(xs)
    for j,v in enumerate(movies):
        print(j,v)

if __name__ == '__main__':
    main()