"use client";

import React, {
  ClassAttributes,
  InputHTMLAttributes,
  useEffect,
  useState,
} from "react";
import { Formik, Form, useField, FieldHookConfig } from "formik";
import { signinSchema } from "../validation/schema";
import Link from "next/link";
import Cookies from "js-cookie";
import { useOutsideClick } from "../lib/useOutsideClick";
import {
  OtherProps,
  User,
  radioProps,
  searchProps,
  siginProps,
} from "../types";
import { useRouter } from "next/navigation";
import { useAuth } from "@/app/context/authContext";

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
  checkValue,
  data,
  optional,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLInputElement> &
  ClassAttributes<HTMLInputElement> &
  FieldHookConfig<string>) => {
  const [field, meta, helpers] = useField({
    name: props.name,
    validate: (value) => {
      let msg: string | undefined = undefined;

      if (data?.length == 0 || optional) return msg;

      const isValuePresent = data?.find(
        (item) => item.name === value || item.email === value
      );

      if (isValuePresent) {
        if (checkValue) checkValue(true, isValuePresent.id);
      } else {
        if (checkValue) checkValue(false);
        msg = "Please choose from list.";
      }

      return msg;
    },
    type: props.type,
  });
  const [filteredData, setData] = useState<any[]>(data!);
  const [focused, setFocus] = useState(false);

  const openFocus = () => setFocus(true);
  const closeFocus = () => setFocus(false);

  const setValue = (value: string) => {
    helpers.setValue(value);
    closeFocus();
  };

  const handleChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;

    const searchRegex = new RegExp(value, "gi");

    const filter = data?.filter((res) => {
      if (searchRegex.test(res.name)) return res;
    }) as any[];

    setData(filter);
  };

  const ref = useOutsideClick(closeFocus);

  useEffect(() => {
    if (data && data.length > 0 && field.value && checkValue) {
      const item = data.find((d) => d.name === field.value);
      if (item) checkValue(true, item.id);
    }
  }, []);

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
          {filteredData.map((item, i) => (
            <li
              className="w-full p-1 cursor-pointer hover:bg-blue-700 hover:text-white rounded"
              key={i}
              onClick={() => {
                setValue(item.name || item.email);
                if (checkValue) {
                  checkValue(true, item.id);
                }
              }}
            >
              {item.name || item.email}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export const MyTextAndCheckInput = ({
  label,
  checkValue,
  data,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLInputElement> &
  ClassAttributes<HTMLInputElement> &
  FieldHookConfig<string>) => {
  const [field, meta, helpers] = useField({
    name: props.name,
    validate: (value) => {
      let msg: string | undefined = undefined;
      const isValuePresent = data?.find((item) => item.name === value);

      if (isValuePresent) {
        if (checkValue) checkValue(true, isValuePresent.id);
      } else {
        if (checkValue) checkValue(false);
        msg = "Please choose from list.";
      }

      return msg;
    },
    type: props.type,
  });
  const [filteredData, setData] = useState<any[]>(data!);
  const [focused, setFocus] = useState(false);

  const openFocus = () => setFocus(true);
  const closeFocus = () => setFocus(false);

  const setValue = (value: string) => {
    helpers.setValue(value);
    closeFocus();
  };

  const handleChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;

    const searchRegex = new RegExp(value, "gi");

    const filter = data?.filter((res) => {
      if (searchRegex.test(res.name)) return res;
    }) as any[];

    setData(filter);
  };

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
              onClick={() => {
                setValue(city.name);
                if (checkValue) {
                  checkValue(true, city.id);
                }
              }}
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
export const Radio = ({ label, name, value, type, checked }: radioProps) => {
  const [isChecked, setIsChecked] = useState(checked);

  const handleChange = (e: React.ChangeEvent) => setIsChecked((prev) => !prev);
  return (
    <label htmlFor={`${value}`} className="font-normal flex items-center gap-1">
      <input
        id={`${value}`}
        type={type}
        name={name}
        value={`${value}`}
        checked={isChecked}
        onChange={handleChange}
      />
      {label}
    </label>
  );
};

export const CheckBox = ({ label, name, value, type, checked }: radioProps) => {
  const [isChecked, setIsChecked] = useState(checked);

  const handleChange = (e: React.ChangeEvent) => setIsChecked((prev) => !prev);

  return (
    <label htmlFor={`${value}`} className="font-normal flex items-center gap-1">
      <input
        id={`${value}`}
        type={type}
        onChange={handleChange}
        name={name}
        value={`${value}`}
        checked={isChecked}
      />
      {label}
    </label>
  );
};

// create a custom FieldSet component that uses the useField hook
//this component can be contained in another file
export const FieldSet = ({
  label,
  customStyle,
  options,
  ...props
}: OtherProps &
  InputHTMLAttributes<HTMLFieldSetElement> &
  ClassAttributes<HTMLFieldSetElement> &
  FieldHookConfig<string>) => {
  const [field, meta] = useField(props);
  return (
    <div className={`w-full ${customStyle}`}>
      {/* <div className="w-full md:col-span-full"> */}
      <label className="w-full font-medium">
        {label}
        {/* make sure the radios are contained in a fieldset */}
        <fieldset
          {...field}
          {...props}
          className="w-full grid grid-cols-2 gap-2 p-2"
        >
          {options?.map((option, i) => {
            if (option.type === "radio") {
              return (
                <Radio
                  key={`${i}`}
                  name={option.name}
                  label={option.label}
                  value={option.value}
                  type={option.type}
                  checked={option.checked}
                />
              );
            }
            return (
              <CheckBox
                key={`${i}`}
                name={option.name}
                label={option.label}
                value={option.value}
                type={option.type}
                checked={option.checked}
              />
            );
          })}
        </fieldset>
      </label>
      {meta.touched && meta.error ? (
        <div className="error text-xs text-red-600">{meta.error}</div>
      ) : null}
    </div>
  );
};

export const SignInForm = () => {
  const { updateUser } = useAuth()!;
  // const [error, setError] = useState<string | null>()
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
        Cookies.set("currentUser", JSON.stringify(user));
        updateUser();
        router.push("/dashboard");
      } else {
        alert("Invalid credentials, try again.");
      }
      // if (response.status != 200) setError("Invalid credentials");
    } catch (e) {
      let errorMessage = "Something went wrong. Try again later.";
      if (e instanceof Error) {
        errorMessage = e.message;
      }
      alert(errorMessage);
    }
  };

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
            isTeacher: "",
          }}
          validationSchema={signinSchema}
          onSubmit={(values, { setSubmitting }) => {
            setTimeout(() => {
              submitForm(values);
              setSubmitting(false);
            }, 400);
          }}
        >
          {({ values }) => (
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
                  {
                    name: "isTeacher",
                    label: "Teacher",
                    value: true,
                    type: "radio",
                    checked: values.isTeacher === "true" ? true : false,
                  },
                  {
                    name: "isTeacher",
                    label: "Student",
                    value: false,
                    type: "radio",
                    checked: values.isTeacher === "false" ? true : false,
                  },
                ]}
              />
              <button
                type="submit"
                className="w-40 py-2 mt-4 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-2xl"
              >
                login
              </button>
            </Form>
          )}
        </Formik>
        <div className="w-full text-center lg:flex lg:items-center lg:justify-between lg:px-8">
          <Link
            href={`/signup`}
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
