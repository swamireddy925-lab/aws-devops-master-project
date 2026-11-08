import subprocess

container_name = "aws-devops-container"

result = subprocess.run(
    ["sudo", "docker", "inspect", "-f", "{{.State.Status}}", container_name],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    status = result.stdout.strip()

    if status == "running":
        print("SUCCESS: Docker container is running!")
    else:
        print("WARNING: Docker container is stopped!")
        print("Current status:", status)

else:
    print("ERROR: Unable to find Docker container!")
    print(result.stderr)
