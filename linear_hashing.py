from bucket import Bucket


class LinearHashing:
    def __init__(self, d_0 = 2):  # initial number of buckets to 2^d_0
        self.round = 0  # using hash functions h_round and h_{round+1}
        self.next_bucket = 0  # pointer to next bucket to insert / 0 to next - 1 buckets have been split in this round
        self.d_0 = d_0  # number of buckets - d0 = 2 where i look for the 2^d_i last bits to calculate h_i

        self.dr_powered = 2 ** (d_0 + self.round)  # number of buckets / to not calculate it every time in hash function
        self.dr_powered_2 = 2 ** (d_0 + self.round + 1)

        self.buckets = [Bucket() for _ in range(self.dr_powered)]  # list of buckets


    def hash_func(self, x, d_i):
        """
        This function applies a simple hash function using XOR.
        Args:
            x: The integer to hash.
        Returns:
            The hash value of the integer.
        """
        x1 = x & 0xFFFF  # Isolate lower 16 bits
        x2 = (x >> 16) ^ x1  # Isolate upper 16 bits and XOR with lower bits
          
        # get last `d_i` bits of x2 in integer form - short of
        # d_i is a power of 2 in this function / implementation
        return x2 % (d_i)  
    

    def insert(self, element):
        """
        This function inserts an element into the linear hashing structure.
        Args:
            element: The element to insert.
        """
        index = self.find_bucket_index(element)
        if (self.buckets[index].insert(element) == False):  # if the element was not inserted in the primary pages
            self.split_next_bucket()  # split bucket pointed be next_bucket

        
    def split_next_bucket(self):
        """
        This function splits the next bucket in the linear hashing structure.
        """
        
        bucket_to_split = self.buckets[self.next_bucket]

         # Update next_bucket and round
        self.next_bucket += 1  # move next_bucket pointer to the next bucket

        temp_pages = bucket_to_split.prim_pages + bucket_to_split.overflow_pages  # merge all pages to a temporary list
        del bucket_to_split.prim_pages[:]  # clear all pages
        del bucket_to_split.overflow_pages[:]
        bucket_to_split.next_insert = 0  # reset next_insert pointer
        
        self.buckets.append(Bucket())  # split image of next bucket
        # print(f"Splitting bucket {self.next_bucket - 1} into bucket {len(self.buckets) - 1}")
        for element in temp_pages:
            index = self.find_bucket_index(element) # find new bucket index (same or new bucket)
            # print(f"Element {element} goes to bucket {index}")
            self.buckets[index].insert(element) # insert element in corresponding bucket (indicated by index)

        # Check for new round
        if (self.next_bucket == self.dr_powered):  # if all buckets have been split in this round
            self.next_bucket = 0  # new round
            self.round += 1  # increase 
            self.dr_powered = 2 ** (self.d_0 + self.round)  # update number of buckets
            self.dr_powered_2 = 2 ** (self.d_0 + self.round + 1)

    
    def find_bucket_index(self, element):
        '''
        This function finds the index of the bucket where the element should be inserted / exist.
        Args:
            element: The element to insert / find.
        Returns:
            The index of the bucket.'''
        
        hash_value = self.hash_func(element, self.dr_powered)  # using h_round
        # print(f"Hash value for element {element}: {hash_value} (next bucket: {self.next_bucket})")
        if (hash_value < self.next_bucket):  # if the hash value is smaller than the next bucket index, it means that the bucket has been split in this round
            return self.hash_func(element, self.dr_powered_2)  # using h_{round+1}
        else:
            return hash_value  # using h_round
        


    def element_exists(self, element):
        '''
        This function checks if an element exists in the linear hashing structure.
        Args:
            element: The element to check.
        Returns:
            True if the element exists, False otherwise.
        '''
        index = self.find_bucket_index(element)
        return self.buckets[index].find(element)