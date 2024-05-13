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
import { LoadingSkeleton } from "../skeletons";

export const LessonForm = ({ id, action }: { id?: string; action: string }) => {
  const navigation = useRouter();
  const { user } = useAuth()!;
  const [lesson, setLesson] = useState<lessonFormProps | null>(null);

  const { data: institutions } = useSWR(
    `http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${user?.user_id}/institutions`,
    fetcher
  );
  const { data: subjects } = useSWR(
    `http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${user?.user_id}/subjects`,
    fetcher
  );
  const { data: classes } = useSWR(
    `http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${user?.user_id}/classes`,
    fetcher
  );

  useEffect(() => {
    if (id) {
      fetch(`http://${process.env.NEXT_API_ADDRESS}/api/v1/lessons/${id}`)
        .then((res) => res.json())
        .then((data) => {
          const modifiedData = { ...data };
          const subject = subjects.find(
            (item: subjectProps) => item.id === modifiedData.subject_id
          );
          modifiedData.subject = subject.name;
          setLesson(modifiedData);
        });
    }
  }, [id, subjects]);

  if (!institutions || !subjects || !classes) return <LoadingSkeleton />;
  if (!lesson && action == "Edit") return <LoadingSkeleton />;
  

  const submitForm = async (values: lessonFormProps) => {
    const institution = institutions?.find(
      (item: institutionProps) => item.name == values.institution
    );
    if (institution) values.institution_id = institution.id;

    const subject = subjects?.find(
      (item: subjectProps) => item.name == values.subject
    );
    if (subject) values.subject_id = subject.id;

    const cls = classes?.find((item: any) => item.name == values.class);
    if (cls) values.class_id = cls.id;

    values.teacher_id = user?.user_id;
    values.public = values.public === "true" ? true : false;

    console.log(values);

    try {
      const response = await fetch(
        `http://${process.env.NEXT_API_ADDRESS}/api/v1/lessons/${id ? id : ""}`,
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
        mutate(
          `http://${process.env.NEXT_API_ADDRESS}/api/v1/${user?.class.toLowerCase()}s/${
            user?.user_id
          }/lessons`
        );
        alert(`Lesson ${action == "Add" ? "added" : "updated"}`);
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
          subject: id && lesson ? lesson.subject : "",
          institution: id && lesson ? lesson.institution : "",
          name: id && lesson ? lesson.name : "",
          download_link: id && lesson ? lesson.download_link : "",
          description: id && lesson ? lesson.description : "",
          public: id && lesson ? lesson.public : "true",
          class: id && lesson ? lesson.class : "",
        }}
        validationSchema={lessonSchema}
        onSubmit={(values, { setSubmitting }) => {
          submitForm(values);
          setSubmitting(false);
        }}
      >
        <Form className="w-full flex flex-col items-center md:grid md:grid-cols-2 md:gap-4 lg:gap-8 p-4 md:p-8 lg:px-16">
          <MyTextInput
            label="Title of lesson"
            name="name"
            type="text"
            placeholder="you@example.com"
          />
          <MyTextAndSelectInput
            label="Subject"
            name="subject"
            data={subjects}
            type="text"
            placeholder="e.g Mathematics"
            disabled={action === "Add" ? false : true}
          />
          {action === "Add" && (
            <>
              <MyTextAndSelectInput
                label="Institution (Optional)"
                name="institution"
                data={institutions}
                type="text"
                placeholder="e.g Insitute of Science and Technology"
                optional={true}
              />
              <MyTextAndSelectInput
                label="Class (Optional)"
                name="class"
                data={classes}
                type="text"
                placeholder="e.g Primary One"
                optional={true}
              />
            </>
          )}
          <MyTextInput
            label="Download URL"
            name="download_link"
            type="text"
            placeholder="you@example.com"
          />
          <FieldSet
            label="Should the lesson be publicly available?"
            name="public"
            options={[
              {
                name: "public",
                label: "Yes",
                value: true,
                type: "radio",
                checked: true,
              },
              {
                name: "public",
                label: "No",
                value: false,
                type: "radio",
                checked: false,
              },
            ]}
          />
          <MyTextArea
            label="Description"
            name="description"
            type="text"
            placeholder="Write a description of the lesson"
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
                    if (res["error"]) {
                      alert("Something went wrong.");
                    } else {
                      mutate(
                        `http://${process.env.NEXT_API_ADDRESS}/api/v1/${user?.class.toLowerCase()}s/${
                          user?.user_id
                        }/lessons`
                      );
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
