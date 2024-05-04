"use client";

import { deleteLesson, fetcher } from "@/app/lib/fetch";
import { institutionProps, lessonFormProps } from "@/app/types";
import { FieldSet, MyTextAndSelectInput, MyTextArea, MyTextInput } from "@/app/ui/form";
import { lessonSchema } from "@/app/validation/lessons";
import { Icon } from "@iconify/react/dist/iconify.js";
import { Form, Formik } from "formik";
import { useRouter } from "next/navigation";
import useSWR from "swr";

export const LessonForm = ({
  id,
  action,
}: {
  id?: string;
  action: string;
}) => {
  const navigation = useRouter();

  const { data: institutionsData } = useSWR(
    "http://127.0.0.1:5000/api/v1/institutions",
    fetcher
  );

  const submitForm = async (values: lessonFormProps) => {

    const institution = institutionsData?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;

    // values.teacher_id = use
    values.public = values.public === "true" ? true : false

    console.log(values);

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/v1/lessons/${id}`,
        {
          method: "POST",
          body: JSON.stringify(values),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const res_data = await response.json();

      // setResponse({
      //   status: response.status == 201 ? "success" : "error",
      //   message: response.status == 201 ? "OK" : res_data.error,
      // });
    } catch (e) {
      let errorMessage = "Something went wrong. Try again later.";
      if (e instanceof Error) {
        errorMessage = e.message;
      }
      // setResponse({ status: "error", message: errorMessage });
    }
  };

  return (
    <div className="w-full max-w-5xl mx-auto flex flex-col items-center justify-center gap-4 py-8">
      <div className="w-full text-center">
        <h2 className="font-semibold text-4xl capitalize">
          {action == "Add" ? "Publish New Lesson" : "Edit"}
        </h2>
      </div>
      <Formik
        initialValues={{
          subject: "Rocket Science",
          institution: "College of Science And Technology",
          name: "How to build a rocket",
          download_link: "https://goal.com",
          description: "",
          public: "true",
        }}
        validationSchema={lessonSchema}
        onSubmit={(values, { setSubmitting }) => {
          submitForm(values);
            setSubmitting(false);
        }}
      >
        <Form className="w-full flex flex-col items-center md:grid md:grid-cols-2 md:gap-4 lg:gap-8 p-4 md:p-8 lg:px-16">
          <MyTextInput
            label="Subject"
            name="subject"
            type="text"
            placeholder="you@example.com"
          />
          <MyTextAndSelectInput
              label="Name of Institution"
              name="institution"
              data={institutionsData}
              type="text"
              placeholder="e.g Insitute of Science and Technology"
            />
          <MyTextInput
            label="Name"
            name="name"
            type="text"
            placeholder="you@example.com"
          />
          <MyTextInput
            label="Download URL"
            name="download_link"
            type="text"
            placeholder="you@example.com"
          />
          <MyTextArea
            label="Description"
            name="description"
            type="text"
            placeholder="Write a description of the lesson"
          />
          <FieldSet
            label="Should the lesson be publicly available?"
            name="public"
            options={[
              { name: "public", label: "Yes", value: true },
              { name: "public", label: "No", value: false },
            ]}
          />
          <div className="w-full flex items-center justify-end gap-2 col-span-full">
            <button
              type="submit"
              className="w-24 h-8 flex items-center justify-center p-2 bg-blue-100 text-black hover:text-white hover:bg-blue-700 rounded-md"
            >
              { action == "Add" ? "Publish" : "Update"}
            </button>
            {action == "Edit" && (
              <div onClick={async() => {
                // change later
                // await deleteLesson(lesson.id!)
              }} className="w-24 h-8 flex items-center justify-center p-2 bg-red-200 hover:bg-red-700 rounded-md hover:text-white cursor-pointer">
                <Icon icon="material-symbols:delete-outline" /> Delete
              </div>
            )}
            <div
              onClick={() => navigation.back()}
              className="w-24 h-8 flex items-center justify-center p-2 bg-slate-200 hover:bg-black rounded-md hover:text-white cursor-pointer"
            >
              <Icon icon="material-symbols:delete-outline" /> Cancel
            </div>
          </div>
        </Form>
      </Formik>
    </div>
  );
};
