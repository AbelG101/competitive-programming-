class FrequencyTracker(object):
    def __init__(self):
        self.number_occurrences = {}
        self.frequency_count = {}

    def add(self, number):
        occurrence = self.number_occurrences.get(number, 0)
        self.number_occurrences[number] = occurrence + 1
        
        if occurrence in self.frequency_count:
            self.frequency_count[occurrence] -= 1
            if self.frequency_count[occurrence] == 0:
                del self.frequency_count[occurrence]
                
        self.frequency_count[occurrence + 1] = self.frequency_count.get(occurrence + 1, 0) + 1

    def deleteOne(self, number):
        occurrence = self.number_occurrences.get(number, 0)
        if occurrence > 0:
            self.number_occurrences[number] -= 1
            
            if self.frequency_count[occurrence] == 1:
                del self.frequency_count[occurrence]
            else:
                self.frequency_count[occurrence] -= 1
            
            self.frequency_count[occurrence - 1] = self.frequency_count.get(occurrence - 1, 0) + 1

    def hasFrequency(self, frequency):
        return frequency in self.frequency_count and self.frequency_count[frequency] > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)