import java.io.File

fun main() {
    val logcatProcess = Runtime.getRuntime().exec("adb -s 988a1b3830544f305730 logcat -b radio")
    val logcatReader = logcatProcess.inputStream.bufferedReader()
    val outputFile = File("RIL_log_On_Off.txt")
    val outputWriter = outputFile.bufferedWriter()

    while (true) {
        val line = logcatReader.readLine() ?: break
        outputWriter.write(line)
        outputWriter.newLine()
    }

    logcatReader.close()
    outputWriter.close()
}