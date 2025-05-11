// https://leetcode.com/problems/circular-sentence/
class Solution {
    func isCircularSentence(_ sentence: String) -> Bool {
        let words = sentence.split(separator: " ").map(String.init)
        let size = words.count

        let first = words[0]
        let second = words[size-1]

        if first.char(at: 0) != second.char(at: second.count-1) {
            return false
        }

        if size == 1 {
            return true
        }

        for i in 0..<size-1 {
            let current = words[i]
            let next = words[i+1]

            if current.char(at: current.count-1) != next.char(at: 0) {
                return false
            }
        }

        return true
    }
}

extension String {
    func char(at index: Int) -> Character {
        precondition(index >= 0 && index < self.count, "Index out of range")
        let charIndex = self.index(self.startIndex, offsetBy: index)
        return self[charIndex]
    }
}