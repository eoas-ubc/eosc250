#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\Users\paust\mini37b\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion
$a448 = "~\repos\atsc448"

function prompt
{
    $l = Split-Path -leaf -path (Get-Location)
    $p = Split-Path -parent -path (Get-Location)
    $p = Split-path -leaf $p
    $e = Split-Path -leaf $env:conda_prefix
    write-host -noNewLine "($e):$p/$l"
    return "> "
}
conda activate e213
set-psreadlineoption -editmode emacs
cd $HOME

function fun_newroc { ssh -i $HOME/.ssh/safe_rail "phil@newroc.eos.ubc.ca" }
Set-Alias newroch fun_newroc
