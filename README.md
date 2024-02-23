# nmuidi Benchmarks

This is supporting documentation for [this video](https://youtu.be/G8BdXgBdaOA).

## Setup

To be able to run these benchmarks you will need:

- [Hyperfine](https://github.com/sharkdp/hyperfine)
- Python 3
- [nmuidi](https://github.com/dillonb/nmuidi)
- A [WSL 1](https://learn.microsoft.com/en-us/windows/wsl/install) Ubuntu image (either called "Ubuntu_WSL1" or update the script accordingly)
- [Busybox](https://www.busybox.net/)
- An empty directory called `empty` for robocopy to use

Once you have all of these installed you should be ready to run the benchmark.

## Benchmark

The way this hyperfine command works is by setting a "prepare" step which runs the `file_generator.py` Python script which generates the sample data into a folder called `files`. This prepare step is run before every command is executed. Commands must be wrapped in quotes and separated by spaces. Each command is run twice as set by the `-- runs 2` option. If you want to increase the run count higher you should be warned that this will wear on your hard drive/SSD, probably not much but worth considering. In my testing the results are pretty consistent. I used a drive that is not my main Windows drive (i.e. not my C drive) which will reduce the amount of background noise that can affect your results.

```
hyperfine.exe -p "python ./file_generator.py" "nmuidi files" "busybox.exe rm -rf files" "rmdir /s /q files" "del /f /s /q files > nul && rmdir /s /q files > nul" "wsl -d Ubuntu_WSL1 -e rm -rf files" -i "robocopy empty files /MIR /mt:128 /log:log.txt" --export-markdown results-5MBfiles.md --runs 2
```

## Results

You can find the latest results [here](Results\results-5MBfiles.md)

## Contributions

If you can think of a better way to delete files on windows, open a pull request and I'd be happy to test it out and include it in the benchmarks.
