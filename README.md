# Challengica
![Poster](./4.jpg)

This is simiar to http://www.pythonchallenge.com/

## About

This was created to host a competition in our college during fest. Only difference is that `pythonchallenge.com` is for **python** and **Challengica** is for **C/C++**

## Demo

The live version of this app is hosted at [Challengica](https://challengica.pythonanywhere.com/)

---

## Running development server on local machine

Make sure you have Python 3.x installed.

Navigate to `challengica` folder in this repo.

Setup a virtual environment for this project proceeding. I would strongly recommend you to use vitualised environment to run this. You can find about how to setu-up virtual environment [here](https://docs.python.org/3/tutorial/venv.html).

Once you're ready with everything, you need to make sure that you have all the packages required are installed on your PC. You can do that by simply following the below command.

```bash
# in challengica directory
pip install -r requirements.txt
```

> To run the development server on localhost

```bash
# `python` command depends on the version and OS installed on your machine
# It can be python3(for Linux or macOS) or py(for Windows) if multiple versions are installed
# make sure to use which ever is installed and suitable in your case
python manage.py runserver
```

Now you can see the app running at `localhost:8000`

---

If you feel there are any bugs in the app or want to make a feature request or want to share any issue you found, please feel free to open an issue and give description.
