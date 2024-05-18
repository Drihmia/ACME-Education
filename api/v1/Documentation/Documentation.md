# ACME Education - API Docs

- [GET]
    - `**[GET]` List All States**
        
        
        | Description | Fetches all the states found on the database, or one particular state when a valid ID is passed |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/states |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one state from the other. Adding it to the URL queries the database and receives the state that has this particular ID | None |
        - **✅ Response 200 - Without ID**
            
            ```python
            [
              {
                "__class__": "State",
                "created_at": "2024-05-05T17:11:00.000000",
                "id": "1a75408f-ccd6-4f1c-9574-b9cdd91394bf",
                "name": "Beni Mellal-Khenifra",
                "updated_at": "2024-05-05T17:11:00.000000"
              },
              {
                "__class__": "State",
                "created_at": "2024-05-05T17:11:16.000000",
                "id": "3935d757-3495-4123-be14-a853f8903193",
                "name": "Casablanca-Settat",
                "updated_at": "2024-05-05T17:11:16.000000"
              },
              {
                "__class__": "State",
                "created_at": "2024-05-05T17:11:30.000000",
                "id": "3ab5cfc3-c014-4044-b68b-caf8a7a9b731",
                "name": "Marrakech-Safi",
                "updated_at": "2024-05-05T17:11:30.000000"
              },
              {
                "__class__": "State",
                "created_at": "2024-05-05T17:12:14.000000",
                "id": "51b6898e-5f15-4a3c-91d2-93bbffc06743",
                "name": "Laayoune-Sakia El Hamra",
                "updated_at": "2024-05-05T17:12:14.000000"
              },...
            ]
            ```
            
        - **✅ Response 200 - With ID**
            
            ```jsx
            {
                "__class__": "State",
                "created_at": "2024-05-05T17:11:16.000000",
                "id": "3935d757-3495-4123-be14-a853f8903193",
                "name": "Casablanca-Settat",
                "updated_at": "2024-05-05T17:11:16.000000"
            }
            ```
            
        - **✅ Response (non-valid ID) 404**
            
            ```jsx
            {
            	"error": "UNKNOWN STATE"
            }
            ```
            
        
        ---
        
        - **`GET]`Cities In A State**
            
            
            | Description | List all cities in a state |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/states/6e381577-72ad-43f9-a3c9-a0e89f3d2cee/cities |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description |
            | --- | --- | --- | --- |
            | url params |  |  |  |
            | ID | String | Yes | Represent the state ID of which you wish lo list the cities in |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "City",
                    "created_at": "2024-05-05T17:11:07.000000",
                    "id": "01893441-c6f5-4b0a-a68f-4913ec2dd02c",
                    "name": "Tighassaline",
                    "state_id": "1a75408f-ccd6-4f1c-9574-b9cdd91394bf",
                    "updated_at": "2024-05-05T17:11:07.000000"
                  },
                  {
                    "__class__": "City",
                    "created_at": "2024-05-05T17:11:03.000000",
                    "id": "06728af2-6976-4097-8224-ccd8b1cdeae1",
                    "name": "Elkbab",
                    "state_id": "1a75408f-ccd6-4f1c-9574-b9cdd91394bf",
                    "updated_at": "2024-05-05T17:11:03.000000"
                  },
                  {
                    "__class__": "City",
                    "created_at": "2024-05-05T17:11:00.000000",
                    "id": "0810b471-a3af-4481-9571-482675b4fb9c",
                    "name": "Boujniba",
                    "state_id": "1a75408f-ccd6-4f1c-9574-b9cdd91394bf",
                    "updated_at": "2024-05-05T17:11:00.000000"
                  },
                  {
                    "__class__": "City",
                    "created_at": "2024-05-05T17:11:02.000000",
                    "id": "0c11aebc-4cb6-4f2c-be4b-2082756a1cf8",
                    "name": "Khenifra",
                    "state_id": "1a75408f-ccd6-4f1c-9574-b9cdd91394bf",
                    "updated_at": "2024-05-05T17:11:02.000000"
                  },...
                ]
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKNOWN STATE"
                }
                ```
                
        
        ---
        
    - `**[GET]` List All Cities**
        
        
        | Description | Fetches all the cities in the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/cities |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one state from the other. Adding it to the URL queries the database and receives the city that has this particular ID | None |
        - **✅ Response 200 - Without ID**
            
            ```python
            [
              {
                "__class__": "City",
                "created_at": "2024-05-05T17:10:27.000000",
                "id": "002d32c6-1f48-4e06-bfee-ac63868a7250",
                "name": "Selouane",
                "state_id": "605ec99e-7ae8-4b7f-8b89-79c01a52d4db",
                "updated_at": "2024-05-05T17:10:27.000000"
              },
              {
                "__class__": "City",
                "created_at": "2024-05-05T17:11:49.000000",
                "id": "0064ce5d-d3c4-43ac-a631-8325248103fe",
                "name": "Itzer",
                "state_id": "d4a8de83-3b75-4579-b6fb-c25cf56a27c5",
                "updated_at": "2024-05-05T17:11:49.000000"
              },
              {
                "__class__": "City",
                "created_at": "2024-05-05T17:13:02.000000",
                "id": "01596a85-6d6f-43b5-898c-9586df902455",
                "name": "El Kel\u00e2a des  S",
                "state_id": "3ab5cfc3-c014-4044-b68b-caf8a7a9b731",
                "updated_at": "2024-05-05T17:13:02.000000"
              },
              {
                "__class__": "City",
                "created_at": "2024-05-05T17:11:07.000000",
                "id": "01893441-c6f5-4b0a-a68f-4913ec2dd02c",
                "name": "Tighassaline",
                "state_id": "1a75408f-ccd6-4f1c-9574-b9cdd91394bf",
                "updated_at": "2024-05-05T17:11:07.000000"
              },...
            ]
            ```
            
        - **✅ Response 200 - With ID**
            
            ```python
            {
              "__class__": "City",
              "created_at": "2024-05-05T17:11:49.000000",
              "id": "0064ce5d-d3c4-43ac-a631-8325248103fe",
              "name": "Itzer",
              "state_id": "d4a8de83-3b75-4579-b6fb-c25cf56a27c5",
              "updated_at": "2024-05-05T17:11:49.000000"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN CITY"}
            ```
            
        
        ---
        
        - `**[GET]` Institutes In a City**
            
            
            | Description | Fetches all the institutes residing in one city |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/cities/bde27a09-8696-4e4d-a758-9949839a75b9/institutions |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | The ID of the cities we wish to list all the institutes in. | None |
            - **✅ Response 200 - Without ID**
                
                ```python
                [
                  {
                    "__class__": "Institution",
                    "city": "Rabat",
                    "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                    "created_at": "2024-05-05T17:38:37.000000",
                    "id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
                    "name": "GROUPE SCOLAIRE PRIVE LES QUATRE TEMPS",
                    "updated_at": "2024-05-05T17:38:37.000000"
                  },
                  {
                    "__class__": "Institution",
                    "city": "Rabat",
                    "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                    "created_at": "2024-05-05T17:18:03.000000",
                    "id": "01a0ac61-a88a-4c45-b447-6a32f443dbf7",
                    "name": "Institution Ibrahim al khalil scientifique priv\u00e9",
                    "updated_at": "2024-05-05T17:18:03.000000"
                  },
                  {
                    "__class__": "Institution",
                    "city": "Rabat",
                    "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                    "created_at": "2024-05-05T17:17:40.000000",
                    "id": "0202b596-f87f-4c73-bee6-2406e0f47bc1",
                    "name": "Youssef bno Tachafine",
                    "updated_at": "2024-05-05T17:17:40.000000"
                  },
                  {
                    "__class__": "Institution",
                    "city": "Rabat",
                    "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                    "created_at": "2024-05-05T18:09:15.000000",
                    "id": "034ebbcb-a91f-4832-87ca-c8cb5ce6c0dd",
                    "name": "AL ALAMA   MOHAMED BEN SOULAIMANE EL JAZOULI",
                    "updated_at": "2024-05-05T18:09:15.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Institutes In City**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN CITY"
                }
                ```
                
            
        
        ---
        
        - `**[GET]` State Of The City**
            
            
            | Description | Fetches the state of the chosen city |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/cities/bde27a09-8696-4e4d-a758-9949839a75b9/state |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | The ID identifying the city of choice that we wish to get the state of. | None |
            - **✅ Response 200**
                
                ```python
                {
                  "__class__": "State",
                  "created_at": "2024-05-05T17:10:49.000000",
                  "id": "bc065409-a41a-4343-b554-d428d06561f4",
                  "name": "Rabat-Sale-Kenitra",
                  "updated_at": "2024-05-05T17:10:49.000000"
                }
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN CITY"
                }
                ```
                
    - `**[GET]`List All Institutions**
        
        
        | Description | Fetches all the institutes in the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/institutions |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Place | Description |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one state from the other. Adding it to the URL queries the database and receives the institute that has this particular ID | None |
        - **✅ Response 200 - Without ID**
            
            ```python
            [
              {
                "__class__": "Institution",
                "city": "Rabat",
                "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                "created_at": "2024-05-05T17:38:37.000000",
                "id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
                "name": "GROUPE SCOLAIRE PRIVE LES QUATRE TEMPS",
                "updated_at": "2024-05-05T17:38:37.000000"
              },
              {
                "__class__": "Institution",
                "city": "Marrakech",
                "city_id": "0baddb7b-b409-4bda-9cec-9a4459599ca1",
                "created_at": "2024-05-05T18:13:47.000000",
                "id": "0000eef8-2d7a-4b8f-a1f6-9a9993c0561f",
                "name": "ss AIT CHEIKH centrale",
                "updated_at": "2024-05-05T18:13:47.000000"
              },
              {
                "__class__": "Institution",
                "city": "Tanger-Assila",
                "city_id": "612cd7d0-4667-4720-a8d9-caca91439241",
                "created_at": "2024-05-05T17:37:52.000000",
                "id": "000ab78b-46ee-45e7-962f-3706b7f8e8e1",
                "name": "GROUPE SCOLAIRE AL AYOUBI 3",
                "updated_at": "2024-05-05T17:37:52.000000"
              },
              {
                "__class__": "Institution",
                "city": "El Kel\u00e2a des  S",
                "city_id": "01596a85-6d6f-43b5-898c-9586df902455",
                "created_at": "2024-05-05T17:18:35.000000",
                "id": "000c45ba-a9e0-4fc6-b316-0b35982bc04f",
                "name": "Etablissement Oumnia II",
                "updated_at": "2024-05-05T17:18:35.000000"
              },...
            ]
            ```
            
        - **✅ Response 200 - With ID**
            
            ```python
            {
              "__class__": "Institution",
              "city": "Rabat",
              "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
              "created_at": "2024-05-05T17:38:37.000000",
              "id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
              "name": "GROUPE SCOLAIRE PRIVE LES QUATRE TEMPS",
              "updated_at": "2024-05-05T17:38:37.000000"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
              "error": "UNKNOWN INSTITUTION"
            }
            ```
            
        
        ---
        
        - `**[GET]`Lessons Of Institute**
            
            
            | Description | Fetches all the lessons of an institute |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/institutions/cfddfd7f-c1ff-4c7d-89b4-9db1f5efdad5/lessons |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | The identifier of the institute of choice that we wish to get all the lessons taught in. | None |
            - **✅ Response 200**
                
                ```python
                {}
                ```
                
            - **✅ Response 200 - No Lessons In Institutes**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN INSTITUTION"
                }
                ```
                
        
        ---
        
        - `**[GET]`Teachers Of An Institutes**
            
            
            | Description | Fetches all teachers working in an institute |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/institutions/cfddfd7f-c1ff-4c7d-89b4-9db1f5efdad5/teachers |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | Identifier to reference the institute that we wish to list the teachers in. | None |
            - **✅ Response 200**
                
                ```jsx
                {}
                ```
                
            - **✅ Response 404**
                
                ```jsx
                {}
                ```
                
        
        ---
        
        - `**[GET]`Subject Of An Institutes**
            
            
            | Description | Fetches all teachers working in an institute |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/institutions/cfddfd7f-c1ff-4c7d-89b4-9db1f5efdad5/subjects |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | Identifier to reference the institute that we wish to list the subject taught in. | None |
            - **✅ Response 200**
                
                ```python
                {}
                ```
                
            - **✅ Response 200 - No Subjects In Institute**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN INSTITUTION"
                }
                ```
                
        
        ---
        
        - `**[GET]`Years Of An Institutes**
            
            
            | Description | Fetches all years of an institute that a student can enroll in  |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/institutions/cfddfd7f-c1ff-4c7d-89b4-9db1f5efdad5/classes |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | Identifier to reference the institute that we wish to list the different years of studying in. | None |
            - **✅ Response 200**
                
                ```python
                {}
                ```
                
            - **✅ Response 200 - No Years In Institute**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN INSTITUTION"
                }
                ```
                
        
        ---
        
        - `**[GET]`Students Of An Institutes**
            
            
            | Description | Fetches a list of enrolled students in this institute |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/institutions/cfddfd7f-c1ff-4c7d-89b4-9db1f5efdad5/students |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | url params |  |  |  |  |
            | ID | String | Yes | Identifier to reference the institute that we wish to list the students enrolled in this particular institute. | None |
            - **✅ Response 200**
                
                ```python
                {}
                ```
                
            - **✅ Response 200 - No Students In Institute**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN INSTITUTION"
                }
                ```
                
    - `**[GET]` List All Subjects**
        
        
        | Description | Fetches all the subjects inside the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/subjects |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Place | Description |
        | --- | --- | --- | --- | --- |
        | body params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one state from the other. Adding it to the URL queries the database and receives the subject that has this particular ID | None |
        - **✅ Response 200 - Without ID**
            
            ```python
            [
              {
                "__class__": "Subject",
                "created_at": "2024-05-09T19:04:38.000000",
                "id": "357c7621-9d37-40d4-83a5-4942ef123576",
                "name": "Langue Espagnole",
                "updated_at": "2024-05-09T19:05:23.000000"
              },
              {
                "__class__": "Subject",
                "created_at": "2024-05-09T19:04:36.000000",
                "id": "431aff91-1b6c-468f-9801-8025268885c2",
                "name": "Math\u00e9matiques",
                "updated_at": "2024-05-09T19:05:22.000000"
              },
              {
                "__class__": "Subject",
                "created_at": "2024-05-09T19:04:39.000000",
                "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                "name": "\u00c9ducation Islamique",
                "updated_at": "2024-05-09T19:05:24.000000"
              },
              {
                "__class__": "Subject",
                "created_at": "2024-05-09T19:04:35.000000",
                "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                "name": "Sciences de la Vie et de la Terre",
                "updated_at": "2024-05-09T19:05:21.000000"
              },...
            ]
            ```
            
        - **✅ Response 200 - With ID**
            
            ```python
            {
              "__class__": "Subject",
              "created_at": "2024-05-09T19:04:39.000000",
              "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
              "name": "\u00c9ducation Islamique",
              "updated_at": "2024-05-09T19:05:24.000000"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
              "error": "UNKNOWN SUBJECT"
            }
            ```
            
        
        ---
        
        - `**[GET]` Institutes Of A Subject**
            
            
            | Description | Fetches all institutes that has this subject in their curriculum |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/subjects/13d20ac5-5133-42b7-b63c-726b7fbe2997/institutions |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Institution",
                    "city": "Sale",
                    "city_id": "9b47b62c-83bd-4911-a0a8-3a9121c28425",
                    "created_at": "2024-05-05T17:54:24.000000",
                    "id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
                    "name": "LYCEE QUALIFIANT ALMANDAR ALJAMIL",
                    "updated_at": "2024-05-09T19:44:52.000000"
                  },
                  {
                    "__class__": "Institution",
                    "city": "Sale",
                    "city_id": "9b47b62c-83bd-4911-a0a8-3a9121c28425",
                    "created_at": "2024-05-05T17:54:25.000000",
                    "id": "2b045809-6be4-4e27-b289-18d48faf009c",
                    "name": "LYCEE QUALIFIANT KADI AYAD",
                    "updated_at": "2024-05-09T19:05:18.000000"
                  },
                  {
                    "__class__": "Institution",
                    "city": "Sale",
                    "city_id": "9b47b62c-83bd-4911-a0a8-3a9121c28425",
                    "created_at": "2024-05-05T17:54:25.000000",
                    "id": "2fd3c0af-b71c-4414-b01f-a2c38c860930",
                    "name": "LYCEE QUALIFIANT JABER IBN HAYANE",
                    "updated_at": "2024-05-09T19:05:17.000000"
                  },
                  {
                    "__class__": "Institution",
                    "city": "Tanger-Assila",
                    "city_id": "612cd7d0-4667-4720-a8d9-caca91439241",
                    "created_at": "2024-05-05T18:07:06.000000",
                    "id": "3079df69-b757-497e-9e17-9ae4c8a1fd06",
                    "name": "LYCEE COLLEGIAL JABIR BNOU HAYYANE",
                    "updated_at": "2024-05-09T19:05:19.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Subject**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN SUBJECT"
                }
                ```
                
        
        ---
        
        - `**[GET]` Lessons Of A Subject**
            
            
            | Description | Fetches all lessons in one subject |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/subjects/13d20ac5-5133-42b7-b63c-726b7fbe2997/lessons |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Lesson",
                    "created_at": "2024-05-09T19:05:05.000000",
                    "description": "lesson N6 for my student related to Physics",
                    "download_link": "https://drive.google.com/file/d/1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/view?usp=sharing",
                    "id": "18a6feb4-668d-4881-9f98-7e5c62ef37e8",
                    "name": "Direct electric current",
                    "public": false,
                    "subject": "Physique-Chimie",
                    "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "teacher": "Redouane DRIHMIA",
                    "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "updated_at": "2024-05-09T19:05:33.000000"
                  },
                  {
                    "__class__": "Lesson",
                    "created_at": "2024-05-09T19:44:51.000000",
                    "description": "Null",
                    "download_link": "ttps",
                    "id": "1c1f825e-469c-43e6-bd21-2a5640549a70",
                    "name": "Direct electric curre",
                    "public": true,
                    "subject": "Physique-Chimie",
                    "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "teacher": "Redouane DRIHMIA",
                    "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "updated_at": "2024-05-09T19:44:54.000000"
                  },
                  {
                    "__class__": "Lesson",
                    "created_at": "2024-05-09T19:05:05.000000",
                    "description": "lesson N6 for my student related to Chemistry",
                    "download_link": "https://drive.google.com/file/d/1rnI4FRlHJxFqvNE_7M1o7jDDgfzJ782U/view",
                    "id": "1d575372-097e-468e-99fd-117fa8ee666c",
                    "name": "Periodic Classification of Chemical Elements",
                    "public": true,
                    "subject": "Physique-Chimie",
                    "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "teacher": "Redouane DRIHMIA",
                    "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "updated_at": "2024-05-09T19:05:33.000000"
                  },
                  {
                    "__class__": "Lesson",
                    "created_at": "2024-05-09T19:27:50.000000",
                    "description": "nothing to provide",
                    "download_link": "https://drive.google.com/file/d/1BYiLeCJ1gIpxtIVDTd3Sc93TzB6t5Vui/view",
                    "id": "30a407a1-d5b5-4dc7-9f20-6fea98400cd8",
                    "name": "PH6: Analysis of Force Vectors in an Orthogonal Coordinate System",
                    "public": true,
                    "subject": "Physique-Chimie",
                    "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "teacher": "Redouane DRIHMIA",
                    "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "updated_at": "2024-05-09T19:31:42.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Subject**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN SUBJECT"
                }
                ```
                
        
        ---
        
        - `**[GET]` Teachers Of A Subject**
            
            
            | Description | Fetches all teachers of one subject |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/subjects/13d20ac5-5133-42b7-b63c-726b7fbe2997/teachers |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Teacher",
                    "city": "Sale",
                    "created_at": "2024-05-09T19:04:44.000000",
                    "email": "red1@gmail.com",
                    "first_name": "redouane",
                    "gender": "M",
                    "id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "institution": "LYCEE QUALIFIANT ALMANDAR ALJAMIL",
                    "last_name": "DRIHMIA",
                    "main_subject": null,
                    "phone_number": "+212683984948",
                    "updated_at": "2024-05-10T21:10:40.000000"
                  },
                  {
                    "__class__": "Teacher",
                    "city": "Sale",
                    "created_at": "2024-05-09T19:04:45.000000",
                    "email": "omer1@gmail.com",
                    "first_name": "OMER",
                    "gender": "M",
                    "id": "7159412a-c8cc-4016-b617-65bf7414840a",
                    "institution": "LYCEE QUALIFIANT ALMANDAR ALJAMIL",
                    "last_name": "Mohamed",
                    "main_subject": null,
                    "phone_number": "+212698765432",
                    "updated_at": "2024-05-09T19:05:31.000000"
                  }
                ]
                ```
                
            - **✅ Response 200 - No Data In Subject**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                  "error": "UNKNOWN SUBJECT"
                }
                ```
                
    - `**[GET]` List All Teachers**
        
        
        | Description | Fetches all the teachers inside the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/teachers |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | body params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one Teacher from the other. Adding it to the URL queries the database and receives the teachers that have this particular ID | None |
        - **✅ Response 200**
            
            ```python
            [
              {
                "__class__": "Teacher",
                "city": "Sidi Kacem",
                "created_at": "2024-05-09T19:04:44.000000",
                "email": "red2@gmail.com",
                "first_name": "DRIHMIA",
                "gender": "M",
                "id": "4cb13c99-da57-4e31-af15-341ab83df3e4",
                "institution": "LYCEE OUHOUD",
                "last_name": "Redouane",
                "main_subject": null,
                "phone_number": "+2126123456452",
                "updated_at": "2024-05-09T19:05:30.000000"
              },
              {
                "__class__": "Teacher",
                "city": "Sale",
                "created_at": "2024-05-09T19:04:44.000000",
                "email": "red1@gmail.com",
                "first_name": "redouane",
                "gender": "M",
                "id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                "institution": "LYCEE QUALIFIANT ALMANDAR ALJAMIL",
                "last_name": "DRIHMIA",
                "main_subject": null,
                "phone_number": "+212683984948",
                "updated_at": "2024-05-10T21:10:40.000000"
              },
              {
                "__class__": "Teacher",
                "city": "Sale",
                "created_at": "2024-05-09T19:04:45.000000",
                "email": "omer1@gmail.com",
                "first_name": "OMER",
                "gender": "M",
                "id": "7159412a-c8cc-4016-b617-65bf7414840a",
                "institution": "LYCEE QUALIFIANT ALMANDAR ALJAMIL",
                "last_name": "Mohamed",
                "main_subject": null,
                "phone_number": "+212698765432",
                "updated_at": "2024-05-09T19:05:31.000000"
              },
              {
                "__class__": "Teacher",
                "city": "Sale",
                "created_at": "2024-05-09T19:04:46.000000",
                "email": "omer2@gmail.com",
                "first_name": "OMER",
                "gender": "M",
                "id": "fd693fc1-5945-4e7d-a695-c6cedd699eaf",
                "institution": "LYCEE QUALIFIANT JABER IBN HAYANE",
                "last_name": "OMER",
                "main_subject": null,
                "phone_number": "+212610928374",
                "updated_at": "2024-05-09T19:05:31.000000"
              }
            ]
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            	"error": "UNKOWN TEACHER"
            }
            ```
            
        
        ---
        
        - `**[GET]` Subject of a teacher**
            
            
            | Description | Fetches all subjects taught by a teacher |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/teachers/27f396cd-50f6-4692-87a7-9e79c7fa42fb/subjects |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:36.000000",
                    "id": "431aff91-1b6c-468f-9801-8025268885c2",
                    "name": "Math\u00e9matiques",
                    "updated_at": "2024-05-09T19:05:22.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:39.000000",
                    "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                    "name": "\u00c9ducation Islamique",
                    "updated_at": "2024-05-09T19:05:24.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                    "name": "Sciences de la Vie et de la Terre",
                    "updated_at": "2024-05-09T19:05:21.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "name": "Physique-Chimie",
                    "updated_at": "2024-05-09T19:05:20.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Teachers**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKOWN TEACHER"
                }
                ```
                
        - `**[GET]` Lessons of a teacher**
            
            
            | Description | Fetches all lessons created by a teacher |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/teachers/27f396cd-50f6-4692-87a7-9e79c7fa42fb/lessons |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:36.000000",
                    "id": "431aff91-1b6c-468f-9801-8025268885c2",
                    "name": "Math\u00e9matiques",
                    "updated_at": "2024-05-09T19:05:22.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:39.000000",
                    "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                    "name": "\u00c9ducation Islamique",
                    "updated_at": "2024-05-09T19:05:24.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                    "name": "Sciences de la Vie et de la Terre",
                    "updated_at": "2024-05-09T19:05:21.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "name": "Physique-Chimie",
                    "updated_at": "2024-05-09T19:05:20.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Teachers**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKOWN TEACHER"
                }
                ```
                
        - `**[GET]` Institutions of a teacher**
            
            
            | Description | Fetches all institutions where that teacher is working |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/teachers/27f396cd-50f6-4692-87a7-9e79c7fa42fb/institutions |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:36.000000",
                    "id": "431aff91-1b6c-468f-9801-8025268885c2",
                    "name": "Math\u00e9matiques",
                    "updated_at": "2024-05-09T19:05:22.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:39.000000",
                    "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                    "name": "\u00c9ducation Islamique",
                    "updated_at": "2024-05-09T19:05:24.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                    "name": "Sciences de la Vie et de la Terre",
                    "updated_at": "2024-05-09T19:05:21.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "name": "Physique-Chimie",
                    "updated_at": "2024-05-09T19:05:20.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Teachers**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKOWN TEACHER"
                }
                ```
                
        - `**[GET]` Years of a teacher**
            
            
            | Description | Fetches all teachers giving this subject in their curriculum |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/teachers/27f396cd-50f6-4692-87a7-9e79c7fa42fb/classes |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:36.000000",
                    "id": "431aff91-1b6c-468f-9801-8025268885c2",
                    "name": "Math\u00e9matiques",
                    "updated_at": "2024-05-09T19:05:22.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:39.000000",
                    "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                    "name": "\u00c9ducation Islamique",
                    "updated_at": "2024-05-09T19:05:24.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                    "name": "Sciences de la Vie et de la Terre",
                    "updated_at": "2024-05-09T19:05:21.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "name": "Physique-Chimie",
                    "updated_at": "2024-05-09T19:05:20.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Teachers**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKOWN TEACHER"
                }
                ```
                
        
        ---
        
    - `**[GET]` List All Students**
        
        
        | Description | Fetches all the students inside the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/students |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Place | Description |
        | --- | --- | --- | --- | --- |
        | body params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one state from the other. Adding it to the URL queries the database and receives the student that has this particular ID | None |
        - **✅ Response 200 - Without ID**
            
            ```python
            [
              {
                "__class__": "Student",
                "city": null,
                "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
                "created_at": "2024-05-09T19:04:56.000000",
                "email": "hicham@gmail.com",
                "first_name": "student_2",
                "gender": "M",
                "id": "0f2a5390-d304-4be8-b1a8-9ca03d22a342",
                "institution": null,
                "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
                "last_name": "hicham",
                "phone_number": null,
                "teacher_email": "red1@gmail.com",
                "updated_at": "2024-05-09T19:05:32.000000"
              },
              {
                "__class__": "Student",
                "city": null,
                "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
                "created_at": "2024-05-09T19:04:56.000000",
                "email": "marwan@gmail.com",
                "first_name": "student_1",
                "gender": "M",
                "id": "9385de5f-32cc-42a0-8dc6-540bb93cb1e8",
                "institution": null,
                "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
                "last_name": "marwan",
                "phone_number": null,
                "teacher_email": "red1@gmail.com",
                "updated_at": "2024-05-09T19:05:32.000000"
              },
              {
                "__class__": "Student",
                "city": null,
                "class_id": "7c71385d-0e4c-4691-850f-f0855e04baea",
                "created_at": "2024-05-09T19:04:58.000000",
                "email": "yasmine@gmail.com",
                "first_name": "student_4",
                "gender": "F",
                "id": "b3ea6da4-734c-425f-bbc6-73f71131cb14",
                "institution": null,
                "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
                "last_name": "yasmine",
                "phone_number": null,
                "teacher_email": "red2@gmail.com",
                "updated_at": "2024-05-09T19:05:33.000000"
              },
              {
                "__class__": "Student",
                "city": null,
                "class_id": "7c71385d-0e4c-4691-850f-f0855e04baea",
                "created_at": "2024-05-09T19:04:57.000000",
                "email": "fatima@gmail.com",
                "first_name": "student_3",
                "gender": "F",
                "id": "b634a8a3-1611-49a7-8bca-8132d25c6e60",
                "institution": null,
                "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
                "last_name": "fatima",
                "phone_number": null,
                "teacher_email": "red1@gmail.com",
                "updated_at": "2024-05-09T19:05:32.000000"
              }
            ]
            ```
            
        - **✅ Response 200 - With ID**
            
            ```python
            {
              "__class__": "Student",
              "city": null,
              "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
              "created_at": "2024-05-09T19:04:56.000000",
              "email": "hicham@gmail.com",
              "first_name": "student_2",
              "gender": "M",
              "id": "0f2a5390-d304-4be8-b1a8-9ca03d22a342",
              "institution": null,
              "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
              "last_name": "hicham",
              "phone_number": null,
              "teacher_email": "red1@gmail.com",
              "updated_at": "2024-05-09T19:05:32.000000"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
              "error": "UNKNOWN STUDENT"
            }
            ```
            
        
        ---
        
        - `**[GET]` Year Of A Student**
            
            
            | Description | Fetches all the years that a particular student is in |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/students/9aae4684-7f9c-4066-8592-9e4a440d097f/classes |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description |
            | --- | --- | --- | --- |
            | url params |  |  |  |
            | ID | String | Yes | The ID of the particular student we wish to get the institutes the current year that the student is in. |
            - **✅ Response 200**
                
                ```python
                {
                  "__class__": "Clas",
                  "created_at": "2024-05-09T19:04:40.000000",
                  "id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
                  "name": "(French) Commun Core",
                  "updated_at": "2024-05-09T19:44:53.000000"
                }
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKNOWN STUDENT"
                }
                ```
                
        
        ---
        
        - `**[GET]` Institutes Of A Student**
            
            
            | Description | Fetches all the Institute that a particular student is enrolled in |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/students/9aae4684-7f9c-4066-8592-9e4a440d097f/institutions |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description |
            | --- | --- | --- | --- |
            | url params |  |  |  |
            | ID | String | Yes | The ID of the particular student we wish to get the institutes the student is enrolled in |
            - **✅ Response 200**
                
                ```python
                {
                  "__class__": "Institution",
                  "city": "Sale",
                  "city_id": "9b47b62c-83bd-4911-a0a8-3a9121c28425",
                  "created_at": "2024-05-05T17:54:24.000000",
                  "id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
                  "name": "LYCEE QUALIFIANT ALMANDAR ALJAMIL",
                  "updated_at": "2024-05-09T19:44:52.000000"
                }
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKNOWN STUDENT"
                }
                ```
                
        
        ---
        
        - `**[GET]` Subjects Of A Student**
            
            
            | Description | Fetches all the Subjects that a particular student studies |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/students/9aae4684-7f9c-4066-8592-9e4a440d097f/subjects |
            | Auth Required |  |
            
            | Paramater | Type  | Required | Description |
            | --- | --- | --- | --- |
            | url params |  |  |  |
            | ID | String | Yes | The ID of the particular student we wish to get the subjects he attends |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:38.000000",
                    "id": "357c7621-9d37-40d4-83a5-4942ef123576",
                    "name": "Langue Espagnole",
                    "updated_at": "2024-05-09T19:05:23.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:36.000000",
                    "id": "431aff91-1b6c-468f-9801-8025268885c2",
                    "name": "Math\u00e9matiques",
                    "updated_at": "2024-05-09T19:05:22.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:39.000000",
                    "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                    "name": "\u00c9ducation Islamique",
                    "updated_at": "2024-05-09T19:05:24.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                    "name": "Sciences de la Vie et de la Terre",
                    "updated_at": "2024-05-09T19:05:21.000000"
                  },...
                ]
                ```
                
            - **✅ Response 404 - No Subjects**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKNOWN STUDENT"
                }
                ```
                
        
        ---
        
        - `**[GET]` Lessons Of A Student**
            
            
            | Description | Fetches all the lessons that a particular student studies |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/students/9aae4684-7f9c-4066-8592-9e4a440d097f/lessons |
            | Auth Required |  |
            
            | Paramater | Type  | Required | Description |
            | --- | --- | --- | --- |
            | url params |  |  |  |
            | ID | String | Yes | The ID of the particular student we wish to get the lessons he attends |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Lesson",
                    "created_at": "2024-05-09T19:05:05.000000",
                    "description": "lesson N6 for my student related to Physics",
                    "download_link": "https://drive.google.com/file/d/1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/view?usp=sharing",
                    "id": "18a6feb4-668d-4881-9f98-7e5c62ef37e8",
                    "name": "Direct electric current",
                    "public": false,
                    "subject": "Physique-Chimie",
                    "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "teacher": "Redouane DRIHMIA",
                    "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "updated_at": "2024-05-09T19:05:33.000000"
                  },
                  {
                    "__class__": "Lesson",
                    "created_at": "2024-05-09T19:05:05.000000",
                    "description": "lesson N6 for my student related to Chemistry",
                    "download_link": "https://drive.google.com/file/d/1rnI4FRlHJxFqvNE_7M1o7jDDgfzJ782U/view",
                    "id": "1d575372-097e-468e-99fd-117fa8ee666c",
                    "name": "Periodic Classification of Chemical Elements",
                    "public": true,
                    "subject": "Physique-Chimie",
                    "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "teacher": "Redouane DRIHMIA",
                    "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                    "updated_at": "2024-05-09T19:05:33.000000"
                  }
                ]
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKNOWN STUDENT"
                }
                ```
                
            - **✅ Response 404 - No Lessons**
                
                ```python
                []
                ```
                
    - `**[GET]`List All Lessons**
        
        
        | Description | Fetches all the Lessons in the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/lessons |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Place | Description |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | No | A UD-ID used to distinguish one state from the other. Adding it to the URL queries the database and receives the lessons that has this particular ID | None |
        - **✅ Response 200 -Without ID**
            
            ```python
            [
              {
                "__class__": "Lesson",
                "created_at": "2024-05-09T19:05:05.000000",
                "description": "lesson N6 for my student related to Physics",
                "download_link": "https://drive.google.com/file/d/1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/view?usp=sharing",
                "id": "18a6feb4-668d-4881-9f98-7e5c62ef37e8",
                "name": "Direct electric current",
                "public": false,
                "subject": "Physique-Chimie",
                "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                "teacher": "Redouane DRIHMIA",
                "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                "updated_at": "2024-05-09T19:05:33.000000"
              },
              {
                "__class__": "Lesson",
                "created_at": "2024-05-09T19:44:51.000000",
                "description": "Null",
                "download_link": "ttps",
                "id": "1c1f825e-469c-43e6-bd21-2a5640549a70",
                "name": "Direct electric curre",
                "public": true,
                "subject": "Physique-Chimie",
                "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                "teacher": "Redouane DRIHMIA",
                "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                "updated_at": "2024-05-09T19:44:54.000000"
              },
              {
                "__class__": "Lesson",
                "created_at": "2024-05-09T19:05:05.000000",
                "description": "lesson N6 for my student related to Chemistry",
                "download_link": "https://drive.google.com/file/d/1rnI4FRlHJxFqvNE_7M1o7jDDgfzJ782U/view",
                "id": "1d575372-097e-468e-99fd-117fa8ee666c",
                "name": "Periodic Classification of Chemical Elements",
                "public": true,
                "subject": "Physique-Chimie",
                "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                "teacher": "Redouane DRIHMIA",
                "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                "updated_at": "2024-05-09T19:05:33.000000"
              },
              {
                "__class__": "Lesson",
                "created_at": "2024-05-09T19:27:50.000000",
                "description": "nothing to provide",
                "download_link": "https://drive.google.com/file/d/1BYiLeCJ1gIpxtIVDTd3Sc93TzB6t5Vui/view",
                "id": "30a407a1-d5b5-4dc7-9f20-6fea98400cd8",
                "name": "PH6: Analysis of Force Vectors in an Orthogonal Coordinate System",
                "public": true,
                "subject": "Physique-Chimie",
                "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                "teacher": "Redouane DRIHMIA",
                "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
                "updated_at": "2024-05-09T19:31:42.000000"
              },...
            ]
            ```
            
        - **✅ Response 200 -With ID**
            
            ```python
            {
              "__class__": "Lesson",
              "created_at": "2024-05-09T19:05:05.000000",
              "description": "lesson N6 for my student related to Physics",
              "download_link": "https://drive.google.com/file/d/1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/view?usp=sharing",
              "id": "18a6feb4-668d-4881-9f98-7e5c62ef37e8",
              "name": "Direct electric current",
              "public": false,
              "subject": "Physique-Chimie",
              "subject_id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
              "teacher": "Redouane DRIHMIA",
              "teacher_id": "68696e13-d591-47d6-83c3-4cc56c9d5593",
              "updated_at": "2024-05-09T19:05:33.000000"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
              "error": "UNKNOWN LESSON"
            }
            ```
            
        - `**[GET]` Public lessons**
            
            
            | Description | Fetches all public lessons in the database |
            | --- | --- |
            | URL | http://web-01.drihmia.tech/api/v1/public_lessons |
            | Auth Required | No |
            
            | Paramater | Type  | Required | Description | Default |
            | --- | --- | --- | --- | --- |
            | body params |  |  |  |  |
            | ID | String | Yes | The ID that distinguishes one institute from another. | None |
            - **✅ Response 200**
                
                ```python
                [
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:36.000000",
                    "id": "431aff91-1b6c-468f-9801-8025268885c2",
                    "name": "Math\u00e9matiques",
                    "updated_at": "2024-05-09T19:05:22.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:39.000000",
                    "id": "5422b360-2315-4343-9b8e-d43a0df8ed23",
                    "name": "\u00c9ducation Islamique",
                    "updated_at": "2024-05-09T19:05:24.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "60daf1b8-6c6d-4983-a8fc-255e30d5dd37",
                    "name": "Sciences de la Vie et de la Terre",
                    "updated_at": "2024-05-09T19:05:21.000000"
                  },
                  {
                    "__class__": "Subject",
                    "created_at": "2024-05-09T19:04:35.000000",
                    "id": "85e85fe1-1910-4eb1-92e5-ec8654e65265",
                    "name": "Physique-Chimie",
                    "updated_at": "2024-05-09T19:05:20.000000"
                  },...
                ]
                ```
                
            - **✅ Response 200 - No Data In Teachers**
                
                ```python
                []
                ```
                
            - **✅ Response 404**
                
                ```python
                {
                	"error": "UNKOWN TEACHER"
                }
                ```
                
        
        ---
        
