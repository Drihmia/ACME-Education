# ACME-Education
## A web application made with teachers' and students' hard educational life in mind.
This application enables students and teachers to coonect with each other, helps teachers share their material with their students in a more profissional and distraction free environment, provide for a chatting place with the teacher so they can be heard and slim the chances of the teacher missing a student note, cares to those in need for knowledage but are not a part of any educational establishment.
## Screenshots

![App Screenshot](https://photos.app.goo.gl/fya9GJAVocrwGqJK7)
![App Screenshot](https://photos.app.goo.gl/T1EbMBuTPf5czJtf7)
![App Screenshot](https://photos.app.goo.gl/z2iWzYADpY6mmbm26)
![App Screenshot](https://photos.app.goo.gl/3uzQYVBLontEZMmx5)

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
  SECRET_KEY='afc418492cb06c4fecc7467f1d12648a'
  JWT_SECRET_KEY='a0aff3b1ed0d8278ba099ef6c32ba28ad054d20e64b3f16164d80bece03d8c97'
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
- To run the production server
    ```bash
      cd ACME-Education/acme-education-frontend
      npm run dev
    ```
- To run the frontend app
    ```bash
      cd ACME-Education/acme-education-frontend
      npm run build
    ```
- To run the app on a server
    ```bash
      cd ACME-Education/acme-education-frontend
      npm run start
    ```

Run the back end
- Starting the database and populating it
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

You can find the API documentation by following this [link](https://night-belly-22c.notion.site/ACME-Education-API-Docs-77ef7af075cd44829cdfcb8d4d45dd79?pvs=4) or see a less cooler version by navigating to `api/v1/Documentation` in the repo and see the MD file.

## Running Tests

The test are devided according to the HTTP method. This way we get the advantage of isolating different casses for each endpoint. This also give the advantages of having the ability to test for a specific HTTP method without having to look for a specific case is a rather long file.

To run tests dedicated for the API, move into the the folder containting the method you would like to test.

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

- DRIHMIA Redouane - [Email](drihmia.redouane@gmail.com)
- Mohammed Omer - [Github](https://github.com/MegaChie) / [LinkedIn](www.linkedin.com/in/mohamed-omer-63b24b21b)
- Ubonisrael Amos Akpanudoh - [Github](https://github.com/ubonisrael) / [LinkedIn](https://linkedin.com/in/ubonisrael-akpanudoh-44ba82246/) / [Email](akpanudohubonisrael@gmail.com)

## License

[MIT](https://choosealicense.com/licenses/mit/)
