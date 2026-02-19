class Seq(list):
    def less(self, i, j):
        return self[i] < self[j]

    def swap_items(self, i, j):
        self[i], self[j] = self[j], self[i]

    def partition(self, l, r, p):
        i, j = l - 1, r
        pivot = self[p]
        while True:
            while True:
                i += 1
                if i == j:
                    return i
                if pivot < self[i]:
                    break

            while True:
                j -= 1
                if j == i:
                    return i
                if self[j] < pivot:
                    break

            self[i], self[j] = self[j], self[i]

    def blockSwap(self, m, r, p):
        if m == r:
            return
        self[m:p + 1] = self[r:p + 1] + self[m:r]

    def downwave(self, start, sortedStart, end):
        if (sortedStart - start) == 0:
            return

        p = sortedStart + (end - sortedStart) // 2
        m = self.partition(start, sortedStart, p)

        if m == sortedStart:
            if p == sortedStart:
                self.upwave(start, sortedStart - 1)
                return
            self.downwave(start, sortedStart, p - 1)
            return

        self.blockSwap(m, sortedStart, p)

        if m == start:
            if p == sortedStart:
                self.upwave(m + 1, end)
                return
            p += 1
            self.downwave(m + p - sortedStart, p, end)
            return

        if p == sortedStart:
            self.upwave(start, m - 1)
            self.upwave(m + 1, end)
            return

        self.downwave(start, m, m + p - sortedStart - 1)
        self.downwave(m + p - sortedStart + 1, p + 1, end)

    def upwave(self, start, end):
        if start == end:
            return

        sortedStart = end
        sortedLength = 1
        leftBound = end - 1
        length = end - start + 1

        while leftBound > start:
            self.downwave(leftBound, sortedStart, end)
            sortedStart = leftBound
            sortedLength = end - sortedStart + 1
            if length < (sortedLength << 2):
                break
            leftBound = end - (sortedLength << 1) + 1

        self.downwave(start, sortedStart, end)

    def WaveSort(self):
        if len(self) < 2:
            return
        self.upwave(0, len(self) - 1)

arr = [12, 11, 13, 5, 6, 7]
arrW = Seq(arr)
arrW.WaveSort()
print("Sorted array is:", arrW)