- [POST]
    - `**[POST]` Create A State**
        
        
        | Description | Adds a state to the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/states |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | None | None | None | None | None |
        | body params |  |  |  |  |
        | name | String | Yes | The name that will be given to the created city. | Empty string |
        - **✅ Response 201**
            
            ```python
            {
                "__class__": "State",
                "created_at": "2024-05-05T17:11:16.000000",
                "id": "3935d757-3495-4123-be14-a853f8903193",
                "name": "Casablanca-Settat",
                "updated_at": "2024-05-05T17:11:16.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 400 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Missing Name**
            
            ```python
            {
            	"error": "Missing name"
            }
            ```
            
        - **✅ Response 400 - Already A State**
            
            ```python
            {
            	"error": "exists"
            }
            ```
            
    - `**[POST]` Create A City**
        
        
        | Description | Adds a city to the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/cities |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | None | None | None | None | None |
        | body params |  |  |  |  |
        | name | String | Yes | The name that will be given to the created city. | Empty string |
        | state_id | String | Yes | The ID reference of the State in which the city resides. | No |
        - **✅ Response 200**
            
            ```python
            {
                "__class__": "City",
                "created_at": "2024-05-05T17:10:27.000000",
                "id": "002d32c6-1f48-4e06-bfee-ac63868a7250",
                "name": "Selouane",
                "state_id": "605ec99e-7ae8-4b7f-8b89-79c01a52d4db",
                "updated_at": "2024-05-05T17:10:27.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - No Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Missing Name**
            
            ```python
            {
            	"error": "Missing name"
            }
            ```
            
        - **✅ Response 400 - Missing State ID**
            
            ```python
            {
            	"error": "Missing state_id"
            }
            ```
            
        - **✅ Response 400 - Already A City**
            
            ```python
            {
            	"error": "exists"
            }
            ```
            
    - `**[POST]` Create An Institution**
        
        
        | Description | Adds an institute to the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/institutions |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | None | None | None | None | None |
        | body params |  |  |  |  |
        | city_id | String | If state_id in not passed | The ID reference of the city in which the institute is located in. | No |
        | name | String | Yes | The name that will be given to the created institute. | Empty string |
        | state_id | String | If city_id is not found | The ID reference of the city in which the institute is located in. | No |
        - **✅ Response 200**
            
            ```python
            {
                "__class__": "Institution",
                "city": "Rabat",
                "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                "created_at": "2024-05-05T17:38:37.000000",
                "id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
                "name": "GROUPE SCOLAIRE PRIVE LES QUATRE TEMPS",
                "updated_at": "2024-05-05T17:38:37.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Missing Name**
            
            ```python
            {
            	"error": "Missing name"
            }
            ```
            
        - **✅ Response 400 - Fake City ID**
            
            ```python
            {
            	"error": "UNKOWN CITY"
            }
            ```
            
        - **✅ Response 400 - Missing City ID**
            
            ```python
            {
            	"error": "Missing state_id: provide city_id or city's name plus state_id"
            }
            ```
            
        - **✅ Response 400 - Missing City ID And No City Relating Information**
            
            ```python
            {
            	"error": "provide city's info, name or id"
            }
            ```
            
        - **✅ Response 400 - Already An Institute**
            
            ```python
            {
            	"error": "exists"
            }
            ```
            
    - `**[POST]` Create A Student**
        
        
        | Description | Adds a student to the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/students |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | None | None | None | None | None |
        | body params |  |  |  |  |
        | first_name | String | Yes | The first name that will be given to the created city. | No |
        | last_name | String | Yes | The last name that will be given to the created city. | No |
        | email | String | Yes | Email of the new student. | No |
        | password | String | Yes | Password used for account authentication | No |
        | class_id | String | Yes | ID reference of the year in which the student is in. | No |
        | institution_id | String | If institution is not passed | ID reference of the institute in which the student is enrolled. | No |
        | institution | String | If institution_id is not passed | Name of the institute in which the student is enrolled. | No |
        | city_id | String | If institution_id is not passed | The ID of the city in which the institute of enrollment is located. | No |
        | city | String | If city_id is not passed | The name of the city in which the institute of enrollment is located. | No |
        | teacher_email | String | No | Name of the teacher that relates to the created student. | Empty string |
        | gender | String | Yes | The gender of the new student | Yes |
        | phone_number | String | No | Mobile number of the new student | Empty string |
        - **✅ Response 200**
            
            ```python
            {
              "__class__": "Student",
              "city": null,
              "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
              "created_at": "2024-05-09T19:04:56.000000",
              "email": "hicham@gmail.com",
              "first_name": "student_2",
              "gender": "M",
              "id": "0f2a5390-d304-4be8-b1a8-9ca03d22a342",
              "institution": null,
              "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
              "last_name": "hicham",
              "phone_number": null,
              "teacher_email": "red1@gmail.com",
              "updated_at": "2024-05-09T19:05:32.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Missing Email**
            
            ```python
            {
            	"error": "Missing email"
            }
            ```
            
        - **✅ Response 700 - Already A Student**
            
            ```python
            {
            	"error": "student exists"
            }
            ```
            
        - **✅ Response 409 - Email Used Before**
            
            ```python
            {
            	"error": "{email} is already registered as a teacher"
            }
            ```
            
        - **✅ Response 400 - Missing First Name**
            
            ```python
            {
            	"error": "Missing first_name"
            }
            ```
            
        - **✅ Response 400 - Missing Last Name**
            
            ```python
            {
            	"error": "Missing last_name"
            }
            ```
            
        - **✅ Response 400 - Missing Password**
            
            ```python
            {
            	"error": "Missing password"
            }
            ```
            
        - **✅ Response 400 - Missing Class ID**
            
            ```python
            {
            	"error": "Missing class_id"
            }
            ```
            
        - **✅ Response 400 - Fake institute ID**
            
            ```python
            {
            	"error": "UNKNOWN INSTITUTION"
            }
            ```
            
        - **✅ Response 400 - Missing ID And Relating Information About Institute**
            
            ```python
            {
            	"error": "Provide 'institution' name with 'city' name or 'city_id', or you can provide the 'institution_id"
            }
            ```
            
    - `**[POST]` Create A Teacher**
        
        
        | Description | Adds a teacher to the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/teachers |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | None | None | None | None | None |
        | body params |  |  |  |  |
        | email | String | Yes | Email of the new teacher. | No |
        | first_name | String | Yes | The first name of the new teacher. | No |
        | last_name | String | Yes | The last name of the new teacher. | No |
        | password | String | Yes | Password used for account authentication | No |
        | institution_id | String | If institution is not passed | ID reference of the institute in which the teacher is working in. | No |
        | institution | String | If institution_id is not passed | Name of the institute in which the teacher is working. | No |
        | city_id | String | If institution_id is not passed | The ID of the city in which the institute of employment is located. | No |
        | city | String | If city_id is not passed | The name of the city in which the institute of employment is located. | No |
        | phone_number | String | No | Mobile number of the new teacher. | Empty string |
        | gender | String | Yes | The gender of the new student | Yes |
        | main_subject | String  | No | Name of the subject to be taught by the teacher. | Empty string |
        - **✅ Response 200**
            
            ```python
            {
              "__class__": "Teacher",
              "city": "Sidi Kacem",
              "created_at": "2024-05-09T19:04:44.000000",
              "email": "red2@gmail.com",
              "first_name": "DRIHMIA",
              "gender": "M",
              "id": "4cb13c99-da57-4e31-af15-341ab83df3e4",
              "institution": "LYCEE OUHOUD",
              "last_name": "Redouane",
              "main_subject": null,
              "phone_number": "+2126123456452",
              "updated_at": "2024-05-09T19:05:30.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Missing Email**
            
            ```python
            {
            	"error": "Missing email"
            }
            ```
            
        - **✅ Response 700 - Already A Teacher**
            
            ```python
            {
            	"error": "Teacher exists"
            }
            ```
            
        - **✅ Response 409 - Email Used Before**
            
            ```python
            {
            	"error": "{email} is already registered as a teacher"
            }
            ```
            
        - **✅ Response 400 - Missing Password**
            
            ```python
            {
            	"error": "Missing password"
            }
            ```
            
        - **✅ Response 400 - Fake institute ID**
            
            ```python
            {
            	"error": "UNKNOWN INSTITUTION"
            }
            ```
            
        - **✅ Response 400 - Missing ID And Relating Information About Institute**
            
            ```python
            {
            	"error": "Provide 'institution' name with 'city' name or 'city_id', or you can provide the 'institution_id"
            }
            ```
            
    - `**[POST]` Create A Lesson**
        
        
        | Description | Adds a lesson to the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/lessons |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | None | None | None | None | None |
        | body params |  |  |  |  |
        | name | String | Yes | Name of the new lesson. | Empty string |
        | download_link | String | Yes | URL to download the lesson from. | Empty string |
        | subject_id | String | Yes | ID of the subject that the lesson belongs to | No |
        | teacher_id | String | Yes | ID of the teacher that the subject is taught by. | No |
        | institutions_id | String | Yes | ID of the Institute that the subject is taught in. | No |
        | description | String | No | Some sentences to describe the lesson created | Empty string |
        | class_id | String | No | The ID of the year in which this lesson is taught. | No |
        - **✅ Response 200**
            
            ```python
            {
              "__class__": "Institution",
              "city": "Rabat",
              "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
              "created_at": "2024-05-05T17:38:37.000000",
              "id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
              "name": "GROUPE SCOLAIRE PRIVE LES QUATRE TEMPS",
              "updated_at": "2024-05-05T17:38:37.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Missing Name**
            
            ```python
            {
            	"error": "Missing name"
            }
            ```
            
        - **✅ Response 400 - Missing Download Link**
            
            ```python
            {
            	"error": "Missing download_link"
            }
            ```
            
        - **✅ Response 400 - Missing Subject ID**
            
            ```python
            {
            	"error": "Missing subject_id"
            }
            ```
            
        - **✅ Response 400 - Missing Teacher ID**
            
            ```python
            {
            	"error": "Missing teacher_id"
            }
            ```
            
        - **✅ Response 403 - Fake Teacher ID**
            
            ```python
            {
            	"error": "UNKOWN TEACHER"
            }
            ```
            
        - **✅ Response 400 - Subject Not Taught By This Teacher**
            
            ```python
            {
            	"error": "The subject is outside your area of expertise"
            }
            ```
            
        - **✅ Response 400 - Institute ID Passed**
            
            ```python
            {
            	"error": "institutions_id is being ignored for MVP"
            }
            ```
            
        - **✅ Response 400 - ِAlready A Lesson**
            
            ```python
            {
            	"error": "lesson exists"
            }
            ```
            
- [PUT]
    - `**[PUT]` Change State’s Information**
        
        
        | Description | Edit specific information about a state |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/states/6e381577-72ad-43f9-a3c9-a0e89f3d2cee |
        | Auth Required | Yes |
        
        | Parameter | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | URL params |  |  |  |  |
        | ID | String | Yes | ID to reference the city we wish to edit the information of. | No |
        | body params |  |  |  |  |
        | name | String | No | The new name of the state. | Empty string |
        - **✅ Response 200**
            
            ```python
            {
                "__class__": "State",
                "created_at": "2024-05-05T17:11:16.000000",
                "id": "3935d757-3495-4123-be14-a853f8903193",
                "name": "Casablanca-Settat",
                "updated_at": "2024-05-05T17:11:16.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 400 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Fake State ID**
            
            ```python
            {
            	"error": "UNKNOWN STATE"
            }
            ```
            
    - `**[PUT]` Change City’s Information**
        
        
        | Description | Edit specific information about a city |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/cities/bde27a09-8696-4e4d-a758-9949839a75b9 |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | ID to reference the city we wish to edit the information of. | No |
        | body params |  |  |  |  |
        | name | String | Yes | The new name of the city. | Empty string |
        - **✅ Response 200**
            
            ```python
            {
                "__class__": "City",
                "created_at": "2024-05-05T17:10:27.000000",
                "id": "002d32c6-1f48-4e06-bfee-ac63868a7250",
                "name": "Selouane",
                "state_id": "605ec99e-7ae8-4b7f-8b89-79c01a52d4db",
                "updated_at": "2024-05-05T17:10:27.000000"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - No Data**
            
            ```python
            {
            	"error": "No JSON"
            }
            ```
            
        - **✅ Response 400 - Fake City ID**
            
            ```python
            {
            		"error": "UNKOWN CITY"
            }
            ```
            
    - `**[PUT]` Change Institution’s Information**
        
        
        | Description | Edit specific information about an institute |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/institutions/cfddfd7f-c1ff-4c7d-89b4-9db1f5efdad5 |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | ID to reference the institute we wish to edit the information of. | No |
        | body params |  |  |  |  |
        | name | String | No | The new name of the city. | Empty string |
        | city_id | String | No | The ID reference of the city in which the institute is located. | No |
        | city | String | If city_id is not passed | The name of the city in which the institute is located. | No |
        - **✅ Response 200**
            
            ```python
            {
                "__class__": "Institution",
                "city": "Rabat",
                "city_id": "f6c022b1-6876-4e16-854f-dee8c21876bf",
                "created_at": "2024-05-05T17:38:37.000000",
                "id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
                "name": "GROUPE SCOLAIRE PRIVE LES QUATRE TEMPS",
                "updated_at": "2024-05-05T17:38:37.000000"
              }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Fake Institute ID**
            
            ```python
            {
            	"error": "UNKNOWN INSTITUTION"
            }
            ```
            
    - `**[PUT]` Change Teacher’s Information**
        
        
        | Description | Edit specific information about a teacher |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/teachers/27f396cd-50f6-4692-87a7-9e79c7fa42fb |
        | Auth Required | Yes |
        
        | Parameter | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | URL params |  |  |  |  |
        | ID | String | Yes | ID to reference the teacher we wish to edit the information of. | No |
        | body params |  |  |  |  |
        | first_name | String | No | The new first name of the teacher. | Empty string |
        | last_name | String | No | The new last name of the teacher. | Empty string |
        | password | String | No | The new password that is used for account authentication. | No |
        | institutions | String | No | institute that the teacher is employed in. | No |
        | subject | String | No | The subjects that the teacher teaches. | No |
        | city | String | No | City of residence for the teacher. | Noclasses. |
        | classes | String | No | The classes that the teacher teaches in. | No |
        - **✅ Response 200**
            
            ```python
            
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Fake Teacher ID**
            
            ```python
            {
            	"error": "UNKNOWN TEACHER"
            }
            ```
            
    - `**[PUT]` Change Student’s Information**
        
        
        | Description | Edit specific information about a student |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/students/9aae4684-7f9c-4066-8592-9e4a440d097f |
        | Auth Required | Yes |
        
        | Parameter | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | URL params |  |  |  |  |
        | ID | String | Yes | ID to reference the city we wish to edit the information of. | No |
        | body params |  |  |  |  |
        | first_name | String | No | The new first name of the student. | Empty string |
        | last_name | String | No | The new last name of the student. | Empty string |
        | password | String | No | The new password that is used for account authentication. | No |
        | teachers_email | String | No | email of the teacher that the student is taught by. | No |
        - **✅ Response 200**
            
            ```python
            
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Fake Student ID**
            
            ```python
            {
            	"error": "UNKNOWN STUDENT"
            }
            ```
            
        - **✅ Response 400 - Fake Teacher ID**
            
            ```python
            {
            	"error": "UNKNOWN TEACHER with {teacher_email}"
            }
            ```
            
    - `**[PUT]` Change Lessons’s Information**
        
        
        | Description | Edit specific information about a lesson |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/lessons/084b5a7a-2099-4457-b2ab-9e9eb1f33fdb |
        | Auth Required | Yes |
        
        | Parameter | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | URL params |  |  |  |  |
        | ID | String | Yes | ID to reference the city we wish to edit the information of. | No |
        | body params |  |  |  |  |
        | name | String | No | The new name of the lesson. | Empty string |
        | download_link | String | No | The new link to download the lesson from | No |
        | description | String | No | Some sentences to tell what the lesson is about | Empty string |
        | public | String | No | A boolen value to decide whether a lesson is available to the public or not. | True |
        - **✅ Response 200**
            
            ```python
            {
            "userId": 1,
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
            }
            ```
            
        - **✅ Response 400 - Bad Data**
            
            ```python
            {
            	"error": "Not a JSON"
            }
            ```
            
        - **✅ Response 422 - Missing Data**
            
            ```python
            {
            	"error": "No data"
            }
            ```
            
        - **✅ Response 400 - Fake Lesson ID**
            
            ```python
            {
            	"error": "UNKNOWN LESSON"
            }
            ```
            
    
- [DELETE]
    - `**[DELETE]` Remove A State**
        
        
        | Description | Deletes a state from the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/states/{ID} |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | Reference tag for the state we wish to delete. | No |
        - **✅ Response 200**
            
            ```python
            {}
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN STATE"}
            ```
            
    - `**[DELETE]` Remove A City**
        
        
        | Description | Deletes a city from the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/cities/{ID} |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | Reference tag for the city we wish to delete. | No |
        - **✅ Response 200**
            
            ```python
            {}
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN CITY"}
            ```
            
    - `**[DELETE]` Remove An Institution**
        
        
        | Description | Deletes an institute from the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/institutions/{ID} |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | Reference tag for the institute we wish to delete. | No |
        - **✅ Response 200**
            
            ```python
            {}
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN INSTITUTE"}
            ```
            
    - `**[DELETE]` Remove A Teacher**
        
        
        | Description | Deletes a teacher from the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/teachers/{ID} |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | Reference tag for the teacher we wish to delete. | No |
        - **✅ Response 200**
            
            ```python
            {}
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN TERACHER"}
            ```
            
    - `**[DELETE]` Remove A Student**
        
        
        | Description | Deletes a student from the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/students/{ID} |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | Reference tag for the student we wish to delete. | No |
        - **✅ Response 200**
            
            ```python
            {}
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN STUDENT"}
            ```
            
    - `**[DELETE]` Remove A Lesson**
        
        
        | Description | Deletes a lesson from the database |
        | --- | --- |
        | URL | http://web-01.drihmia.tech/api/v1/lessons/{ID} |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description | Default |
        | --- | --- | --- | --- | --- |
        | url params |  |  |  |  |
        | ID | String | Yes | Reference tag for the lesson we wish to delete. | No |
        - **✅ Response 200**
            
            ```python
            {}
            ```
            
        - **✅ Response 404**
            
            ```python
            {"error": "UNKNOWN LESSON"}
            ```
