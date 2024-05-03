"use client";

import React, { ClassAttributes, InputHTMLAttributes, useContext, useState } from "react";
import {
  Formik,
  Form,
  useField,
  FieldHookConfig
} from "formik";
import { signinSchema } from "../validation/auth";
import Link from "next/link";
import Cookies from 'js-cookie'
import { useOutsideClick } from "../lib/useOutsideClick";
import { User, cityProps, siginProps } from "../types";
import { useRouter } from "next/navigation";
import { authUserContext, useAuth } from "@/context/authContext";

interface radioProps {
  label: string;
  name: string;
  value: boolean;
}

interface OtherProps {
  label: string;
  placeholder?: string;
  options?: radioProps[];
  data?: cityProps[];
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
        className="relative w-full font-semibold text-black"
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
export const MyTextAndSelectInput = ({
  label,
  data,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLInputElement> &
  ClassAttributes<HTMLInputElement> &
  FieldHookConfig<string>) => {
  const [field, meta, helpers] = useField(props);
  const [filteredData, setData] = useState<cityProps[]>([]);
  const [focused, setFocus] = useState(false);

  const openFocus = () => setFocus(true);
  const closeFocus = () => setFocus(false);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;

    const searchRegex = new RegExp(value, "gi");

    const filter = data?.filter((res) => {
      if (searchRegex.test(res.name)) return res;
    }) as cityProps[];

    setData(filter);
  };

  const setValue = (value: string) => {
    helpers.setValue(value);
    closeFocus();
  };

  // useEffect(() => {
  //   console.log(field);
  // }, [field]);

  const ref = useOutsideClick(closeFocus);

  return (
    <div ref={ref} className="relative w-full mb-4 z-1">
      <label
        className="relative w-full font-semibold text-black"
        htmlFor={props.id || props.name}
      >
        {label}
        <input
          onFocus={openFocus}
          className={`w-full p-2 md:px-4 md:py-3 tablet:mt-1 laptop:mt-2 font-normal text-base border ${
            meta.error ? "border-red-600" : "border-dark/25"
          } hover:border-dark/50 focus:border-dark/75 outline-none rounded-xl md:rounded-2xl`}
          {...field}
          {...props}
          onChange={(e) => {
            field.onChange(e);
            handleChange(e);
          }}
        />
      </label>
      {meta.touched && meta.error ? (
        <div className="error text-xs text-red-600">{meta.error}</div>
      ) : null}
      {focused && filteredData.length > 0 && (
        <ul className="absolute w-full max-h-48 overflow-y-scroll top-full left-0 flex flex-col gap-1 p-1 md:p-2 bg-white rounded-md shadow-md z-10">
          {filteredData.map((city, i) => (
            <li
              className="w-full p-1 cursor-pointer hover:bg-blue-700 hover:text-white rounded"
              key={i}
              onClick={() => setValue(city.name)}
            >
              {city.name}
            </li>
          ))}
        </ul>
      )}
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
        className="flex pb-2 font-semibold text-black"
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
    <div className="w-full mb-4">
      <label
        className="w-full flex pb-2 font-medium"
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

//create your input component
//in this case im defining the radio input
//this component can be contained in another file
export const InputField = ({ label, name, value }: radioProps) => {
  return (
    <label htmlFor={name} className="block font-normal">
      <input type="radio" name={name} value={`${value}`} />
      {label}
    </label>
  );
};

// create a custom FieldSet component that uses the useField hook
//this component can be contained in another file
export const FieldSet = ({
  label,
  options,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLFieldSetElement> &
  ClassAttributes<HTMLFieldSetElement> &
  FieldHookConfig<string>) => {
  const [field, meta] = useField(props);
  return (
    <div className="w-full">
      <label className="w-full font-medium">
        {label}
        {/* make sure the radios are contained in a fieldset */}
        <fieldset {...field} {...props} className="w-full flex items-center gap-4">
          {options?.map((option, i) => (
            <InputField
              key={`${i}`}
              name={option.name}
              label={option.label}
              value={option.value}
            />
          ))}
        </fieldset>
      </label>
      {meta.touched && meta.error ? (
        <div className="error text-xs text-red-600">{meta.error}</div>
      ) : null}
    </div>
  );
};


export const SignInForm = () => {
  const { updateUser } = useAuth()!
  const [error, setError] = useState<string | null>()
  const router = useRouter();

  const submitForm = async (values: siginProps) => {

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/v1/${
          values.isTeacher == "true" ? "teacher_login" : "student_login"
        }`,
        {
          method: "POST",
          body: JSON.stringify(values),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const user: User = await response.json();
      if (user.access_token) {
        Cookies.set("currentUser", JSON.stringify(user))
        updateUser()
        router.push("/dashboard")
      }
      if (response.status != 200) setError("Invalid credentials");
    } catch (e) {
      let errorMessage = "Something went wrong. Try again later.";
      if (e instanceof Error) {
        errorMessage = e.message;
      }
      setError( errorMessage );
    } 
  };

  return (
    <>
      <div className="w-full max-w-md flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl shadow-xl">
        <div className="w-full text-center">
          <h2 className="font-semibold text-4xl capitalize">Login</h2>
          {error && <p className="w-full pt-2 italic text-red-600">{error}</p>}
        </div>
        <Formik
          initialValues={{
            email: "",
            password: "",
            isTeacher: ""
          }}
          validationSchema={signinSchema}
          onSubmit={(values, { setSubmitting }) => {
            setTimeout(() => {
              submitForm(values)
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
              className="w-40 py-2 mt-4 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-2xl"
            >
              login
            </button>
          </Form>
        </Formik>
        <div className="w-full text-center lg:flex lg:items-center lg:justify-between lg:px-8">
          <Link
            href={`/`}
            className="block text-black/60 hover:text-blue-900 hover:underline text-sm"
          >
            Don&apos;t have an account? Sign up
          </Link>
          <Link
            href={`#`}
            className="block text-black/60 hover:text-blue-900 hover:underline text-sm"
          >
            Forgot password?
          </Link>
        </div>
      </div>
    </>
  );
};
