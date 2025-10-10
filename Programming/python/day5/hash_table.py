"""
Custom Hash Table Implementation with Chaining
Day 5 - Project 1

YOUR MISSION: Build a hash table from scratch!

You'll implement:
1. _hash() - Convert keys to array indices
2. insert() - Add         index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]with collision handling
3. search() - Find items in O(1) average time
4. delete() - Remove items
5. _resize() - Grow the table when it gets too full

Ready? Let's code! 🚀
"""

class HashTable:
    """
    Custom hash table implementation using chaining for collision resolution.
    """
    
    def __init__(self, initial_size=8):
        """Initialize the hash table."""
        self.size = initial_size
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        self.collisions = 0
    
    def _hash(self, key):
        """
        TODO #1: Implement hash function
        
        Convert a key to an array index.
        
        Algorithm:
        1. Convert key to string: key_str = str(key)
        2. Sum ASCII values: hash_value = sum(ord(char) for char in key_str)
        3. Return: hash_value % self.size
        
        Example:
            key = "cat"
            ASCII: 'c'=99, 'a'=97, 't'=116
            Sum: 99 + 97 + 116 = 312
            Index: 312 % 8 = 0
        
        Args:
            key: The key to hash
            
        Returns:
            int: Index in range [0, size-1]
        """
        key_str = str(key)
        hash_value = (sum(ord(char) for char in key_str))
        return hash_value % self.size
    
    def _load_factor(self):
        """Calculate current load factor."""
        return self.count / self.size
    
    def _resize(self):
        """
        TODO #2: Implement table resizing
        
        When load factor > 0.7, double the table size and rehash all items.
        
        Algorithm:
        1. Print resize message (for visibility)
        2. Save old buckets: old_buckets = self.buckets
        3. Double the size: self.size *= 2
        4. Create new empty buckets: self.buckets = [[] for _ in range(self.size)]
        5. Reset counters: self.count = 0, self.collisions = 0
        6. Rehash all items:
           - for bucket in old_buckets:
               - for key, value in bucket:
                   - self.insert(key, value)
        
        Args:
            None
            
        Returns:
            None
        """
        print(f"📈 Resizing table from {self.size} to {self.size * 2} buckets...")
        
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        self.collisions = 0

        #rehash all items
        for bucket in old_buckets:
            for key,value in bucket:
                self.insert(key,value)
            

    
    def insert(self, key, value):
        """
        TODO #3: Implement insert operation
        
        Insert or update a key-value pair.
        
        Algorithm:
        1. Get bucket index: index = self._hash(key)
        2. Get the bucket: bucket = self.buckets[index]
        3. Check if key already exists:
           - for i, (k, v) in enumerate(bucket):
               - if k == key:
                   - bucket[i] = (key, value)  # Update
                   - return False
        4. If not found, append: bucket.append((key, value))
        5. Increment count: self.count += 1
        6. Track collision: if len(bucket) > 1: self.collisions += 1
        7. Check load factor: if self._load_factor() > 0.7: self._resize()
        8. return True
        
        Args:
            key: The key
            value: The value
            
        Returns:
            bool: True if inserted, False if updated
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if key already exists
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value) #update
                return False
        
        # Key not found, insert new
        bucket.append((key,value))
        self.count += 1
        if len(bucket) > 1:
            self.collisions += 1
        if self._load_factor() > 0.7:
            self._resize()

        return True

    def search(self, key):
        """
        TODO #4: Implement search operation
        
        Find a value by key.
        
        Algorithm:
        1. Get bucket index: index = self._hash(key)
        2. Get the bucket: bucket = self.buckets[index]
        3. Search through bucket:
           - for k, v in bucket:
               - if k == key:
                   - return v
        4. return None (not found)
        
        Args:
            key: The key to search for
            
        Returns:
            The value if found, None otherwise
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v
        return None  # Not found
    
    def delete(self, key):
        """
        TODO #5: Implement delete operation
        
        Remove a key-value pair.
        
        Algorithm:
        1. Get bucket index: index = self._hash(key)
        2. Get the bucket: bucket = self.buckets[index]
        3. Search and remove:
           - for i, (k, v) in enumerate(bucket):
               - if k == key:
                   - del bucket[i]
                   - self.count -= 1
                   - return True
        4. return False (not found)
        
        Args:
            key: The key to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k   , v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False  # Not found
    # ========================================
    # HELPER METHODS (Already implemented!)
    # ========================================
    
    def __contains__(self, key):
        """Enable 'in' operator: if key in hash_table"""
        return self.search(key) is not None
    
    def __setitem__(self, key, value):
        """Enable: hash_table[key] = value"""
        self.insert(key, value)
    
    def __getitem__(self, key):
        """Enable: value = hash_table[key]"""
        value = self.search(key)
        if value is None:
            raise KeyError(f"Key '{key}' not found")
        return value
    
    def keys(self):
        """Get all keys."""
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_keys.append(key)
        return all_keys
    
    def values(self):
        """Get all values."""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_values.append(value)
        return all_values
    
    def items(self):
        """Get all (key, value) pairs."""
        all_items = []
        for bucket in self.buckets:
            for item in bucket:
                all_items.append(item)
        return all_items
    
    def stats(self):
        """Print hash table statistics."""
        print("\n" + "="*60)
        print("📊 HASH TABLE STATISTICS")
        print("="*60)
        print(f"Items: {self.count}")
        print(f"Buckets: {self.size}")
        print(f"Load Factor: {self._load_factor():.2f}")
        print(f"Collisions: {self.collisions}")
        print(f"\nBucket Distribution:")
        
        for i, bucket in enumerate(self.buckets):
            if bucket:
                keys = [k for k, v in bucket]
                print(f"  Bucket {i:2d}: {len(bucket)} items - {keys}")
        
        non_empty = sum(1 for b in self.buckets if b)
        print(f"\nNon-empty buckets: {non_empty}/{self.size} ({non_empty/self.size*100:.1f}%)")
        print("="*60 + "\n")
    
    def __str__(self):
        """String representation."""
        items = self.items()
        if not items:
            return "{}"
        items_str = ", ".join(f"'{k}': {v}" for k, v in items)
        return "{" + items_str + "}"
    
    def __repr__(self):
        """Developer representation."""
        return f"HashTable(size={self.size}, count={self.count}, load={self._load_factor():.2f})"


# ========================================
# TEST SUITE (Run this to check your work!)
# ========================================

def test_hash_table():
    """Test your hash table implementation."""
    print("\n" + "="*60)
    print("🧪 TESTING YOUR HASH TABLE")
    print("="*60 + "\n")
    
    # Test 1: Hash function
    print("TEST 1: Hash Function")
    ht = HashTable(initial_size=10)
    try:
        index = ht._hash("cat")
        if index is not None and 0 <= index < 10:
            print(f"  ✅ hash('cat') = {index} (valid index)")
        else:
            print(f"  ❌ hash('cat') returned invalid index: {index}")
    except:
        print("  ❌ _hash() not implemented yet")
    print()
    
    # Test 2: Insert
    print("TEST 2: Insert Operation")
    ht = HashTable(initial_size=4)
    try:
        result = ht.insert("apple", 10)
        if ht.count == 1:
            print(f"  ✅ Insert works! Count = {ht.count}")
        else:
            print(f"  ❌ Insert didn't update count correctly: {ht.count}")
    except:
        print("  ❌ insert() not implemented yet")
    print()
    
    # Test 3: Search
    print("TEST 3: Search Operation")
    try:
        value = ht.search("apple")
        if value == 10:
            print(f"  ✅ Search works! Found 'apple' = {value}")
        else:
            print(f"  ❌ Search returned wrong value: {value}")
        
        value = ht.search("banana")
        if value is None:
            print(f"  ✅ Search correctly returns None for missing key")
        else:
            print(f"  ❌ Search should return None for missing key")
    except:
        print("  ❌ search() not implemented yet")
    print()
    
    # Test 4: Delete
    print("TEST 4: Delete Operation")
    try:
        result = ht.delete("apple")
        if result and ht.count == 0:
            print(f"  ✅ Delete works! Count = {ht.count}")
        else:
            print(f"  ❌ Delete didn't work correctly")
    except:
        print("  ❌ delete() not implemented yet")
    print()
    
    # Test 5: Resize
    print("TEST 5: Auto-Resize (watch for resize message)")
    ht = HashTable(initial_size=4)
    try:
        for i in range(5):  # This should trigger resize
            ht.insert(f"key{i}", i * 10)
        
        if ht.size > 4:
            print(f"  ✅ Resize works! Size increased to {ht.size}")
        else:
            print(f"  ❌ Resize didn't happen")
    except:
        print("  ❌ Resize test failed")
    print()
    
    # Test 6: Full integration
    print("TEST 6: Full Integration Test")
    ht = HashTable(initial_size=4)
    try:
        # Insert
        ht.insert("apple", 10)
        ht.insert("banana", 20)
        ht.insert("cherry", 30)
        
        # Search
        assert ht.search("apple") == 10
        assert ht.search("banana") == 20
        assert ht.search("cherry") == 30
        
        # Update
        ht.insert("apple", 15)
        assert ht.search("apple") == 15
        
        # Delete
        ht.delete("banana")
        assert ht.search("banana") is None
        assert ht.count == 2
        
        print("  ✅ ALL INTEGRATION TESTS PASSED! 🎉")
        print(f"  Final state: {repr(ht)}")
    except Exception as e:
        print(f"  ❌ Integration test failed: {e}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    test_hash_table()
