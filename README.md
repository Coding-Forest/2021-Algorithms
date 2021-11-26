# <span id="top">2021-Algorithms</span>


## Data Structures & Algorithms

### Data Structures

[1. Arrays](#arrays)  
[2. Graphs](#graphs)  
[3. Hash Tables](#hashtables)  
[4. Heap](#heap)  
[5. Linked Lists](#linkedlists)  
[6. Queues](#queues)  
[7. Stacks](#stacks)  
[8. Trees](#trees)  
[9. Tries](#tries)  

<br>


### Algorithms  

[1. Binary Search](#binarysearch)  
[2. DFS/BFS](#dfs/bfs)  
[3. Dynamic Programming](#dynamicprogramming)  
[4. Exhaustive Search](#exhaustivesearch)  
[5. Greedy](#greedy)  
[6. Sorting](#sorting)  

<br>


## Data Structures  

### <span id="arrays">Arrays</span>

<br>

[[Top👆]](#top)

<br>

### <span id="graphs">Graphs</span>

<br>

[[Top👆]](#top)

<br>

### <span id="hashtables">Hash Tables</span>

<br>

[[Top👆]](#top)

<br>

### <span id="heap">Heap</span>

**Binary heaps**  
The major difference between [linked list](#linkedlist) and binary heap is that nodes in binary heaps have 2 child nodes whereas linked list is a list of nodes *serially connected to one after another; every node is connected to exactly one node.*

**Min heap**
  - Every parent node has a value that is smaller that that of its child nodes. Starting from top to bottom, the values increase. In other words, the root holds the minimum value. 
    - `parent` < `child`
  - Key operations
    - `insert`
    - `delete`

**Max heap**
  - Advantage: `MaxHeap` is fast.
    - `insert` in O(log n)
    - `get max` in O(1)
    - `remove max` in O(log n)
  - `parent` > `child`
  - Easy to implement using an array.
    - `MaxHeap` operations
      - `push (insert)`: add value to end of the array. float it up to the proper position. 
      - `peek (get max)`: return the value at heap[1].
      - `pop (remove max)`: move max to end of array. delete it. buble down the item at index 1 to the proper position. Return `max`
      
  **Learning materials**
  - Joe James (2015) Python: MaxHeap heapsort https://www.youtube.com/watch?v=GnKHVXv_rlQ&ab_channel=JoeJames
  - Spanning Tree (20200 What Is a Binary Heap? https://www.youtube.com/watch?v=AE5I0xACpZs&ab_channel=SpanningTree

<br>

[[Top👆]](#top)

<br>

### <span id="linkedlists">Linked Lists</span>

<br>

[[Top👆]](#top)

<br>

### <span id="queues">Queues</span>

<br>

[[Top👆]](#top)

<br>

### <span id="stacks">Stacks</span>

<br>

[[Top👆]](#top)

<br>

### <span id="trees">Trees</span>

<br>

[[Top👆]](#top)

<br>

### <span id="tries">Tries</span>

<br>

[[Top👆]](#top)

<br>



## Algorithms  

### <span id="binarysearch">Binary Search</span>

<br>

[[Top👆]](#top)

<br>

### <span id="dfs/bfs">DFS/BFS</span>

<br>

[[Top👆]](#top)

<br>

### <span id="dynamicprogramming">Dynamic Programming</span>

<br>

[[Top👆]](#top)

<br>

### <span id="exhaustivesearch">Exhaustive Search</span>

<br>

[[Top👆]](#top)

<br>

### <span id="greedy">Greedy</span>

<br>

[[Top👆]](#top)

<br>

### <span id="sorting">Sorting</span>

<br>

[[Top👆]](#top)

<br>




Tutorial Series
1. Algorithms in Motion (Beau Carnes)
2. Data Structures, Algorithms, and Machine Learning Optimization (Jon Krohn)


Study of computer programming algorithms

1) Binary Search https://binarysearch.com/
2) Leetcode https://leetcode.com/


Resources 

1)  Dense Sentiment Classifier (Jon Krohn) https://github.com/jonkrohn/DLTFpT/blob/master/notebooks/dense_sentiment_classifier.ipynb
2) Deep Learning with TensorFlow, Keras, and PyTorch (Jon Krohn) https://github.com/jonkrohn/DLTFpT
