| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `nmuidi files` | 5.675 ± 0.149 | 5.570 | 5.780 | 1.00 |
| `busybox.exe rm -rf files` | 107.634 ± 0.460 | 107.308 | 107.959 | 18.97 ± 0.50 |
| `rmdir /s /q files` | 9.847 ± 0.065 | 9.801 | 9.893 | 1.74 ± 0.05 |
| `del /f /s /q files > nul && rmdir /s /q files > nul` | 11.121 ± 0.047 | 11.087 | 11.154 | 1.96 ± 0.05 |
| `wsl -d Ubuntu_WSL1 -e rm -rf files` | 12.308 ± 0.118 | 12.224 | 12.392 | 2.17 ± 0.06 |
| `robocopy empty files /MIR > nul` | 15.714 ± 0.545 | 15.329 | 16.100 | 2.77 ± 0.12 |
