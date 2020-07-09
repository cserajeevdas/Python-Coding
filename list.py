def main():
    seq = range(10)
    print("\nActual list")
    print_list(seq)

    print("\nNewly generated 2x list with even numbers")
    seq_2x = [x*2 for x in seq if x%2==0]
    print_list(seq_2x)

    print("\nNewly generated 2x list with even numbers")
    seq_2x_even = [x*2 for x in seq if x%2==0]
    print_list(seq_2x_even)

    print('\nNewly generated 2x touples')
    seq_touple = [(x, x*2) for x in seq]
    print_list(seq_touple)

    print('\nNewly generated pi')
    from math import pi
    seq_pi = [round(pi, i) for i in seq]
    print_list(seq_pi)

#create a map out of list
    print('\nNewly generated map from list')
    seq_map = { x: x**2 for x in seq }
    print(seq_map)

def print_list(objectx):
    for x in objectx:
        print(x, end=' ')
if __name__ == '__main__':
    main()
