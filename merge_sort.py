from SortingAlgorithm import SortingAlgorithm

class MergeSort(SortingAlgorithm):

    def merge(self, left, right):
        i = 0
        j = 0
        output = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i = i + 1
            else:
                output.append(right[j])
                j = j + 1

        
        # at this point one of the lists is empty. We can now simply append the 
        # remaining list to the end of the output. We don't need to check which 
        # one is empty. We can simply add the emtpy list. 
        output.extend(left[i:])
        output.extend(right[j:])        
        return output

        
    def merge_sort(self, x):
        if len(x) <= 1:
            # abort recursion if list has only one element left.
            return x
        
        # Divide list in two parts.
        left = x[:(len(x)//2)]
        right =x [len(x)//2:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def sort(self):
        self.data = self.merge_sort(self.data)


if __name__ == "__main__":
    arr = [4,2,3]
    ms = MergeSort(arr)
    ms.sort()
    print(ms.data)