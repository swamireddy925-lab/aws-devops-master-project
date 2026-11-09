import subprocess
import sys

container_name = "aws-devops-container"

result = subprocess.run(
    ["docker", "inspect", "-f", "{{.State.Status}}", container_name],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("ERROR: Unable to inspect Docker container!")
    print(result.stderr.strip())
    sys.exit(1)

status = result.stdout.strip()

if status == "running":
    print("SUCCESS: Docker container is running!")
else:
    print("WARNING: Docker container is not running!")
    print("Current status:", status)
    sys.exit(1)
