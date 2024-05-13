"use client";

import React from 'react'
import useSWR, { mutate } from "swr";
import { FieldSet, MyTextAndSelectInput, MyTextInput } from "./form";
import { Formik, Form } from "formik";
import { signupTeacherSchema, updateTeacherSchema } from "../validation/schema";
import { useEffect, useState } from "react";
import { SignUpModal } from "./signupModal";
import { fetcher } from "../lib/fetch";
import { cityProps, institutionProps, responseProps, selectedCityProps, teacherSignupProps } from "../types";
import { Icon } from "@iconify/react/dist/iconify.js";
import { LoadingSkeleton } from './skeletons';

export const TeacherForm = ({
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

  const [institutions, setInstitutions] = useState<institutionProps[]>(
    []
  );
  const [subjects, setSubjects] = useState<any[]>([])

  const [teacherClasses, setTeacherClasses] = useState<any[]>([])

  const [selectedCity, setCity] = useState<selectedCityProps>({
    status: false,
    id: "",
  });

  useEffect(() => {
    fetch(`http://${process.env.NEXT_API_ADDRESS}/api/v1/subjects`).then(res => res.json()).then(data => setSubjects(data))
  }, [])
  
  useEffect(() => {
    if (selectedCity.id != "") {
      fetch(
        `http://${process.env.NEXT_API_ADDRESS}/api/v1/cities/${selectedCity.id}/institutions`
      )
        .then((res) => res.json())
        .then((data) => setInstitutions(data));
    } else {
      setInstitutions([]);
    }
  }, [selectedCity]);

  const checkValue = (status: boolean, id?: string) => {
    if (status) {
      setCity({ status: true, id: id! });
    } else {
      setCity({ status: false, id: "" });
    }
  };

  const { data: cities } = useSWR(
    `http://${process.env.NEXT_API_ADDRESS}/api/v1/cities`,
    fetcher
  );
  const { data: classes } = useSWR(
    `http://${process.env.NEXT_API_ADDRESS}/api/v1/classes`,
    fetcher
  );

  useEffect(() => {
    if (profile) {
      fetch(`http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${profile.id}/classes`).then(res => res.json()).then(data => setTeacherClasses(data))
    }
  }, [])

  const submitForm = async (values: teacherSignupProps) => {
    const city = cities?.find(
      (item: cityProps) => item.name == values.city
    );
    if (city) values.city_id = city.id;

    const institution = institutions?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;

    console.log(values);

    try {
      const response = await fetch(
        `http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${action == "update" ? profile.id : ""}`,
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
          if (profile) {
            mutate(`http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${profile.id}`);
            mutate(`http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${profile.id}/subjects`);
            mutate(`http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${profile.id}/classes`);
            mutate(`http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${profile.id}/institutions`);
          }
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

  if (!cities || (action === 'update' && (!classes || !teacherClasses))) return <LoadingSkeleton />
  
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
            phone_number:
              action == "update"
                ? profile.phone_number
                : "",
            password: "",
            confirm_password: "",
            institution: action == "update" ? profile.institution : "",
            city: action == "update" ? profile.city : "",
            gender: action == "update" ? profile.gender : "",
            subjects: action == "update" ? profile.subjects.map((sub: any) => sub.id) : [],
            classes: action == "update" ? profile.classes.map((cls: any) => cls.id) : [],
            institutions: action == "update" ? profile.institutions.map((ins: any) => ins.id) : [],
          }}
          validationSchema={action === "update" ? updateTeacherSchema : signupTeacherSchema}
          onSubmit={(values, { setSubmitting }) => {
            submitForm(values);
            setSubmitting(false);
          }}
        >
          {({ values }) => {
            return (
              (
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
                {action === "signup" && (
                  <>
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
                <MyTextAndSelectInput
                  label="City"
                  name="city"
                  data={cities}
                  checkValue={checkValue}
                  type="text"
                  placeholder="e.g MarsCity"
                  disabled={profile ? true : false}
                />
                <MyTextAndSelectInput
                  label="Name of Institution"
                  name="institution"
                  data={institutions}
                  type="text"
                  disabled={!selectedCity.status}
                  placeholder="e.g Insitute of Science and Technology"
                />
                <FieldSet
                    label="Gender"
                    name="gender"
                    options={[
                      {
                        name: "gender",
                        label: "Male",
                        value: "M",
                        type: "radio",
                        checked: values.gender === "M" ? true : false
                      },
                      {
                        name: "gender",
                        label: "Female",
                        value: "F",
                        type: "radio",
                        checked: values.gender === "F" ? true : false
                      },
                    ]}
                  />
                {action === "update" && subjects && (
                  <>
                  <FieldSet
                    label="Subjects"
                    name="subjects_id"
                    customStyle="col-span-full"
                    options={subjects.map((sub: any) => {
                      const newSub = { ...sub };
                      newSub.label = sub.name;
                      newSub.name = "subjects_id";
                      newSub.value = sub.id;
                      newSub.type = "checkbox";
                      newSub.checked = values.subjects.includes(sub.id) ? true : false;
                      return newSub;
                    })}
                  />
                  <FieldSet
                    label="Classes"
                    name="classes_id"
                    customStyle="col-span-full"
                    options={classes.map((cls: any) => {
                      const newSub = { ...cls };
                      newSub.label = cls.name;
                      newSub.name = "classes_id";
                      newSub.value = cls.id;
                      newSub.type = "checkbox";
                      newSub.checked = values.classes.includes(cls.id) ? true : false;
                      return newSub;
                    })}
                  />
                  <FieldSet
                    label="Institutions"
                    name="institutions_id"
                    customStyle="col-span-full h-96 overflow-y-scroll"
                    options={institutions.map((ins: any) => {
                      const newSub = { ...ins };
                      newSub.label = ins.name;
                      newSub.name = "institutions_id";
                      newSub.value = ins.id;
                      newSub.type = "checkbox";
                      newSub.checked = values.institutions.includes(ins.id) ? true : false;
                      return newSub;
                    })}
                  />
                  </>
                )}
                <div className="flex items-center gap-4 justify-center md:col-span-full">
                  <button
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
              )
            )
          }}
        </Formik>
      </div>
      {isModal && action === "signup" && (
        <SignUpModal closeModal={closeModal} response={response} />
      )}
    </>
  );
};
