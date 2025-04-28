// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution {
    func countCharacters(_ words: [String], _ chars: String) -> Int {

        var count: [String : Int] = [:]

        for char in chars {
            count[String(char), default: 0] += 1
        }

        func isCanForm(word: String, count: [String:Int]) -> Bool {
            for c in word {
                if word.filter{ $0 == c }.count > count[String(c), default: 0] {
                    return false
                }
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