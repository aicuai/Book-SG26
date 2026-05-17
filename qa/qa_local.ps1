<#
.SYNOPSIS
  Book-SG26 Local QA Runner (Win11 / PowerShell)

.DESCRIPTION
  Performs local QA against this repository on a Windows machine where
  GPU-dependent verification (Stability Matrix, ComfyUI Desktop, etc.) is
  possible — i.e. things GitHub-hosted runners and Mac cannot exercise.

  By default:
    1. git pull --ff-only
    2. python qa/check_json.py
    3. python qa/check_shortlinks.py

  On failure, pass -ReportIssue to file a GitHub Issue via the gh CLI
  (label: qa-failure-local). The development repository monitors that
  label for follow-up.

.PARAMETER SkipPull
  Skip the initial git pull step.

.PARAMETER ReportIssue
  On failure, create a GitHub Issue using the gh CLI.

.NOTES
  Requires: git, python (3.10+), pyyaml (`pip install pyyaml`), and
  (for -ReportIssue) the gh CLI authenticated against this repository.
#>

[CmdletBinding()]
param(
    [switch]$SkipPull,
    [switch]$ReportIssue
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot

Push-Location $repoRoot
try {
    if (-not $SkipPull) {
        Write-Host "==> git pull" -ForegroundColor Cyan
        git pull --ff-only
    }

    $failed = @()

    Write-Host "`n==> JSON validation" -ForegroundColor Cyan
    python qa/check_json.py
    if ($LASTEXITCODE -ne 0) { $failed += "check_json" }

    Write-Host "`n==> Shortlink check" -ForegroundColor Cyan
    python qa/check_shortlinks.py
    if ($LASTEXITCODE -ne 0) { $failed += "check_shortlinks" }

    if ($failed.Count -eq 0) {
        Write-Host "`nAll local QA checks passed." -ForegroundColor Green
        exit 0
    }

    Write-Host "`nLocal QA failed: $($failed -join ', ')" -ForegroundColor Yellow

    if ($ReportIssue) {
        $title = "[QA-local] $($failed -join ', ') failed on Win11"
        $os = (Get-CimInstance Win32_OperatingSystem).Caption
        $hostInfo = "$env:COMPUTERNAME / $os"
        $timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'

        $body = @"
ローカル QA (Windows) で失敗を検出しました。

- 失敗したチェック: $($failed -join ', ')
- 実行ホスト: $hostInfo
- 日時: $timestamp

> このIssueはローカル QA スクリプト (qa/qa_local.ps1) により手動報告されました。
> 詳細解析と対応は開発リポジトリ側で実施されます。
"@

        Write-Host "==> Reporting issue via gh" -ForegroundColor Cyan
        gh issue create --label "qa-failure-local" --title $title --body $body
    } else {
        Write-Host "Tip: re-run with -ReportIssue to file a GitHub Issue automatically." -ForegroundColor DarkGray
    }

    exit 1
}
finally {
    Pop-Location
}
