"use client";

import React from "react";
import useSWR, { mutate } from "swr";
import { FieldSet, MyTextAndSelectInput, MyTextInput } from "./form";
import { Formik, Form } from "formik";
import { signupStudentSchema, updateStudentSchema } from "../validation/schema";
import { useEffect, useState } from "react";
import { SignUpModal } from "./signupModal";
import { fetcher } from "../lib/fetch";
import {
  cityProps,
  institutionProps,
  responseProps,
  selectedCityProps,
  studentSignupProps,
} from "../types";
import { Icon } from "@iconify/react/dist/iconify.js";
import { LoadingSkeleton } from "./skeletons";

export const StudentForm = ({
  action,
  profile,
  close,
}: {
  action: string;
  profile?: any;
  close?: () => void;
}) => {
  const [response, setResponse] = useState<responseProps>({
    status: "",
    message: "",
  });
  const [isModal, setModal] = useState(false);
  const closeModal = () => setModal(false);

  const [institutionsData, setInstitutionsData] = useState<institutionProps[]>(
    []
  );

  const [selectedCity, setCity] = useState<selectedCityProps>({
    status: false,
    id: "",
  });

  useEffect(() => {
    if (selectedCity.id != "") {
      fetch(
        `http://127.0.0.1:5000/api/v1/cities/${selectedCity.id}/institutions`
      )
        .then((res) => res.json())
        .then((data) => setInstitutionsData(data));
    } else {
      setInstitutionsData([]);
    }
  }, [selectedCity]);

  const checkValue = (status: boolean, id?: string) => {
    if (status) {
      setCity({ status: true, id: id! });
    } else {
      setCity({ status: false, id: "" });
    }
  };

  const { data: citiesData } = useSWR(
    "http://127.0.0.1:5000/api/v1/cities",
    fetcher
  );

  if (!citiesData) return <LoadingSkeleton />;

  const submitForm = async (values: studentSignupProps) => {
    console.log("clicked");
    const city = citiesData?.find(
      (item: cityProps) => item.name == values.city
    );
    if (city) values.city_id = city.id;

    const institution = institutionsData?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/v1/students/${
          action == "update" ? profile.id : ""
        }`,
        {
          method: action == "signup" ? "POST" : "PUT",
          body: JSON.stringify(values),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const res_data = await response.json();

      if (res_data["error"]) {
        setResponse({ status: "error", message: res_data["error"] });
        alert(res_data["error"]);
      } else {
        setResponse({ status: "success", message: "OK" });
        if (action == "update") {
          alert("Profile updated");
          if (close) {
            close();
          }
          if (profile)
            mutate(`http://127.0.0.1:5000/api/v1/students/${profile.id}`);
        }
      }
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
      <div
        className={`w-full ${
          action === "signup" ? "max-w-3xl shadow-xl" : ""
        } flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl`}
      >
        <div className="w-full text-center">
          {action === "signup" ? (
            <>
              <h2 className="font-semibold text-3xl md:text-4xl capitalize mb-2 md:mb-4">
                Sign Up
              </h2>
              <p className="max-w-sm mx-auto">
                Join millions of institutions, teachers and students using ACME
                Education
              </p>
            </>
          ) : (
            <h2 className="font-semibold text-3xl md:text-4xl capitalize mb-2 md:mb-4">
              Update profile
            </h2>
          )}
        </div>
        <Formik
          initialValues={{
            first_name: action == "update" ? profile.first_name : "",
            last_name: action == "update" ? profile.last_name : "",
            email: action == "update" ? profile.email : "",
            phone_number: action == "update" ? profile.phone_number : "",
            password: "",
            confirm_password: "",
            institution: action == "update" ? profile.institution : "",
            city: action == "update" ? profile.city : "",
            gender: "",
            class_id: action == "update" ? profile.class_id : "",
            teacher_email: "",
          }}
          validationSchema={
            action === "update" ? updateStudentSchema : signupStudentSchema
          }
          onSubmit={(values, { setSubmitting }) => {
            console.log("submitting values");
            
            submitForm(values);
            setSubmitting(false);
          }}
        >
          <Form className="w-full flex flex-col md:grid md:grid-cols-2 md:gap-4 lg:gap-6 items-center p-4 md:p-8 lg:px-16">
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
              label="Email Address"
              name="email"
              type="email"
              placeholder="you@example.com"
            />
            <MyTextInput
              label="Phone Number"
              name="phone_number"
              type="number"
              placeholder="+2334045002001"
            />
            <MyTextInput
              label="Class ID"
              name="class_id"
              type="text"
              placeholder=""
              disabled={profile ? true : false}
            />
            <MyTextAndSelectInput
              label="City"
              name="city"
              data={citiesData}
              checkValue={checkValue}
              type="text"
              placeholder="e.g MarsCity"
              disabled={profile ? true : false}
            />
            <MyTextAndSelectInput
              label="Name of Institution"
              name="institution"
              data={institutionsData}
              type="text"
              disabled={!selectedCity.status}
              placeholder="e.g Insitute of Science and Technology"
            />
            {action === "signup" && (
              <>
                <MyTextInput
                  label="Teacher's Email"
                  name="teacher_email"
                  type="email"
                  placeholder=""
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
              </>
            )}
            <FieldSet
                  label="Gender"
                  name="gender"
                  options={[
                    {
                      name: "gender",
                      label: "Male",
                      value: "M",
                      type: "radio",
                    },
                    {
                      name: "gender",
                      label: "Female",
                      value: "F",
                      type: "radio",
                    },
                  ]}
                />
            <div className="flex items-center gap-4 justify-center md:col-span-full">
              <button
              onClick={() => console.log('clicked')
              }
                type="submit"
                className="w-40 py-2 mt-8 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-xl"
              >
                {action === "signup" ? "sign up" : "update"}
              </button>
              {action === "update" && (
                <div
                  onClick={() => {
                    if (
                      confirm("Are you sure you want to go cancel?") &&
                      close
                    ) {
                      close();
                    }
                  }}
                  className="w-40 mt-8 flex items-center gap-1 justify-center p-2 bg-slate-200 hover:bg-black rounded-xl hover:text-white cursor-pointer"
                >
                  <Icon icon="pajamas:cancel" /> Cancel
                </div>
              )}
            </div>
          </Form>
        </Formik>
      </div>
      {isModal && action === "signup" && (
        <SignUpModal closeModal={closeModal} response={response} />
      )}
    </>
  );
};
