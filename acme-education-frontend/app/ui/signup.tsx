"use client";

import useSWR from "swr";
import { FieldSet, MyTextAndSelectInput, MyTextInput } from "./form";
import { Formik, Form } from "formik";
import { signupSchema } from "../validation/auth";
import { useEffect, useState } from "react";
import { SignUpModal } from "./signupModal";
import { fetcher } from "../lib/fetch";
import { cityProps, institutionProps } from "../types";

interface signupProps {
  first_name: string;
  last_name: string;
  email: string;
  telephone: string;
  password: string;
  confirm_password: string;
  isTeacher: string;
  city: string;
  city_id?: string;
  institution: string;
  institution_id?: string;
}

interface responseProps {
  status: string;
  message: string;
}

interface selectedCityProps {
  status: boolean;
  id: string;
}

export const SignUpForm = () => {
  const [response, setResponse] = useState<responseProps>({
    status: "",
    message: "",
  });
  const [isModal, setModal] = useState(false);
  const closeModal = () => setModal(false);

  const [institutionsData, setInstitutionsData] = useState<institutionProps[]>([])

  const [selectedCity, setCity] = useState<selectedCityProps>({status: false, id: ""})

  useEffect(() => {
    if (selectedCity.id != "") {
      fetch(`http://127.0.0.1:5000/api/v1/cities/${selectedCity.id}/institutions`).then(res => res.json()).then(data => setInstitutionsData(data))
    } else {
      setInstitutionsData([])
    }
    }, [selectedCity])

  const checkValue = (status: boolean, id?: string) => {
    
    if (status) {
      setCity({status: true, id: id!})
    } else {
      setCity({status: false, id: ""})
    }
  }

  const { data: citiesData } = useSWR(
    "http://127.0.0.1:5000/api/v1/cities",
    fetcher
  );

  // const { data: institutionsData } = useSWR(
  //   `http://127.0.0.1:5000/api/v1/cities/${selectedCity.id}/institutions`,
  //   fetcher
  // );

  // change later - done
  if (institutionsData) console.log(institutionsData);

  const submitForm = async (values: signupProps) => {
    const city = citiesData?.find(
      (item: cityProps) => item.name == values.city
    );
    if (city) values.city_id = city.id;

    const institution = institutionsData?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;

    console.log(values);

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/v1/${
          values.isTeacher == "true" ? "teachers" : "students"
        }`,
        {
          method: "POST",
          body: JSON.stringify(values),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const res_data = await response.json();

      setResponse({
        status: response.status == 201 ? "success" : "error",
        message: response.status == 201 ? "OK" : res_data.error,
      });
    } catch (e) {
      let errorMessage = "Something went wrong. Try again later.";
      if (e instanceof Error) {
        errorMessage = e.message;
      }
      setResponse({ status: "error", message: errorMessage });
    } finally {
      setModal(true);
    }
  };

  return (
    <>
      <div className="w-full max-w-xl flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl shadow-xl">
        <div className="w-full text-center">
          <h2 className="font-semibold text-3xl md:text-4xl capitalize mb-2 md:mb-4">
            Sign Up
          </h2>
          <p className="max-w-sm mx-auto">
            Join millions of institutions, teachers and students using ACME
            Education
          </p>
        </div>
        <Formik
          initialValues={{
            first_name: "",
            last_name: "",
            email: "",
            telephone: "",
            password: "",
            confirm_password: "",
            institution: "",
            city: "",
            isTeacher: "false",
          }}
          validationSchema={signupSchema}
          onSubmit={(values, { setSubmitting }) => {
            submitForm(values);
            setSubmitting(false);
          }}
        >
          <Form className="w-full flex flex-col items-center p-4 md:p-8 lg:px-16">
            <MyTextInput
              label="Email Address"
              name="email"
              type="email"
              placeholder="you@example.com"
            />
            <MyTextInput
              label="First Name"
              name="first_name"
              type="text"
              placeholder="John"
            />
            <MyTextInput
              label="Last Name"
              name="last_name"
              type="text"
              placeholder="Doe"
            />
            <MyTextInput
              label="Phone Number"
              name="telephone"
              type="number"
              placeholder="+233 404 500 2001"
            />
            <MyTextInput
              label="Password"
              name="password"
              type="password"
              placeholder=""
            />
            <MyTextInput
              label="Confirm Password"
              name="confirm_password"
              type="password"
              placeholder=""
            />
            <MyTextAndSelectInput
              label="City"
              name="city"
              data={citiesData}
              checkValue={checkValue}
              type="text"
              placeholder="e.g MarsCity"
            />
            <MyTextAndSelectInput
              label="Name of Institution"
              name="institution"
              data={institutionsData}
              type="text"
              disabled={!selectedCity.status}
              placeholder="e.g Insitute of Science and Technology"
            />
            <FieldSet
              label="Are you a Teacher or a Student?"
              name="isTeacher"
              options={[
                { name: "isTeacher", label: "Teacher", value: true },
                { name: "isTeacher", label: "Student", value: false },
              ]}
            />
            <button
              type="submit"
              className="w-40 py-2 mt-8 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-xl"
            >
              sign up
            </button>
          </Form>
        </Formik>
      </div>
      {isModal && <SignUpModal closeModal={closeModal} response={response} />}
    </>
  );
};
