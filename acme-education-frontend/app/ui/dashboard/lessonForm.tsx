"use client";

import { useAuth } from "@/app/context/authContext";
import { deleteLesson, fetcher } from "@/app/lib/fetch";
import { institutionProps, lessonFormProps, subjectProps } from "@/app/types";
import {
  FieldSet,
  MyTextAndSelectInput,
  MyTextArea,
  MyTextInput,
} from "@/app/ui/form";
import { lessonSchema } from "@/app/validation/lessons";
import { Icon } from "@iconify/react/dist/iconify.js";
import { Form, Formik } from "formik";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import useSWR, { mutate } from "swr";

export const LessonForm = ({ id, action }: { id?: string; action: string }) => {
  const navigation = useRouter();
  const { user } = useAuth()!;
  const [lesson, setLesson] = useState<lessonFormProps | null>(null);

  const { data: institutionsData } = useSWR(
    `http://127.0.0.1:5000/api/v1/teachers/${user?.user_id}/institutions`,
    fetcher
  );
  const { data: subjectsData } = useSWR(
    `http://127.0.0.1:5000/api/v1/teachers/${user?.user_id}/subjects`,
    fetcher
  );

  useEffect(() => {
    if (id) {
      fetch(`http://127.0.0.1:5000/api/v1/lessons/${id}`)
        .then((res) => res.json())
        .then((data) => {
          const modifiedData = { ...data };
          const subject = subjectsData.find(
            (item: subjectProps) => item.id === modifiedData.subject_id
          );
          modifiedData.subject = subject.name;
          setLesson(modifiedData);
        });
    }
  }, [id, subjectsData]);

  if (!institutionsData || !subjectsData) return <p>Loading</p>;
  // if (!subjectsData || !institutionsData || (!lesson && action == "Edit")) return <p>Loading......</p>;
  if (!lesson && action == "Edit") return <p>Loading......</p>;
  if (lesson && action == "Edit") console.log(lesson);

  const submitForm = async (values: lessonFormProps) => {
    const institution = institutionsData?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;

    const subject = subjectsData?.find(
      (item: subjectProps) => item.name == values.subject
    );
    if (subject) values.subject_id = subject.id;

    values.teacher_id = user?.user_id;
    values.public = values.public === "true" ? true : false;

    // console.log(values);

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/v1/lessons/${id ? id : ""}`,
        {
          method: action === "Add" ? "POST" : "PUT",
          body: JSON.stringify(values),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const res_data = await response.json();

      if (res_data["error"]) {
        alert(res_data["error"]);
      } else {
        alert(`Lesson ${action == "Add" ? "added" : "updated"}`);
        mutate(
          `http://127.0.0.1:5000/api/v1/${user?.class.toLowerCase()}s/${
            user?.user_id
          }/lessons`
        );
        navigation.push("/dashboard/lessons");
      }

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
          subject: id ? lesson?.subject! : "",
          institution: id ? lesson?.institution! : "",
          name: id ? lesson?.name! : "",
          download_link: id ? lesson?.download_link! : "",
          description: id ? lesson?.description! : "",
          public: id ? lesson?.public! : "true",
        }}
        validationSchema={lessonSchema}
        onSubmit={(values, { setSubmitting }) => {
          submitForm(values);
          setSubmitting(false);
        }}
      >
        <Form className="w-full flex flex-col items-center md:grid md:grid-cols-2 md:gap-4 lg:gap-8 p-4 md:p-8 lg:px-16">
          <MyTextAndSelectInput
            label="Subject"
            name="subject"
            data={subjectsData}
            type="text"
            placeholder="e.g Mathematics"
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
              { name: "public", label: "Yes", value: true, type: "radio" },
              { name: "public", label: "No", value: false, type: "radio" },
            ]}
          />
          <div className="w-full flex items-center justify-end gap-2 col-span-full">
            <button
              type="submit"
              className="w-24 h-8 flex items-center justify-center p-2 bg-blue-100 text-black hover:text-white hover:bg-blue-700 rounded-md"
            >
              {action == "Add" ? "Publish" : "Update"}
            </button>
            {action == "Edit" && (
              <div
                onClick={async () => {
                  if (confirm("Are you sure you delete this lesson?")) {
                    const res = await deleteLesson(lesson?.id!);
                    console.log(res);
                    if (res["error"]) {
                      alert("Something went wrong.");
                    } else {
                      alert("Lesson deleted");
                      navigation.push("/dashboard/lessons");
                    }
                  }
                }}
                className="w-24 h-8 flex items-center justify-center p-2 bg-red-200 hover:bg-red-700 rounded-md hover:text-white cursor-pointer"
              >
                <Icon icon="material-symbols:delete-outline" /> Delete
              </div>
            )}
            <div
              onClick={() => {
                if (confirm("Are you sure you want to go back?")) {
                  navigation.back();
                }
              }}
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
