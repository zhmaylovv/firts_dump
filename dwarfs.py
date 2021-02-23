from CodewarsTest import Test

def get_number_of_boats(dwarfs, limit):
    counter = 0
    dwarfs.sort(reverse=True)
    while dwarfs:
        the_one = dwarfs.pop(0)
        if dwarfs:
            add = 1
            for i in range(len(dwarfs)):
                if the_one + dwarfs[i] <= limit:
                    dwarfs.pop(i)
                    counter += 1
                    add = 0
                    break
            if add:
                counter += 1
        else:
            counter += 1
    return counter

Test.assert_equals(get_number_of_boats([59, 1, 58, 1, 3, 59, 4], 60), 4)
Test.assert_equals(get_number_of_boats([3, 3, 3, 1, 3, 4, 4], 4), 6)
Test.assert_equals(get_number_of_boats([5, 6, 7, 8, 9, 4], 10), 5)
Test.assert_equals(get_number_of_boats([3, 2, 2, 1], 3), 3)
Test.assert_equals(get_number_of_boats([6, 7, 8, 9, 1, 1, 2], 11), 3)