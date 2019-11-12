## introduction
* *interface*: a formal contract between a class and the outside world.if your class claims to implement an interface,then all methods defined by interface must appear in your class(or somewhere in your superclass) before the class will successfully compile.This is a way of enforcing promised behavior.All methods that you declare or define are automatically public and abstract(even if you omit the public word)
* *Abstract class*: Methods and classes can be declared as abstract using the abstract keyword.Abstract class cannot be instantiated,but they can be subclassed using extend keyword. Unlike interfaces, abstract classes can provide implementation inheritance for features other than public methods, including instance variables.Classes that implement interfaces will inherit all of the methods and variables from that interface. If an implementing class fails to implement any abstract methods inherited from an interface, then that class must be declared abstrac
* Abstract Data Type(ADT) is defined only by its operation,not by its implementation
  implementation is related the class internal 
  operation is related to the using of the call

## Abstract data type
* Stacks: Structures that support last-in first-out retrieval of elements
  push(int x ):put x on the top of the stack
  int pop():take the emement on the top of the stack
* Lists: an ordered set of elements
  add(int i):adds an elements
  int get(int i):get element at index i
* Sets:an unordered set of unique elements(no repeats)
  add(int i):adds an element
  contains(int i):returns a boolean for whether or not the set contains the value
* Maps :set of key/value pairs
  put(K key,V value):puts a key value pair into the map
  V get(K key):gets the value corresponding to the key


binary trees are composeed of:
* nodes
* edges that connect those nodes
    there is only one path between any two nodes
    each node has either 0,1 or 2 children
Binary Search Trees:
  in addition to all of the above requirements, also hold the property that for every node X in the tree
  * Every key in the left subtree is less than X's key
  * Every key in the right subtree is greater the X's key
  

   