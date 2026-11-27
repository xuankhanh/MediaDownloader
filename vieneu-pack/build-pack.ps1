<#
Builds the VieNeu voice pack that Media Downloader downloads for its Vietnamese voices (a person's own voice, and VieNeu's own), from VieNeu-TTS v3 Turbo
(Apache-2.0, https://github.com/pnnbao97/VieNeu-TTS). Three zips and a manifest, to be put on a release of this repository, which the workflow "VieNeu voice pack"
(.github/workflows/vieneu-pack.yml) does: run it there, not by hand. A published pack is never changed: a new pack is a new number, which the app takes by itself when it is the newest
published one of its contract (PackContract in MediaKit's VieNeu.cs, in the app's source repository).

    vieneu-runtime-<ver>.zip   Python 3.12 (python-build-standalone), the libraries the engine needs, vieneu_runner.py and the licenses   (~65 MB)
    vieneu-int8-<ver>.zip      the model for CPUs with VNNI, with the codec and the speaker encoder                                       (~235 MB)
    vieneu-fp32-<ver>.zip      the same at full precision, for the other CPUs                                                           (~340 MB)
    manifest.json              the pack's number and contract, the VieNeu inside, and each zip's name, size and SHA-256
    (the runtime also has presets.json: the voices the model has, for the app's list)

Everything is made in -Work (a scratch folder with room for 3 GB, not on a nearly full drive): uv, the Python and the downloads' caches stay there too.
Needs Python (any version) on the PATH or in -Python, to run uv from. Written for Windows PowerShell 5.1 (it is what it was tried with).

    .\build-pack.ps1 -Work D:\Temp\vieneu-pack -Out D:\Temp\vieneu-pack\dist -PackVersion 1 -Contract 1
#>
param(
    [Parameter(Mandatory)] [string] $Work,
    [Parameter(Mandatory)] [string] $Out,
    # The pack's number: each new one is the next (the workflow counts); the app takes the newest published of its contract
    [int] $PackVersion = 1,
    # The contract with the app: how it calls vieneu_runner.py and what the folders hold (PackContract in the app); changed only with the app
    [int] $Contract = 1,
    [string] $Python = "python"
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path

# A program that fails doesn't stop a PowerShell script by itself: each one is looked at, or the pack would be made of what was left
function Check-Exit($what) {
    if ($LASTEXITCODE -ne 0) { throw "$what failed (exit code $LASTEXITCODE)" }
}
# robocopy says 0 to 7 for a copy that went well (1 is "files were copied")
function Copy-Tree($from, $to, [string[]] $skip) {
    robocopy $from $to /E /NFL /NDL /NJH /NJS /NP /XD @skip | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "copying $from failed (robocopy exit code $LASTEXITCODE)" }
    $global:LASTEXITCODE = 0
}

New-Item -ItemType Directory -Force $Work, $Out | Out-Null
foreach ($d in 'tmp', 'pipcache', 'uvcache', 'py', 'hf', 'stage') { New-Item -ItemType Directory -Force "$Work\$d" | Out-Null }
$env:TEMP = "$Work\tmp"; $env:TMP = "$Work\tmp"; $env:PIP_CACHE_DIR = "$Work\pipcache"; $env:UV_CACHE_DIR = "$Work\uvcache"
$env:UV_PYTHON_INSTALL_DIR = "$Work\py"; $env:HF_HOME = "$Work\hf"; $env:PYTHONUTF8 = "1"
# Only the Python build uv fetches into $Work\py: a Python 3.12 that is on the PATH (the one setup-python leaves on the GitHub runner) would be taken instead, and nothing
# would be left in $Work\py to put in the pack (a pack is made of the one build, whatever is installed on the machine that makes it)
$env:UV_PYTHON_PREFERENCE = "only-managed"

# --- uv, then Python 3.12 and the libraries, at the versions the engine was tried with
if (-not (Test-Path "$Work\bootstrap\Scripts\uv.exe")) {
    & $Python -m venv "$Work\bootstrap"; Check-Exit "python -m venv"
    & "$Work\bootstrap\Scripts\python.exe" -m pip install --quiet uv; Check-Exit "pip install uv"
}
$uv = "$Work\bootstrap\Scripts\uv.exe"
Remove-Item "$Work\env" -Recurse -Force -ErrorAction SilentlyContinue
& $uv venv --python 3.12 "$Work\env"; Check-Exit "uv venv"
$envPython = "$Work\env\Scripts\python.exe"
& $uv pip install --python $envPython --no-deps "vieneu==3.8.5"; Check-Exit "uv pip install vieneu"
& $uv pip install --python $envPython "sea-g2p==0.11.0" "onnxruntime==1.32.0" "numpy==2.5.5" "soundfile==0.14.0" "soxr==1.1.0" "kaldi-native-fbank==1.23.3" "tokenizers==0.23.3" "huggingface-hub==2.5.0" "PyYAML==6.0.4"
Check-Exit "uv pip install the libraries"

# --- the runtime zip: Python, the libraries, the runner
$stage = "$Work\stage\runtime"
Remove-Item $stage -Recurse -Force -ErrorAction SilentlyContinue
$standalone = Get-ChildItem "$Work\py" -Directory | Where-Object { $_.Name -like "cpython-3.12*-windows-x86_64-none" } | Select-Object -First 1
if (-not $standalone) { throw "uv didn't leave a Python 3.12 in $Work\py" }
Copy-Tree $standalone.FullName "$stage\python" @("__pycache__", "test", "tests", "idlelib", "tkinter", "turtledemo", "Doc")
Copy-Tree "$Work\env\Lib\site-packages" "$stage\site-packages" @("__pycache__", "tests")
# What the reading never uses (tried 2026-11: it still reads, stops and copies a voice without them): the windows library of Python (tcl/tk), pip and what installs
# packages, the C headers, the docs and tests, and hf_xet (a faster download, but the model is read from disk here). About 30 MB of 235.
$python = "$stage\python"
foreach ($cut in "tcl", "include", "libs", "Scripts", "Lib\ensurepip", "Lib\venv", "Lib\pydoc_data", "Lib\site-packages", "DLLs\_tkinter.pyd", "DLLs\tcl86t.dll", "DLLs\tk86t.dll", "pythonw.exe") {
    Remove-Item "$python\$cut" -Recurse -Force -ErrorAction SilentlyContinue
}
Get-ChildItem "$python\DLLs" -Filter "_test*.pyd" | Remove-Item -Force
Get-ChildItem "$python\Lib" -Directory -Filter "test*" | Remove-Item -Recurse -Force
Get-ChildItem "$stage\site-packages" -Directory | Where-Object { $_.Name -like "hf_xet*" } | Remove-Item -Recurse -Force
if (-not (Test-Path "$python\python.exe") -or -not (Test-Path "$stage\site-packages\vieneu") -or -not (Test-Path "$stage\site-packages\onnxruntime")) {
    throw "the runtime is missing python.exe, vieneu or onnxruntime"
}
Copy-Item "$here\vieneu_runner.py" "$stage\vieneu_runner.py"
# The voices the model has, as the app lists them
& $envPython -I -X utf8 "$here\make_presets.py" "$stage\site-packages\vieneu\assets\voices_v3_turbo.json" "$stage\presets.json"; Check-Exit "make_presets.py"
# What Apache-2.0 asks to go with what is passed on: the license text, and who made what
New-Item -ItemType Directory -Force "$stage\licenses" | Out-Null
$dist = Get-ChildItem "$Work\env\Lib\site-packages" -Directory -Filter "vieneu-*.dist-info" | Select-Object -First 1
$license = Get-ChildItem $dist.FullName -Recurse -File | Where-Object { $_.Name -like "LICENSE*" } | Select-Object -First 1
if ($license) { Copy-Item $license.FullName "$stage\licenses\Apache-2.0.txt" } else { throw "the license text of vieneu was not found" }
Copy-Item "$here\THIRD-PARTY.txt" "$stage\licenses\THIRD-PARTY.txt"
Set-Content "$stage\version.txt" $PackVersion -Encoding ascii -NoNewline
Add-Type -AssemblyName System.IO.Compression.FileSystem
function New-Zip($folder, $zip) {
    Remove-Item $zip -ErrorAction SilentlyContinue
    [IO.Compression.ZipFile]::CreateFromDirectory($folder, $zip, [IO.Compression.CompressionLevel]::Optimal, $false)
}
$runtimeZip = "$Out\vieneu-runtime-$PackVersion.zip"
New-Zip $stage $runtimeZip

# --- the models: a Hugging Face cache folder (hub\models--org--name\refs\main and snapshots\<revision>\...), which the runner reads offline
$layout = "$here\make_models_layout.py"
foreach ($precision in 'int8', 'fp32') {
    $folder = "$Work\stage\models-$precision"
    Remove-Item $folder -Recurse -Force -ErrorAction SilentlyContinue
    & $envPython $layout $folder $precision; Check-Exit "make_models_layout.py $precision"
    New-Zip $folder "$Out\vieneu-$precision-$PackVersion.zip"
}

# --- the manifest
function Entry($name, $path) {
    [ordered]@{ file = $name; size = (Get-Item $path).Length; sha256 = (Get-FileHash $path -Algorithm SHA256).Hash.ToLowerInvariant() }
}
# Which VieNeu is inside, for whoever reads the manifest (the app does not use it: it asks for the pack's number only)
$vieneuVersion = $dist.Name -replace '^vieneu-(.+)\.dist-info$', '$1'
$manifest = [ordered]@{
    version = $PackVersion
    contract = $Contract
    vieneu  = $vieneuVersion
    runtime = Entry "vieneu-runtime-$PackVersion.zip" $runtimeZip
    int8    = Entry "vieneu-int8-$PackVersion.zip" "$Out\vieneu-int8-$PackVersion.zip"
    fp32    = Entry "vieneu-fp32-$PackVersion.zip" "$Out\vieneu-fp32-$PackVersion.zip"
}
# Without a byte order mark (Set-Content -Encoding utf8 of Windows PowerShell writes one): the app reads it as it comes over the network
[IO.File]::WriteAllText("$Out\manifest.json", ($manifest | ConvertTo-Json -Depth 4), (New-Object Text.UTF8Encoding($false)))
Get-ChildItem $Out | Select-Object Name, @{ n = 'MB'; e = { [math]::Round($_.Length / 1MB, 1) } } | Format-Table -AutoSize
$global:LASTEXITCODE = 0
