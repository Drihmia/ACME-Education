import { Form, Formik, useField, useFormik, useFormikContext } from "formik";
import { filterSchema } from "../validation/filter";
import { FieldSet, MyTextAndSelectInput, MyTextInput } from "./form";
import { lessonFormProps, subjectProps } from "../types";
import { useState } from "react";
import { LessonCard } from "./dashboard/lessonsCard";

interface filterFormProps {
  subjects: subjectProps[];
  lessons: lessonFormProps[];
  openModal: (val: string) => void;
  user_class: string
}

export const FilterForm = ({
  subjects,
  lessons,
  openModal,
  user_class
}: filterFormProps) => {
  const [filteredLessons, setFilteredLessons] = useState(lessons)

  const applyFilter = (values: {
    subject: string;
    name: string;
    public: string;
  }) => {
    const regex = new RegExp(values.name, "gi");

    const data = lessons
      .filter((lesson) => {
        if (values.name === "") return lesson;
        if (regex.test(lesson.name)) return lesson;
      })
      .filter((lesson) => {
        if (values.subject === "") return lesson;

        const subject = subjects.find((sub) => sub.name === values.subject);
        if (lesson.subject_id === subject?.id) return lesson;
      })
      .filter((lesson) => {
        if (values.public === "") return lesson;
        if (lesson.public && values.public === "true") return lesson;
        if (!lesson.public && values.public === "false") return lesson;
      });

    setFilteredLessons(data);
  };

  return (
    <>
    <div className="w-full">
      <p className="font-semibold text-lg mt-4">Filter By</p>
      <Formik
        initialValues={{
          subject: "",
          name: "",
          public: "",
        }}
        validationSchema={filterSchema}
        onSubmit={(values, { setSubmitting }) => {
          applyFilter(values);
          setSubmitting(false);
        }}
        onReset={(values, { resetForm }) => {
          values = {
            subject: "",
            name: "",
            public: "",
          };
          setFilteredLessons(lessons)
        }}
      >
        {({ values }) => (
          <Form className="w-full grid gap-4 lg:grid-cols-[2fr_2fr_2fr_1fr] lg:gap-6 lg:items-center">
          <MyTextAndSelectInput
            label="Subject"
            name="subject"
            data={subjects}
            type="text"
            placeholder="e.g Mathematics"
            optional={true}
          />
          <MyTextInput
            label="Name"
            name="name"
            type="text"
            placeholder="How to build a rocket"
          />
          <FieldSet
            label="Public"
            name="public"
            options={[
              {
                name: "public",
                label: "Yes",
                value: true,
                type: "radio",
                checked: values.public === "true" ? true : false
              },
              {
                name: "public",
                label: "No",
                value: false,
                type: "radio",
                checked: values.public === "false" ? true : false
              },
            ]}
          />
          <div className="flex items-center gap-2">
            <button
              type="submit"
              className="w-28 h-12 py-2 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-xl"
            >
              Apply filter
            </button>
            <button
              type="reset"
              className="w-20 h-12 py-2 bg-red-100 text-black hover:text-white hover:bg-red-600 capitalize rounded-xl"
            >
              Clear
            </button>
          </div>
        </Form>
        )}
      </Formik>
    </div>
    {filteredLessons.length > 0 ? (
      <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
        <li className="w-full grid grid-cols-[0.75fr_5fr_2fr_2fr_0.5fr] p-2 bg-blue-50 rounded-md">
          <span className="font-semibold">S/N</span>
          <span className="font-semibold">Title</span>
          <span className="font-semibold">Subject</span>
          <span className="font-semibold">Author</span>
          <span className="font-semibold">Public</span>
        </li>
        {filteredLessons.map((lesson: lessonFormProps, i: number) => (
          <LessonCard
            key={`${i}`}
            index={i}
            lesson={lesson}
            openModal={openModal}
            user_class={user_class}
          />
        ))}
      </ul>
    ) : (
      <p>You do not have any published lessons.</p>
    )}
    </>
  );
};
