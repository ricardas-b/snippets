import pytest



def climbing_stairs_in_one_two_steps(n):
    ''' Calculate the number of different ways to climb stairs with <n> number of steps,
        making either one or two steps at a time '''

    counter = [0] * (n + 1)
    counter[0] = 1

    if n > 0:
        counter[1] = 1

    for i in range(2, n+1):
        counter[i] = counter[i-1] + counter[i-2]

    return counter[n]



def climbing_stairs_in_one_two_three_steps(n):
    ''' Calculate the number of different ways to climb stairs with <n> number of steps,
        making either one, two or three steps at a time '''

    counter = [0] * (n + 1)
    counter[0] = 1

    if n > 0:
        counter[1] = 1

    if n > 1:
        counter[2] = 2

    for i in range(3, n+1):
        counter[i] = counter[i-1] + counter[i-2] + counter[i-3]

    return counter[n]



def climbing_stairs_in_k_steps(n, k):
    ''' Calculate the number of different ways to climb stairs with <n> number of steps,
        making <k> steps at a time '''

    counter = [0] * (n + 1)
    counter[0] = 1

    if n > 0:
        counter[1] = 1

    for i in range(2, n+1):
        for j in range(1, k+1):
            if i-j < 0:
                continue

            counter[i] += counter[i-j]

    return counter[n]






@pytest.mark.parametrize('number_of_steps, expected_paths', [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (50, 20365011074)])
def test_climbing_stairs_in_one_two_steps(number_of_steps, expected_paths):
    calculated_paths = climbing_stairs_in_one_two_steps(number_of_steps)
    assert calculated_paths == expected_paths


@pytest.mark.parametrize('number_of_steps, expected_paths', [(0, 1), (1, 1), (2, 2), (3, 4), (4, 7), (50, 10562230626642)])
def test_climbing_stairs_in_one_two_three_steps(number_of_steps, expected_paths):
    calculated_paths = climbing_stairs_in_one_two_three_steps(number_of_steps)
    assert calculated_paths == expected_paths


@pytest.mark.parametrize('number_of_steps, allowed_steps, expected_paths', [(0, 1, 1), (5, 2, 8), (10, 10, 512)])
def test_climbing_stairs_in_k_steps(number_of_steps, allowed_steps, expected_paths):
    calculated_paths = climbing_stairs_in_k_steps(number_of_steps, allowed_steps)
    assert calculated_paths == expected_paths
