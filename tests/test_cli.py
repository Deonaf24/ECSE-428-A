import subprocess
import sys

def test_cli_push_pop_outputs_canonical():
    p = subprocess.run(
        [sys.executable, "-m", "src.cli"],
        input="push 5\npop\n",
        text=True,
        capture_output=True,
    )
    assert p.returncode == 0
    assert p.stdout.strip().splitlines() == ["5 + j0"]
