"""******************************************************************************
* Purpose: Hashing .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 02-01-2019
*
******************************************************************************"""

class HashTable:
    def __init__(self):
        self.size = 11                      # size of hash table
        self.slots = [None] * self.size     # list ot hold keys.
        self.data = [None] * self.size      # list to hold values of data .

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))  # calculating hash value by taking reminder of  key and 11(size).

      if self.slots[hashvalue] == None:                 # if slot is empty at hash-values position
        self.slots[hashvalue] = key                     # add key to the slots
        self.data[hashvalue] = data                     # add value to the data.
      else:
        if self.slots[hashvalue] == key:                # if hash-value is already present then replace the data in data list.
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))         # if slot is not empty rehash the hash-value.
          while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data          #replace

    def hashfunction(self,key,size):            # function to calculate hash value.
         return key%size

    def rehash(self,oldhash,size):              # function to rehash the value.
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:      # found=None and stop=None
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):         # Accessing an item using an index
        return self.get(key)

    def __setitem__(self, key, data):   # Assigning to an item using an index
        self.put(key, data)



H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
H[20]='duck'
print(H.slots)

print(H.data)

print(H.get(54))