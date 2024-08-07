# ACME-Education
## A web application made with teachers' and students' hard educational life in mind.
This application enables students and teachers to coonect with each other, helps teachers share their material with their students in a more profissional and distraction free environment, provide for a chatting place with the teacher so they can be heard and slim the chances of the teacher missing a student note, cares to those in need for knowledage but are not a part of any educational establishment.
## Screenshots

![App Screenshot](https://lh3.googleusercontent.com/pw/AP1GczNmGsJ6XrFnDGWR-IkemF8EQjHCk00s1z1SIqCJJLb54wkRMpW51rWN_Qs0CLrg07-ZuvBvFXIdw7XzL6RTbeRYva3kHvvCPcITGZ0MSCuXJ3EbiBAz5B4rQdUU9-tP1rYTvdQiSnq7PHQU8fe2Ahcq=w3280-h1986-s-no-gm?authuser=0)
![App Screenshot](https://lh3.googleusercontent.com/pw/AP1GczNvs12boNWQxvkUynm87fnDDFfS2txqSjhWGWh0kYESIdp1xcqJXR-tHirZRTBFQU6Ghmy8oJa4Gen8MrjDYN3wmELBGzNp78jstJBjPmSnYO8MfFo242jnI-WmxTWvTGVyHWA5jlOe0Olwjje-9bEU=w3454-h1150-s-no-gm?authuser=0)
![App Screenshot](https://lh3.googleusercontent.com/pw/AP1GczO6j7jJ6HuT-P0e4E22u_g-hA36XVNkSQjTMyHtPztUdwUi2jKtdpnlwUfIAzRdWXZ0WJb-oq9PU2zFIMEyMt809vRBFuwM_gETtOMMBkEUa9Sd1Z110OaCpDrpam9DnfN1CR3ALTgsvv2IodWWR6s9=w3432-h1868-s-no-gm?authuser=0)
![App Screenshot](https://lh3.googleusercontent.com/pw/AP1GczORq7kaR2Jw5P0grfXAdiQUjyUqSFxxqxS4_8tgEPGpMdtM2mkMiKFH7Y6wQ0jb8hzViat1Uh0VhI5mT6BrqS5xrxR90n_fIpyJ_Y33KdldUxl7Abnv4qGVxIq5rJezf5HQbOOVOQr-brBJFB8VbfEV=w2902-h688-s-no-gm?authuser=0)

## Used By

This project is made for:

- Teachers.
- Students.
- Scholars.


## Contributing

- DRIHMIA Redouane - Database, ORM and API.
- Mohammed Omer - API, API tests and documentation for the API.
- Ubonisrael Amos Akpanudoh - Front end and code reviewing.
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

```
  SECRET_KEY='defined by user'
  JWT_SECRET_KEY='defined by user'
  ACME_EMAIL='to send verification email'
  FRONT_END_ROUTER="127.0.0.1:3000"
  BACK_END_ROUTER="127.0.0.1:5000"
  p='database password'
  u='database user'
  h='ip address of database'
  D='ACME'
```


## Tech Stack

**Front end:** React and Nextjs

**Back end:** Python3 and SQL

**Framework:** Flask


## Installation

Install dependancies

```bash
  sudo apt update
  sudo apt install mysql-server
  sudo apt-get install python3-dev
  sudo apt-get install libmysqlclient-dev
  sudo apt-get install zlib1g-dev
  sudo pip3 install mysqlclient
  sudo pip3 install SQLAlchemy
  sudo apt-get install -y python3-lxml
  sudo pip3 install Flask
  sudo pip3 install flask_cors
  sudo pip3 install flasgger
  sudo pip3 install pytest
  sudo pip3 install yagmail
  sudo pip3 install flask_jwt_extende
  npm install
```

Run the fornt end
- To run the front-end server on development mode
    ```bash
      cd ACME-Education/acme-education-frontend
      npm run dev
    ```
- To run the build
    ```bash
      cd ACME-Education/acme-education-frontend
      npm run build
    ```
- To run the front-end server on production mode:
    ```bash
      cd ACME-Education/acme-education-frontend
      npm run start
    ```

Run the back end
- Starting the database, populate it and run the back end
    ```bash
      cd ACME-Education
      ./pop.bash
    ```
- starting the API
    ```bash
      cd ACME-Education
      python3 -m api.v1.app
    ```
## API Reference

You can find the API documentation by following this <a href="https://night-belly-22c.notion.site/ACME-Education-API-Docs-77ef7af075cd44829cdfcb8d4d45dd79?pvs=4" target="_blank">link</a> or see a less cooler version by navigating to [`/docs`](https://drihmia.tech/docs) in the repo and see the MD file.

## Running Tests

The test are devided according to the HTTP methods. This way we get the advantage of isolating different casses for each endpoint. This also give the advantages of having the ability to test for a specific HTTP method without having to look for a specific case in a rather long file.

To run tests dedicated for the API, move into the folder containting the method you would like to test.

- Run all the test casses for all endpoints
    ```bash
      pytest -v
    ```
- Run all the test casses for a specific endpoint
    ```bash
      pytest -v test_{endpoint name}.py
    ```
- Run aspecific test casse for an endpoint
    ```bash
      pytest -v test_{endpoint name}.py::{test case name from instide the file}
    ```

## Authors

- DRIHMIA Redouane - [Email](drihmia.redouane@gmail.com) / [Github](https://github.com/Drihmia) / [LinkedIn](https://www.linkedin.com/in/rdrihmia/)
- Mohammed Omer - [Github](https://github.com/MegaChie) / [LinkedIn](www.linkedin.com/in/mohamed-omer-63b24b21b)
- Ubonisrael Amos Akpanudoh - [Email](akpanudohubonisrael@gmail.com) / [Github](https://github.com/ubonisrael) / [LinkedIn](https://linkedin.com/in/ubonisrael-akpanudoh-44ba82246/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
