class Counter:
    def click(self):
        self.value += 1

    def get_value(self):
        return self.value
    
    def reset(self):
        self.value = 0

    def undo(self):
        if self.value > 0:
            self.value -=1
    
    def set_max_limit(self, max_limit):
        self.max_limit = max_limit

def main():
    counter = Counter()
    counter.set_max_limit()
    counter.reset()
    counter.click()
    count = counter.get_value()
    print(count)
    counter.undo()
    count = counter.get_value()
    print(count)

if __name__ == '__main__':
    main()