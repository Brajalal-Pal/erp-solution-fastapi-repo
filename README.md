
## Instructions:

```bash
$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"



# Following commaneds executed
$ git config  --global init.defaultBranch main
$ git branch  -m main
$ pip install -r requirements-dev.txt

# -------------------------------------------------------------------------------------------
$ uvicorn app.main:app --reload

or

# Add following in the app/main.py file
if __name__ == "__main__":
    import uvicorn as uv
    uv.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

# Run following in the terminal
$ python app.main

# -------------------------------------------------------------------------------------------
# Testing: create pytest.ini in the root folder with following lines.
[pytest]
pythonpath = .

# Then, run:
$ pytest

$ ruff check . --fix

# Push the changes to github repo
$ git config --global user.email "brajalal@rediffmail.com"
$ git config --global user.name "Brajalal Pal"
$ git remote add origin https://github.com/Brajalal-Pal/erp-solution-fastapi-repo.git

# -------------------------------------------------------------------------------------------

```


