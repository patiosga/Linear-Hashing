class Bucket:
    def __init__(self, capacity=5):  # each bucket has a default capacity of 10
        self.capacity = capacity
        self.prim_pages = []
        self.overflow_pages = []
        self.next_insert = 0
        # pointer to the next insert location (if there is space in the primary pages, 
        # it will be the next insert location, otherwise it will be the first location in the overflow pages)

    def insert(self, element):
        """
        This function inserts an element into the bucket.
        Args:
            element: The element to insert.
        Returns:
            True if the element was inserted into the primary pages, False otherwise.
        """
        if self.next_insert < self.capacity:
            self.prim_pages.append(element)
            self.next_insert += 1
            return True
        else:
            self.overflow_pages.append(element)
            return False

    def delete(self, element):
        '''
        This function deletes an element from the bucket.
        Args:
            element: The element to delete.
        Returns:
            True if the is deleted, False if it is not found.'''
        if element in self.prim_pages:
            self.prim_pages.remove(element)
            self.next_insert -= 1
            return True
        elif element in self.overflow_pages:
            self.overflow_pages.remove(element) 
            return True
        else:
            return False

    def find(self, element):
        '''
        This function finds an element in the bucket.
        Args:
            element: The element to find.
        Returns:
            True if the element was found, False otherwise.
        '''
        if element in self.prim_pages:
            return True
        elif element in self.overflow_pages:
            return True
        else:
            return False
        

    def __str__(self):
        return "Primary pages: " + self.prim_pages + "\nOverflow pages: "+ self.overflow_pages