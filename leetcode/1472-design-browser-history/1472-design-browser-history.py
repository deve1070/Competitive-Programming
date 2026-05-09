# Browser History
# Array + Current Pointer
# Time Complexity:
# visit   -> O(1) amortized
# back    -> O(1)
# forward -> O(1)

class BrowserHistory:

    def __init__(self, homepage: str):
        # Store history in list
        self.history = [homepage]

        # Current page index
        self.current = 0

        # Last valid page in history
        self.last = 0

    def visit(self, url: str) -> None:
        # Move to next position
        self.current += 1

        # If we're inside existing list, overwrite
        if self.current < len(self.history):
            self.history[self.current] = url
        else:
            self.history.append(url)

        # Clear forward history by updating boundary
        self.last = self.current

    def back(self, steps: int) -> str:
        # Move back as much as possible
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward as much as possible
        self.current = min(self.last, self.current + steps)
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)