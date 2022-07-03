class Solution {
    fun romanToInt(s: String): Int {
        val romanNumbersMapped = mapOf<Char, Int>(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000
        )

        val converted: MutableList<Int> = s.map { it -> romanNumbersMapped[it]!! }.toMutableList()
        var lastNum = converted[0]
        // 전처리
        for( (index,num) in converted.withIndex()){
            if(num > lastNum){
                converted[index - 1] *= -1
            } else {
                lastNum = num
            }
        }
        return converted.sum()
    }
}

fun main() {
    println(Solution().romanToInt("MCMXCIV"))
}