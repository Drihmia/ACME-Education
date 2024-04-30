"use client";

import React, { ClassAttributes, InputHTMLAttributes } from "react";
import { Formik, Form, useField, FieldHookConfig } from "formik";
import { signinSchema } from "../validation/auth";
import Link from "next/link";

interface OtherProps {
  label: string;
  placeholder: string;
}

export const MyTextInput = ({
  label,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLInputElement> &
  ClassAttributes<HTMLInputElement> &
  FieldHookConfig<string>) => {
  const [field, meta] = useField(props);
  return (
    <div className="w-full mb-4">
      <label
        className="relative w-full font-semibold text-black text-xs"
        htmlFor={props.id || props.name}
      >
        {label}
        <input
          className={`w-full p-2 md:px-4 md:py-3 tablet:mt-1 laptop:mt-2 font-normal text-base border ${
            meta.error ? "border-red-600" : "border-dark/25"
          } hover:border-dark/50 focus:border-dark/75 outline-none rounded-xl md:rounded-2xl`}
          {...field}
          {...props}
        />
      </label>
      {meta.touched && meta.error ? (
        <div className="error text-xs text-red-600">{meta.error}</div>
      ) : null}
    </div>
  );
};

export const MyTextArea = ({
  label,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLTextAreaElement> &
  ClassAttributes<HTMLTextAreaElement> &
  FieldHookConfig<string>) => {
  const [field, meta] = useField(props);
  return (
    <div className="mb-4">
      <label
        className="flex pb-2 font-semibold text-black text-xs"
        htmlFor={props.id || props.name}
      >
        {label}
      </label>
      <textarea
        className={`w-full h-40 p-4 text-base border ${
          meta.error ? "border-red-600" : "border-dark/25"
        } hover:border-dark/50 focus:border-dark/75 rounded-lg outline-none`}
        {...field}
        {...props}
      />
      {meta.touched && meta.error ? (
        <div className="error text-xs text-red-600">{meta.error}</div>
      ) : null}
    </div>
  );
};

export const MySelect = ({
  label,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLSelectElement> &
  ClassAttributes<HTMLSelectElement> &
  FieldHookConfig<string>) => {
  const [field, meta] = useField(props);
  return (
    <div className="mb-4">
      <label
        className="flex pb-2 font-medium text-xs"
        htmlFor={props.id || props.name}
      >
        {label}
      </label>
      <select
        className="w-full px-4 py-2 text-base border border-dark/25 rounded-3xl"
        {...field}
        {...props}
      />
      {meta.touched && meta.error ? (
        <div className="error text-xs text-red-600">{meta.error}</div>
      ) : null}
    </div>
  );
};

export const SignInForm = () => {
  return (
    <>
      <div className="w-full max-w-md flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl shadow-xl">
        <div className="w-full text-center">
          <h2 className="font-semibold text-4xl capitalize">Login</h2>
        </div>
        <Formik
          initialValues={{
            email: "",
            password: "",
          }}
          validationSchema={signinSchema}
          onSubmit={(values, { setSubmitting }) => {
            setTimeout(() => {
              alert(JSON.stringify(values, null, 2));
              setSubmitting(false);
            }, 400);
          }}
        >
          <Form className="w-full flex flex-col items-center p-4 md:p-8 lg:px-16">
            <MyTextInput
              label="Email"
              name="email"
              type="email"
              placeholder="you@example.com"
            />
            <MyTextInput
              label="Password"
              name="password"
              type="password"
              placeholder=""
            />
            <button
              type="submit"
              className="w-40 py-2 mt-4 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-2xl"
            >
              login
            </button>
          </Form>
        </Formik>
        <div className="w-full text-center lg:flex lg:items-center lg:justify-between lg:px-8">
          <Link href={`/signup`} className="block text-black/60 hover:text-blue-900 hover:underline text-sm">
            Don&apos;t have an account? Sign up
          </Link>
          <Link href={`forgotPassword`} className="block text-black/60 hover:text-blue-900 hover:underline text-sm">
            Forgot password?
          </Link>
        </div>
      </div>
    </>
  );
};
