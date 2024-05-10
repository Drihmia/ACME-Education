"use client"

import { Form, Formik } from 'formik';
import React from 'react'
import { FieldSet } from './form';
import { signupQuestion } from '../validation/schema';
import { useRouter } from 'next/navigation';

export const SignUpQuestion = () => {
    const navigation = useRouter()

    const submitForm = ({answer}: {answer: string}) => {    
        if (answer === "true") {
            navigation.push('/signup/teacher')
        } else {
            navigation.push('/signup/student')
        }
    }
    return (
        <div
        className={`w-full max-w-xl shadow-xl flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl`}
      >
        <Formik
          initialValues={{
            answer: ""
          }}
          validationSchema={signupQuestion}
          onSubmit={(values, { setSubmitting }) => {
            submitForm(values);
            setSubmitting(false);
          }}
        >
          {({ values }) => (
            <Form className="w-full flex flex-col lg:gap-4 items-center p-4 md:p-8 lg:px-16">
            <FieldSet
                label="Are you a Teacher or a Student?"
                name="answer"
                options={[
                  {
                    name: "answer",
                    label: "Teacher",
                    value: true,
                    type: "radio",
                    checked: values.answer === "true" ? true : false
                  },
                  {
                    name: "answer",
                    label: "Student",
                    value: false,
                    type: "radio",
                    checked: values.answer === "false" ? true : false
                  },
                ]}
              />
            <div className="flex items-center gap-4 justify-center md:col-span-full">
              <button
                type="submit"
                className="w-40 py-2 mt-8 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-xl"
              >
                Continue
              </button>
            </div>
          </Form>
          )}
        </Formik>
      </div>

    )
}