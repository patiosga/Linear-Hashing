from linear_hashing import LinearHashing
import random
import time


if __name__ == '__main__':
    lh = LinearHashing()
    num_of_elements = 5000000
    random_numbers = [random.randint(-10000, 10000) for _ in range(num_of_elements)]
    
    start_time = time.time()

    for num in random_numbers:
        lh.insert(num)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Insertion time %f seconds for %d elements\n" % (execution_time, num_of_elements))

    random_numbers = random_numbers[:num_of_elements//2]
    random_numbers += [random.randint(-10000, 10000) for _ in range(num_of_elements//2)]

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
    print("Search time %f seconds for %d elements\n" % (execution_time, num_of_elements))


