"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
"""

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current_idx = 0
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # Get current idx
        # Add after current idx
        # Everything post that is no longer applicable
        self.history = self.history[:self.current_idx+1]
        self.history.append(url)
        self.current_idx +=1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        new_current_idx = max(0, self.current_idx - steps)
        self.current_idx = new_current_idx
        return self.history[self.current_idx]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        new_current_idx = min(len(self.history) - 1, self.current_idx + steps)
        self.current_idx = new_current_idx
        return self.history[self.current_idx]
    
    def get_current_history(self):
        print("history", self.history)
        return self.history
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("www.araz.com")
obj.get_current_history()
obj.visit("Www.google.com")
obj.visit("Www.google2.com")
obj.visit("Www.google3.com")
obj.visit("Www.google4.com")
obj.visit("Www.google5.com")
obj.visit("Www.google6.com")
obj.get_current_history()
param_2 = obj.back(2)
print(param_2)
obj.visit("Www.googley.com")
obj.get_current_history()
param_3 = obj.forward(3)
print(param_3)
param_2 = obj.back(4)
print(param_2)
obj.visit("www.algos.com")
obj.get_current_history()