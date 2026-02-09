import subprocess
import sys

#T-CLI1
def test_cli_push_pop_outputs_canonical():
    p = subprocess.run(
        [sys.executable, "-m", "src.cli"],
        input="push 5\npop\n",
        text=True,
        capture_output=True,
    )
    assert p.returncode == 0
    assert p.stdout.strip().splitlines() == ["5 + j0"]

#T-CLI-ERR1
def test_cli_underflow_prints_error():
    p = subprocess.run(
        [sys.executable, "-m", "src.cli"],
        input="pop\n",
        text=True,
        capture_output=True,
    )
    assert p.returncode == 0
    assert p.stdout.strip().splitlines() == ["Error: stack underflow"]
