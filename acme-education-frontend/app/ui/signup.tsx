"use client";

import { FieldSet, MyTextInput } from "./form";
import { Formik, Form } from "formik";
import { signupSchema } from "../validation/auth";

const SignUpForm = () => {
  return (
    <>
      <div className="w-full flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl shadow-xl">
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
            firstName: "",
            lastName: "",
            email: "",
            telephone: "",
            password: "",
            confirmPassword: "",
            isTeacher: "",
          }}
          validationSchema={signupSchema}
          onSubmit={(values, { setSubmitting }) => {
            setTimeout(() => {
              alert(JSON.stringify(values, null, 2));
              setSubmitting(false);
            }, 400);
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
              name="firstName"
              type="text"
              placeholder="John"
            />
            <MyTextInput
              label="Last Name"
              name="lastName"
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
              name="confirmPassword"
              type="password"
              placeholder=""
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
              className="w-40 py-2 mt-8 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-3xl"
            >
              sign up
            </button>
          </Form>
        </Formik>
      </div>
    </>
  );
};

export default SignUpForm;
