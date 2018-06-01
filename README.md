"# Change-making-problem" 
----
The change-making problem, also known as minimum coin change problem, addresses the question of finding the minimum number of coins (of certain denominations) that add up to a given amount of money. It is a knapsack type problem, and has applications wider than just currency.  
----
It is also the most common variation of the coin change problem, a general case of partition in which, given the available denominations of an infinite set of coins, the objective is to find out the number of possible ways of making a change for a specific amount of money, without considering the order of the coins.  
----
It is weakly NP-hard, but may be solved optimally in pseudo-polynomial time by dynamic programming. 

----
In my way, I'll use Greedy Algorithm to solve this problem. It gave ```O(m^2)``` with m is size of type Coin
