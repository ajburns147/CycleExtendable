# Software Development Plan

## Phase 0/1: Requirements Specification and System Analysis *(20%)*
* Need to Read output from C text file and determine if cycle extendable

1. Convert from graph6 to usable format
   1. Get adjacency matrix
   2. Take lower left diagonal matrix and append rows to string
   3. Pad on right with 0s until len is a multiple of 6
   4. Split into 6 bit pieces
   5. vertices + 63 = first char of graph6
   6. Take chr of the int each piece and add to graph6
2. Determine if cycle extendable
   1. Find all cycles in graph
   2. Add each cycle to a set to prevent duplicates
   3. For each cycle in the set:
      1. if meet any of these conditions, skip
         * len = num vert (Hamiltonian)
      2. Compare with every other cycle in set
         1. if length doesn't differ by 1, skip
         2. if first set is subset of second set, cycle is extendable for that first path
      3. If at the end, there are no cycles that are extendable, have found counter example
### Files
* main.py
  * driver
  * minimal logic
* graph6_conversion
  * Able to convert graph6
* extendability
  * from adjMatrix, determines if cycle extendable
### Features
* export to file if not cycle extendable
* Print % completion, time so far, and estimated time remaining
  * estimated time left is 

* Eventual analysis on what parts take the longest


## Phase 2: Design *(30%)*
   ```
   def printReport(start_time, file_length, curr_file_loc):
       percent_complete = round(curr_file_loc * 100/file_length, 3)
       curr_time = time.time()
       time_so_far = curr_time - start_time
       time_left = time_so_far * (1 - percent_complete/100)
       
       print(
       "Running Report \n" +
       "-------------------------------\n" +
       "Percent Completion = " + percent_complete + "  %/n" +
       "Time so far = " + time_so_far + " sec\n" +
       "Time remaining = " + time+left
       )
   ```

```
def adjToGraph6(adjMatrix):
   elements_from_row = 1
   bin_list = ""
   
   for row in adjMatrix:
      bin_list += "".join(list(map(str, row[0:elements_from_row])))
      elements_from_row += 1
      
   bin_list += "0" * (len(bin_list) % 6)
   
   chunks = [bin_list[i:i+6] for i in range(0, len(bin_list), 6)]
   
   graph6 = chr(len(adjMatrix)+63)
   
   for i in chunks:
      graph6 += chr(int(i, 2) + 63)
   
   return graph6
```

## Phase 3: Implementation *(15%)
* Optimization Ideas:
  * store previous graphs in dict. If graph - 1 vertex

## Phase 4: Testing & Debugging *(30%)*


## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance