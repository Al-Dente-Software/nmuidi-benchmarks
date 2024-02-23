| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `nmuidi files` | 16.467 ± 0.441 | 16.042 | 17.541 | 1.00 |
| `busybox.exe rm -rf files` | 35.391 ± 0.261 | 35.125 | 35.950 | 2.15 ± 0.06 |
| `rmdir /s /q files` | 18.436 ± 0.234 | 18.211 | 18.999 | 1.12 ± 0.03 |
| `del /f /s /q files > nul && rmdir /s /q files > nul` | 29.364 ± 0.572 | 28.640 | 30.388 | 1.78 ± 0.06 |
| `wsl -d Ubuntu_WSL1 -e rm -rf files` | 31.698 ± 0.922 | 31.026 | 33.978 | 1.92 ± 0.08 |
| `robocopy empty files /MIR > nul` | 37.749 ± 0.207 | 37.402 | 38.187 | 2.29 ± 0.06 |
