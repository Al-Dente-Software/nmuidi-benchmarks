| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `nmuidi files` | 5.798 ± 0.526 | 5.427 | 6.170 | 1.00 |
| `rmdir /s /q files` | 10.670 ± 0.161 | 10.556 | 10.783 | 1.84 ± 0.17 |
| `del /f /s /q files > nul && rmdir /s /q files > nul` | 12.133 ± 0.001 | 12.132 | 12.133 | 2.09 ± 0.19 |
| `robocopy empty files /MIR /mt:128 /log:log.txt` | 12.947 ± 0.075 | 12.894 | 12.999 | 2.23 ± 0.20 |
| `wsl -d Ubuntu_WSL1 -e rm -rf files` | 13.591 ± 0.036 | 13.565 | 13.617 | 2.34 ± 0.21 |
| `busybox.exe rm -rf files` | 109.705 ± 0.073 | 109.653 | 109.756 | 18.92 ± 1.71 |
