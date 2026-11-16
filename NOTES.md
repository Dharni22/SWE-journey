# How to start a session

cd ~/learn/swe-journey
conda activate ./.venv

Then work. Type `conda deactivate` when done.

## Machine notes (work laptop, Ubuntu, no sudo)
- `python3 -m venv` does NOT work here: the python3-venv package is missing and needs sudo.
- `pip install` outside an environment fails with "externally-managed-environment" (PEP 668).
- So the environment is a conda env created inside the project:
    conda create -p ./.venv python=3.12 -y
- Activate with `conda activate ./.venv`, NOT `source .venv/bin/activate`.
- Inside the env, plain `pip install <package>` works normally.
- Conda `(base)` is for work. This project has its own env.

## GitHub
- Personal account: Dharni22
- Clone/push use the SSH alias `github-personal`, not `github.com`.
- Personal key: ~/.ssh/id_ed25519_personal  (work key id_ed25519 is untouched)
- Git identity is personal only inside ~/learn/ (set by includeIf in ~/.gitconfig)

## Save my work
git status
git add <files>
git commit -m "what I did"
git push
