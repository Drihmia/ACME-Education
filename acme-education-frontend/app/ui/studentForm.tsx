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
  classProps, 
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
  const [classesData, setClassesData] = useState<classProps[]>(
    []
  );
  const [classes, setClasses] = useState<any[]>([]);
  const [teachers, setTeachers] = useState<any[]>([]);

  const [selectedCity, setCity] = useState<selectedCityProps>({
    status: false,
    id: "",
  });
  const [selectedInstitute, setInstitute] = useState<selectedCityProps>({
    status: false,
    id: "",
  });

  useEffect(() => {
    if (selectedCity.id != "") {
      fetch(
        `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/cities/${selectedCity.id}/institutions`
      )
        .then((res) => res.json())
        .then((data) => {
          setInstitutionsData(data);
        });
    } else {
      setInstitutionsData([]);
    }
  }, [selectedCity]);

  useEffect(() => {
    (async () => {
      if (selectedInstitute.id != "") {
        const fetchSchoolClasses = fetch(
          `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/institutions/${selectedInstitute.id}/classes`
        ).then((res) => res.json());
        const fetchSchoolTeachers = fetch(
          `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/institutions/${selectedInstitute.id}/teachers`
        ).then((res) => res.json());

        const [schoolClasses, schoolTeachers] = await Promise.all([
          fetchSchoolClasses,
          fetchSchoolTeachers,
        ]);
        setClasses(schoolClasses);
        setTeachers(schoolTeachers);
      } else {
        setClasses([]);
        setTeachers([]);
      }
    })();
  }, [selectedInstitute]);

  const checkValue = (value: string) => {
    if (value === "city") {
      return (status: boolean, id?: string) => {
        if (status) {
          setCity({ status: true, id: id! });
        } else {
          setCity({ status: false, id: "" });
        }
      };
    } else {
      return (status: boolean, id?: string) => {
        if (status) {
          setInstitute({ status: true, id: id! });
        } else {
          setInstitute({ status: false, id: "" });
        }
      };
    }
  };

  const { data: citiesData } = useSWR(
    `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/cities`,
    fetcher
  );

  if (!citiesData) return <LoadingSkeleton />;

  const submitForm = async (values: studentSignupProps) => {
    const city = citiesData?.find(
      (item: cityProps) => item.name == values.city
    );
    if (city) values.city_id = city.id;

    const institution = institutionsData?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;


    const clas = classes?.find((item: any) => item.name == values.class);
    if (clas) values.class_id = clas.id;

    if (action === "update") {
      delete values.password
      delete values.confirm_password
    }

    // For getting the CSRF cookies for POST, PUT or DELETE requests
    function getCookie(name: string): string | undefined {
      let value = '';
      if (typeof document !== 'undefined') {
        value = `; ${document.cookie}`;
      }
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) {
        const part = parts.pop();
        if (part) {
          return part.split(';').shift();
        }
        return "1233"
      }
    }
    const csrfToken = getCookie('csrf_access_token');

    const headers: HeadersInit = {
      "Content-Type": "application/json",
    };

    if (csrfToken) {
      headers['X-CSRF-TOKEN'] = csrfToken;
    }
    try {


      const response = await fetch(
        `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/${
          action == "update" ? "students/" + profile.id : "students/"
        }`,
        {
          method: action == "signup" ? "POST" : "PUT",
          body: JSON.stringify(values),
          headers: headers,
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
            mutate(`https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/students/${profile.id}`);
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
            gender: action == "update" ? profile.gender : "",
            class: action == "update" ? profile.class.name : "",
            teacher_email: action == "update" ? profile.teacher_email : "",
            is_teacher: action == "signup" ? false: false,
          }}
          validationSchema={
            action === "update" ? updateStudentSchema : signupStudentSchema
          }
          onSubmit={(values, { setSubmitting }) => {
            submitForm(values);
            setSubmitting(false);
          }}
        >
          {({ values }) => {
            return (
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
                  disabled={profile ? true : false}
                />
                <MyTextInput
                  label="Phone Number"
                  name="phone_number"
                  type="string"
                  placeholder="+212637890987"
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
                  data={citiesData}
                  checkValue={checkValue("city")}
                  type="text"
                  placeholder="e.g Sale"
                  disabled={profile ? true : false}
                />
                <MyTextAndSelectInput
                  label="Name of Institution"
                  name="institution"
                  data={institutionsData}
                  checkValue={checkValue("institute")}
                  type="text"
                  disabled={action === "signup" ? !selectedCity.status : true}
                  placeholder="e.g Lycee Qualifiant ALMANDAR ALJAMIL"
                />
                <MyTextAndSelectInput
                  label="Class"
                  name="class"
                  data={classes}
                  type="text"
                  placeholder="Tronc commun (French)"
                  disabled={
                    action === "signup" ? !selectedInstitute.status : true
                  }
                />
                <MyTextAndSelectInput
                  label="Teacher"
                  name="teacher_email"
                  type="email"
                  data={teachers}
                  placeholder="teacher@example.com"
                  disabled={
                    action === "signup" ? !selectedInstitute.status : true
                  }
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
                      checked: values.gender === "M" ? true : false,
                    },
                    {
                      name: "gender",
                      label: "Female",
                      value: "F",
                      type: "radio",
                      checked: values.gender === "F" ? true : false,
                    },
                  ]}
                />
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
            );
          }}
        </Formik>
      </div>
      {isModal && action === "signup" && (
        <SignUpModal closeModal={closeModal} response={response} />
      )}
    </>
  );
};
