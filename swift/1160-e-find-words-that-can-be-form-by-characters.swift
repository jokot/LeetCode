// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution {
    func countCharacters(_ words: [String], _ chars: String) -> Int {

        var count = Array(repeating: 0, count: 26)

        func getIndexFromChar(char: Character) -> Int {
            let charAscii = Int(char.asciiValue ?? 0)
            let aAscii = Int(Character("a").asciiValue ?? 0)
            return charAscii-aAscii
        }

        for char in chars {
            count[getIndexFromChar(char: char)] += 1
        }

        func isCanForm(word: String, count: [Int]) -> Bool {
            var runningCount = count
            for c in word {
                if runningCount[getIndexFromChar(char: c)] == 0 {
                    return false
                }
                runningCount[getIndexFromChar(char: c)] -= 1
            }

            return true
        }

        var result = 0

        for word in words {
            if isCanForm(word: word, count: count) {
                result += word.count
            }
        }
        return result
    }
}