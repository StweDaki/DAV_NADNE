import subprocess

email = "stewartdaki@gmail.com"
passphrase = "a"

subprocess.run(["ssh-keygen", "-t", "ed25519", "-C", email, "-f", "N:\PostProd\Prj\GIT\DAV_NADNE/.ssh/id_ed25519", "-N", passphrase])
