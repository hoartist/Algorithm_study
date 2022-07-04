class P200 {
    val dx =arrayOf(1,-1,0,0)
    val dy = arrayOf(0,0,1,-1)
    lateinit var visited:Array<BooleanArray>
    var answer = 0

    fun numIslands(grid: Array<CharArray>): Int {
        answer = 0
        visited = Array(grid.size){BooleanArray(grid[0].size)}
        for((rowIndex,row) in visited.withIndex()){
            for((colIndex,position) in row.withIndex()){
                if(!position && grid[rowIndex][colIndex] == '1'){
                    println("[$rowIndex, $colIndex]")
                    searchArea(rowIndex,colIndex,grid )
                    answer += 1
                }
            }
        }
        return answer
    }
    fun searchArea(x:Int, y:Int, grid:Array<CharArray>){
        if(x < 0 || x >= visited.size || y < 0 || y >= visited[0].size){
            println("returned at $x $y, ${visited[0].size} ${visited.size}")
            return
        }
        if(grid[x][y] == '1'&& visited[x][y] == false ){
            visited[x][y] = true
            for(i in 0 until 4){
                searchArea(x + dx[i], y + dy[i],grid)
            }
        }

    }
}