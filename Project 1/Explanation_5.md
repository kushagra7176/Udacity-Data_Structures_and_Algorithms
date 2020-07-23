Summary:

I have used two classes namely Block and BlockChain. 
Block class is a template of a LinkedList node and BlockChain class is used to implement a LinkedList. 
Inside the BlockChain class, I have three methods namely append, size and to_list which will append nodes to the end of a LinkedList, return its length and return a list of nodes respectively.

Time and Space Complexity:

Time Complexity:

append takes O(1) since we are adding a new node at the head.

size takes O(n) since we have to traverse the entire LinkedList to find the length of a LinkedList

to_list also takes O(n) as we have to traverse the entire LinkedList to copy each node's value to this list.

Total: O(1 + n + n) => O(n)

Space Complexity:

Space complexity is O(n) as we need a constant space to store each node. Therefore for n nodes, space complexity grows linearly.