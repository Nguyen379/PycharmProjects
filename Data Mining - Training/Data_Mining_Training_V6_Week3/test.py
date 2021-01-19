class SearchArray:
    def __init__(self, input):
        self.list = input

    def search_list(self, start, end, target):
        if start > end:
            return -1

        half = start + (end - start) // 2
        value = self.list[half]

        if value == target:
            return half
        elif value == "":
            left = self.search_list(start, half - 1, target)
            right = self.search_list(half + 1, end, target)
            return max(left, right)
        elif target > value:
            return self.search_list(half + 1, end, target)
        else:
            return self.search_list(start, half - 1, target)

    def search(self, target):
        start = 0
        end = len(self.list) - 1
        return self.search_list(start, end, target)


input = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]

client = SearchArray(input)
print(client.search('ball'))
