from linear_hashing import LinearHashing
import numpy as np
import time


if __name__ == '__main__':
    lh = LinearHashing()
    num_of_elements = 5000000
    random_numbers = list(np.random.randint(-10000, 10000, num_of_elements))
    
    start_time = time.time()

    for num in random_numbers:
        lh.insert(num)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Insertion time: {execution_time} seconds for {num_of_elements} elements\n")

    random_numbers = random_numbers[:num_of_elements//2]
    np.concatenate((random_numbers, np.random.randint(-10000, 10000, num_of_elements//2)))  # concaetnate numbers that probably are not in the hash table

    # Visualize the buckets
    # for i,bucket in enumerate(lh.buckets):
    #     print(f'Bucket {i}: {bucket}')

    # print(lh.round, lh.next_bucket)
    

    start_time = time.time()

    for num in random_numbers:
        if (lh.element_exists(num) == False):
            # print(f"Element {num} not found")
            # print(lh.find_bucket_index(num))
            pass

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Find time: {execution_time} seconds for {num_of_elements} elements")


